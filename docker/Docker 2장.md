# Docker 2장

## Docker image 만들기

### docker commit

- container 를 이미지로 만들 수 있다

- `docker commit [OPTION] CONTAINER_NAME [REPOSITORY[:TAG]]`

- ```shell
  docker run -it --name commit_test ubuntu:14.04
  
  root@9e3e794745f3:/# echo "test commit" >> first
  
  
  ~/Desktop/Docker 8s
  ❯ docker commit -a "hbyyytest" -m "first commit" commit_test commit_test:first
  sha256:d487ec78a72b4bec6dc34985cf0030fc2197907e0909a76566ceceba9d0d6b5f
  
  ~/Desktop/Docker
  ❯ docker images                                                               
  REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
  commit_test   first     d487ec78a72b   3 seconds ago   197MB
  rabbitmq      latest    5744a9083332   2 months ago    219MB
  ubuntu        14.04     13b66b487594   5 months ago    197MB
  
  ```

### Layer

- 위에서 만든 image 의 Layer를 확인해 보자

| ubuntu:14.04                                                 | commit_test:first                                            | commit_test:second                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| "Layers": [                <br />"sha256:f2fa9f..",      "sha256:30d3c4..",                "sha256:83109f.."            ] | "Layers": [<br />"sha256:f2fa9f..",      <br />"sha256:30d3c4..",         "sha256:83109f..",          "sha256:c4ec79.."            ] | "Layers": [               <br /> "sha256:f2fa9f..",               <br /> "sha256:30d3c4..",                <br />"sha256:83109f..",                "sha256:c4ec79..",                "sha256:bebf09.."            ] |

- 컨테이너 내용 변경 후 commit 할 때, **변경된 사항**만 새로운 레이어로 저장한다.

### Docker image 삭제

- `docker rmi IMAGE_NAME`
- **실행 중인** 컨테이너가 있는 이미지는 삭제할 수 없다.
  - `-f` 옵션을 주면 삭제 가능하지만, 실제로 이미지 레이어를 삭제하지는 않고 이미지 이름만 삭제해 `<none>` 이미지로 남는다 (Dangling image)
    - `docker image prune` 으로 삭제 가능
- **다른 이미지가 기반으로 하는** 이미지는 삭제할 수 없다.
  - 삭제 명령어는 수행되지만, 이름만 삭제하는 식으로 진행한다.

### 이미지 추출, 로드

- `docker save -o NAME.tar [OPTION] IMAGE_NAME `
- `docker load -i [TAR_FILE] `

- 이미지를 단일 바이너리 파일로 저장하고 로드할 수 있다 (`.tar`)
- **모든 이미지 Layer** 를 저장하기 때문에, 효율적이지 않다



## Image Build

- 애플리케이션을 Image 로 만드는 과정을 살펴보면, 다음과 같다
  1. 빈 이미지 (ubuntu, python 등)를 가져와 컨테이너 생성
  2. 컨테이너에 변경사항을 적용(환경설정, 소스코드 복제 등)
  3. 컨테이너를 **commit**

이런 식으로 진행한다면, 계속해서 수작업으로 패키지를 설치하고, 소스코드를 가져오고 하는 과정을 진행해야 한다

이와 같은 과정을 하나의 파일(**Dockerfile**) 에 기록해 놓고, 쉽게 수행할 수 있는 기능이 **`docker build`** 기능



### Dockerfile

- Dockerfile 을 작성해야 하는 이유는,
  1. 이미지를 생성하는 방법을 기록해서, 동일한 이미지를 생성하는 걸 보장할 수 있다
  2. 따라서 빌드, 배포 시 계속해서 같은 환경을 유지할 수 있을 것이다

#### 문법

- 기본적으로 사용되는 명령어로는 **FROM, RUN, ADD** 등이 있다.

```dockerfile
FROM ubuntu:18.04
MAINTAINER hbyyytest
LABEL "purpose"="practice"

RUN apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN	apt install -y nginx
ADD my_nginx.conf /etc/nginx/
WORKDIR /src/app
EXPOSE 80
CMD nginx -g "daemon off;"
```



