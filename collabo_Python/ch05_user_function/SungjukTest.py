def sungjukInfo(name, kor, eng =50, math =60):
    total = kor + eng + math
    avg = total / 3.0

    if avg >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'
    # end if

    print('%s 학생의 성적표' % name)
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격 여부 : %s' % (total, avg, passOrFail))
    print()
# end def

name, kor, eng, math = '김철수', 50, 60, 70

# positional argument
sungjukInfo(name, kor, eng, math)
sungjukInfo('박영희', 80)

# keyword argument
sungjukInfo(math=30, eng=90, name='홍길동', kor=100)

#  위의 두개의 방식 혼합(positonal, keyword)
sungjukInfo('김민수', 80, math=90) # 영어는 기본값 할당

# keyword 방식은 positional 방식보다 앞에 놓일 수 없습니다.