class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # end def __init__

    def getName(self):
        return self.name + '님'

    # end def getName

    def showData(self):
        print('이름 : ' + str(self.name))
        print('나이 : ' + str(self.age))
        print('성별 : ' + str(self.gender))
    # end def showData
# end class Person

class Employee(Person): # 서브클래스(슈퍼클래스)
    def __init__(self, name, age, gender, salary, hiredate):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hiredate = hiredate
    # end def __init__

    def showData(self):
        super().showData()
        print('급여 : ' + str(self.salary))
        print('입사일자 : ' + str(self.hiredate))
    # end def showData

    def doWork(self):
        print(super().getName() + ' 열심히 일합시다.')
    # end def doWork
# end class Employee

class Student(Person):
    def __init__(self, name, age, gender, subject, grade):
        super().__init__(name, age, gender)
        self.subject = subject
        self.grade = grade
    # end def __init__

    def showData(self):
        super().showData()
        print('과목 : ' + str(self.subject))
        print('성적 : ' + str(self.grade))
    # end def showData

    def doStudy(self):
        print(super().getName() + ' 열심히 공부합시다.')
    # end def doWork
# end class Student

soo = Employee('김철수', 20, '남자', 50000, '2020/12/25')
soo.showData()
soo.doWork()
print( '-' * 20 )

hee = Student('박영희', 19, '여자', '국어', 'A학점')
hee.showData()
hee.doStudy()
print( '-' * 20 )

# Person 클래스를 상속 받는 Teacher 클래스를 구현해 보세요.
# kim = Teacher('김유신', 40, '남자', '파이썬')
# kim.showData()
# kim.doTeach() # 파이썬을 가르칩니다.