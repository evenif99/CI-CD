class Sports:
    def __init__(self, name, entry):
        self.name = name
        self.entry = entry
    # end def __init__

    def showInfo(self):
        print('종목 : ' + self.name)
        print('엔트리 : ' + str(self.entry))
    # end def showInfo

class BaseBall(Sports):
    def __init__(self, name, entry, batting_rate):
        super().__init__(name, entry)
        self.batting_rate = batting_rate
    # end def __init__

    def showInfo(self):
        super().showInfo()
        print('타율 : {:.6f}'.format(self.batting_rate))
    # end def showInfo

class FootBall(Sports):
    def __init__(self, name, entry, goal_count):
        super().__init__(name, entry)
        self.goal_count = goal_count
    # end def __init__

    def showInfo(self):
        super().showInfo()
        print('골 수  : ' + str(self.goal_count))
    # end def showInfo

base = BaseBall('야구', 9, 0.235)
base.showInfo()
print('-' * 20)

foot = FootBall('축구', 11, 5)
foot.showInfo()
print('-' * 20)