def studentCheck(name):

    students = ['철수', '영희', '민수', '지영']

    if name in students:
        print(f'\'{name}\' 학생은 출석하였습니다')

    else:
        message = f'\'{name}\' 학생은 출석하지 않았습니다.'
        raise Exception(message)
    # end def studentCheck

try:
    checkList = ['철수', '훈식']
    for one in checkList:
        studentCheck(one)
    # end for

except Exception as err:
    print('결석 확인 : {}'.format(err))