def namePrint(name, age):
    return name + "님, " + "나이 : " + str(age) + "세"
#end def namePrint

def sayHello(word, retry= 10 ):

    for i in range(retry):
        print(word)
    print()
# end def