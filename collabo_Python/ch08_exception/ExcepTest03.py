class MinJumsuException(Exception):
    def __init__(self, value):
        self.message = f'{value}님은(는) 과락 대상입니다.'

    def __str__(self):
        return f'{self.message}'
# end class MinJumsuException

class FailedException(Exception):
    def __init__(self, value):
        self.message = f'{value}님은(는) 불합격입니다.'
    def __str__(self):
        return f'{self.message}'
# end class FailedException


name = input('이름 입력 :')
kor = input('국어 점수 입력 :')
eng = input('영어 점수 입력 :')
math = input('수학 점수 입력 :')

try:
    name = str(name)
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    scores = [kor, eng, math]

    if any(score < 40 for score in scores):
        raise MinJumsuException(name)
    elif (kor + eng + math)/3 < 65:
        raise FailedException(name)
    else:
        print(f'{name}님 합격입니다.')

except MinJumsuException as err:
    # 과락 전용 처리
    print('시험을 잘못 보셨군요')
    print(err)

except FailedException as err:
    # 평균 미만 전용 처리
    print('조금만 더 공부하시길 바랍니다.')
    print(err)

except ValueError as err:
    print('올바른 형식을 입력해 주셔야 합니다.')
    print(err)

except Exception as err:
    print('기타 오류 발생 : ', err)
# end try