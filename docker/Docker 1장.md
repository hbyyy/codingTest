# Docker 1장, 2장

## Docker volume



```shell
docker run -v {호스트 디렉토리}/{컨테이너 디렉토리} ~~
```

- 호스트에 없는 디렉토리를 설정한다?
  - 호스트에 디렉토리가 생성됨
- 호스트에 이미 존재하는 디렉토리를 공유하면?
  - 컨테이너 디렉토리가 덮어씌워진다
    - 정확히는, 호스트의 디렉토리를 컨테이너의 디렉토리에 마운트

### Volume container

- 볼륨을 사용하는 컨테이너를 다른 컨테이너와 공유
  - 직접 공유하는 것이 아니라, 컨테이너를 통해 공유한다

```
docker run -it -v /home/hostvolume:/home/containervolume --name testcontainer1 ubuntu

docker run -it --volumes-from testcontainer1 ubuntu
docker run -it --volumes-from testcontainer2 ubuntu

```

- 볼륨 공유만 하는 컨테이너로 사용할 수 있다

### docker volume

- 볼륨을 생성 후 연결

```
docker volume create myvolume

docker run -it -v myvolume:/home/containervolume --name test1 ubuntu
docker run -it -v myvolume:/home/containervolume --name test2 ubuntu
```

- 여러 컨테이너에 연결해 사용할 수 있다

**실제로 어디 저장?**

```shell
docker inspect --type volume myvolume
[
    {
        "CreatedAt": "2021-09-02T22:26:32+09:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/myvolume/_data",	# 실제 저장 위치
        "Name": "myvolume",
        "Options": {},
        "Scope": "local"
    }
]

```

- volume create 시 스토리지 백엔드를 정해줄 수 있다. 기본은 local



## docker network

- 컨테이너 내부 ifconfig

  - ```
    root@3e5e1bb73a31:/# ifconfig
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    ...
    
    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
    ...
    ```

- 호스트 ifconfig

  - ```
    docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    ...
    
    enp3s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
    ...
    
    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
    ...
    
    veth944e9a9: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    ...
    
    wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    ...
    ```

**컨테이너는 생성될 때 호스트에서 veth... 라는 네트워크 인터페이스를 생성해 연결된다**

```
container1	etho0  < --- > host veth...   / ---> host docker 0  <---> host eth0
										 ^
container2	etho0  < --- > host veth...  |
										 ^
container3	etho0  < --- > host veth...  |
```



## docker log

```
docker logs my_container_name
```

- docker container의 표준 출력, 에러를 확인할 수 있다



### log 저장

- 컨테이너 로그는, JSON 형태로 **도커 내부에** 저장된다. 
- 호스트에서 확인하려면?
  - `/var/lib/docker/containers/{CONTAINER_ID}/{CONTAINER_ID}-json.log` 경로에 파일이 존재
- `--log-opt` 옵션으로 json 파일의 최대 크기, 최대 갯수를 정해줄 수 있다

