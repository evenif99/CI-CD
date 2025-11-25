def sayHello(word, retry= 10 ):

    for i in range(retry):
        print(word)
    print()
# end def

sayHello('안녕하세요', 5)

sayHello(word='hello', retry=7)

sayHello(retry=3, word='곤니찌와')

sayHello('방가워요')