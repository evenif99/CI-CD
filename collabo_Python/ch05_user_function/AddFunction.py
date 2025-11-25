# 함수의 정의
# 매개 변수 : parameter, argument, 인자, 인수라고 부르기도 합니다.
# 자바와는 달리 매개 변수는 기본 값을 가질 수 있습니다.
# 오버로딩 개념이 없습니다.
def add(first, second=15):
    return first + second # 리턴 구문에는 해당 함수의 동작을 정의
# end def

su01=14
su02=5

# positional argument : index를 이용하여 매개 변수에 할당하는 방식, 일반적으로 많이 사용
result = add(su01, su02) # 함수의 호출
print('%d + %d = %d' % (su01, su02, result))

print('%d + %d = %d' % (100, 200, add(100, 200)))

# keyword argument : 매개변수 키워드를 이용하여 매개 변수에 할당하는 방식
result = add(second=su01, first=su02)
print('%d + %d = %d' % (su02, su01, result))

#  위의 두개의 방식 혼합(positonal, keyword)
result = add(15, second=20)
print('%d + %d = %d' % (15, 20, result))

result = add(10) # 매개변수의 기본값을 가질 수 있으며  해당 사항 시 함수에 대한 오류가 발생하지 않습니다.
print('%d' % result)