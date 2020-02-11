from MonsterClass import  Monster


class StudentMonster(Monster):

    uni_id = 0

    def __init__(self, name, strength, scary_skills):
        super().__init__(name, strength, scary_skills)
        self.__subjects = ['Maths']
        self.__tiny_debt = 0
        self.uni_id = StudentMonster.uni_id
        StudentMonster.uni_id += 1

    def party(self):
        return 'Wooooooooo'

    def test(self,score):
        if score >70:
            return 'This is test is so easy'
        else:
            return 'That test was so hard'

    def be_poor(self,money = 0):
        if money > 0:
            return 'I can afford cheese today'
        else:
            return 'Guess its pasta tonight'

    def setter_subjects(self,*args):
        self.__subjects.extend(*args)

    def getter_subjects(self):
        return self.__subjects

    def strength(self):
        super.strength
        return 3 * super.strength

    def setter_debt_attribute(self, amount): #This is an interna
        self.__tiny_debt = amount

    def get_debt_value(self):
        input('What is your logging?')
        input('What is your password?')
        return self.__tiny_debt


