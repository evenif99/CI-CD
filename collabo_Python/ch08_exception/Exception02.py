# 품목을 주문하되, 존재하지 않으면 예외 발생시키기

def coffeeCheck(findItem):
    menu = ['아메리카노', '라떼' , '카푸치노', '바닐라라떼', '모카라떼']
    if findItem in menu:
        print(f'품목 \'{findItem}\'은(는) 판매 중입니다.')

    else: # 예외발생 시키기
        message = f'품목 \'{findItem}\'은(는) 판매하고 있지 않습니다.'
        raise Exception(message)
# end def coffeeCheck

try:
    orderList = ['아메리카노', '핫초코']
    for item in orderList:
        coffeeCheck(item)
    # end for

except Exception as err:
    print('예외 발생 : {}'.format(err))
# end try