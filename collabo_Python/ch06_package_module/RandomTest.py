import random

# 0.0 <= 값 <1.0
print(random.random())

# random.seed(1234) # 시드 배정하면 항상 동일한 값이 나옴
print(random.random())

print(random.randint(1, 10))

coffees = ['아메리카노', '카페라떼', '아이스커피', '디카페인커피', '바닐라라떼']
print(random.choice(coffees))

random.shuffle(coffees)
print(coffees)

# 로또 번호 생성
lottoNumber = [su for su in range(1, 46)]
random.shuffle(lottoNumber)
print(lottoNumber)

lotto = lottoNumber[0:6]
print('당첨 번호 : ', lotto)

second = lottoNumber[6:7]
print('2등 당첨 : ', second)


def extractLottoNo():
    random.shuffle(lottoNumber)
    lotto = sorted(lottoNumber[0:6])
    second = lottoNumber[6:7]
    return lotto, second
#end def extractLottoNo

# 로또 5게임 출력하기
for idx in range(1, 6):
    print(f'\n{idx} 번째 게임')
    lotto, second = extractLottoNo()
    print('당첨 번호 : ', lotto)
    print('2등 당첨 : ', second)

# end for

# 다음 명단을 이용하여, 1조당 2명씩 조 배정을 해보세요.
MEMBER_SU = 2 # 조원 멤버 수

members = ['이민정', '최현미', '강유식', '김정식', '안미주', '심현철', '오지훈', '이한나']

random.shuffle(members)
print()
print(members)
print('-'*30)

for idx in range(0, len(members), MEMBER_SU):
    print(members[idx:idx + MEMBER_SU])
# end for

n = 3
sampling = random.sample(members, n)
print(sampling)
