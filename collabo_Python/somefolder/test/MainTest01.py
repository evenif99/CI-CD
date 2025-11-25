import somefolder.mymath.MathModule
import somefolder.sansu.SansuModule

# import 구문만 사용 시 패키지 경로가 길어지면 코드 또한 길어집니다.
print('# import 구문 사용하기')
su = 4
result = somefolder.mymath.MathModule.square_root(su)
print('루트 01 : ', result)

su01 = 3
su02 = 4
result = somefolder.mymath.MathModule.jegob(su01, su02)
print('제곱합 01 : ', result)

print('# from 패키지경로.모듈이름 import 함수')
# from somefolder.sansu.SansuModule import *
from somefolder.sansu.SansuModule import add
su01 = 5
su02 = 6
result = add(su01, su02)
print('합셈 : ', result)

from somefolder.sansu.SansuModule import sub
su01 = 10
su02 = 7
result = sub(su01, su02)
print('뺄셈 : ', result)

print('# from 패키지경로 import 모듈이름')
from somefolder.mymath import MathModule
su = 5
result = MathModule.square_root(su)
print('루트 02 : ', result)

su01 = 7
su02 = 8
result = MathModule.jegob(su01, su02)
print('제곱합 02 : ', result)

print('# 별칭 사용하기')
import somefolder.mymath.MathModule as mm
su = 11
result = mm.square_root(su)
print('루트 03 : ', result)