# 모듈 : 미리 작성된 함수 코드를 모아 놓은 파이썬 파일

import math
import lib   # 현재 프로젝트 폴더에서 lib 라는 파이썬 파일이 존재하는지 확인한 이후에 그 안에서 함수를 사용할 수 있도록 함.
# 모듈파일이 큰 경우, 특정한 모듈에서 특정한 기능만 이용하도록 할 수 있음
from lib import add
# 모듈 파일이 지나치게 긴 경우, 이 해당 모듈을 간략하게 사용할 때 as 를 사용
import lib as t   # lib 라는 모듈을 t 라는 짧은 별칭으로 사용하겠다.

print(math.pow(3,8))
print(math.sqrt(64))
print(math.gcd(72,24))

print(lib.add(3,5))
print(lib.subtract(3,5))

print(add(10,20))
print(t.add(10,20))
