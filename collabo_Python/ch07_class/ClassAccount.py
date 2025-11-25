class Account: # 클래스 정의
    bankname = 'KB'

    def __init__(self, name, no, deposit): # self 사용 시 무조건 작성해놔야 한다.
        # 인스턴스 변수 : self 키워드를 사용하여 선언한 변수
        self.name = name
        self.no = no
        self.deposit = deposit
    # end def __init__

    def printData(self):
        print('예금주 : %s' % self.name)
        print('계좌번호 : %d' % self.no)
        print('예치금 : %d' % self.deposit)
    # end def printData
# end class Account

print('주거래은행 : %s' % Account.bankname)
print('-'*30)

soo = Account('김철수', 1234, 1000) # 객체 생성
soo.printData()

hee = Account('박영희', 5678, 2000) # 객체 생성
hee.printData()