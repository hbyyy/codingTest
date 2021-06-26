from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            first_byte = bin(data[idx])[2:].zfill(8)
            byte_count = 0
            for i in first_byte:
                if i == '0':
                    break
                else:
                    byte_count += 1

            if byte_count == 1 or byte_count > 4:
                return False

            idx += 1

            if byte_count:
                byte_count -= 1
                for i in range(byte_count):
                    if idx >= len(data) or not bin(data[idx])[2:].zfill(8).startswith('10'):
                        return False
                    idx += 1

        return True


## 모범 답안

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(idx + 1, idx + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        idx = 0

        while idx < len(data):
            first = data[idx]
            if (first >> 3) == 0b11110:
                if not check(3):
                    return False
                idx += 4
            elif (first >> 4) == 0b1110:
                if not check(2):
                    return False
                idx += 3
            elif (first >> 5) == 0b110:
                if not check(1):
                    return False
                idx += 2
            elif (first >> 7) == 0:
                idx += 1
            else:
                return False

        return True