##### FROM

- 생성할 이미지의 베이스가 될 이미지를 적어준다

##### MAINTAINER

- Image를 만든 개발자의 정보
  - deprecated docker 1.13.0

##### LABEL

- 이미지에 메타데이터를 추가한다
  - `LABEL maintainer "hbyyy <hbyyy@hbyyy.com>"`

##### RUN

- 이미지를 만들기 위해 container 안에서 명령어를 실행한다
- Dockerfile 빌드 과정에서는 **별도의 입력이 불가** 하므로, 입력을 자동으로 수행하는 옵션을 꼭 붙여 준다
- `RUN ["/bin/bash", "echo hello"]` 와 같이, 배열 식으로 사용할 수도 있다.
  -  `RUN ["echo", "$MY_TEST_ENV"]` 는 불가, `RUN ["sh", "-c", "echo $MY_TEST_ENV"]` 처럼 사용해야 한다.

##### ADD

- 파일을 이미지에 추가한다
- 파일의 위치는 **Dockerfile이 위치한 디렉터리에서 가져온다**
  - 이 디렉터리를 Context 라고 함
- 비슷한 **COPY** 명령어도 있다
  - COPY 는 로컬에서만 복사하는 기능을 가짐
  - ADD 는 wget 등을 통해 원격지의 파일을 복사하는 긴으, 파일이 .tar 등 압축파일일 때 자동으로 해제해 주는 기능 등이 있다

##### EXPOSE

- **컨테이너가 사용할 내부 포트**를 지정해 준다



### docker build

- r`docker build [-t DOCKERFILE_NAME] [OPTION] DOCKERFILE_PATH`
  - `-t` 명령어가 없으면 16진수 형태의 이름을 가진 이미지를 만든다

#### Build 과정

##### Build context

- Dockerfile이 위치한 디렉터리
- 이 위치에는 **빌드에 불필요한 파일**들이 없도록 해야 한다
  - 빌드 속도 저하
  - 메모리 점유율 증가

`.gitignore` 와 비슷하게, `.dockerignore` 파일을 작성해 컨텍스트에서 제외할 수 있다

##### 컨테이너 생성, 커밋

- Dockerfile 의 명령어 한 줄이 **하나의 Layer** 이다

```shell
❯ docker build -t my_test_docker_image ./
Sending build context to Docker daemon   2.56kB
Step 1/9 : FROM ubuntu:18.04
18.04: Pulling from library/ubuntu
e4ca327ec0e7: Pull complete 
Digest: sha256:9bc830af2bef73276515a29aa896eedfa7bdf4bdbc5c1063b4c457a4bbb8cd79
Status: Downloaded newer image for ubuntu:18.04
 ---> 54919e10a95d
Step 2/9 : MAINTAINER hbyyytest
 ---> Running in fb1965b11339
Removing intermediate container fb1965b11339
 ---> 4c7f71d506c8
Step 3/9 : LABEL "purpose"="practice"
 ---> Running in 9ee6524e00da
 # Step 마다 임시 container를 생성하고, 삭제한다
Removing intermediate container 9ee6524e00da
 ---> 081733074d38
Step 4/9 : RUN apt -y update && apt -y dist-upgrade && apt -y autoremove
 ---> Running in 52bcf17d2f69
....
```



## Docker daemon



### 도커의 구조

```
❯ ps aux | grep docker
root      2152  0.0  0.4 1792040 76264 ?       Ssl  21:29   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
hby       8467  0.0  0.0  15724  1048 pts/0    S+   21:55   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn docker

~
❯ which docker         
/usr/bin/docker

```



- docker client
  - 사용자의 입력을 받아 API 호출 (to docker daemon)
- docker daemon
  - API 입력을 받아 실제 기능을 수행한다 

```
									/var/run/docker.sock

docker version --------> docker client -----------> docker deaemon
```

