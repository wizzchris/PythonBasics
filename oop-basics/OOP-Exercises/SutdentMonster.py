from MonsterClass import  Monster


class StudentMonster(Monster):
    subjects = ['Maths']

    def __init__(self, name, strength, scary_skills, uni_id, scary_subjects):
        super().__init__(name, strength, scary_skills)
        self.uni_id = uni_id
        self.subjects.append(scary_subjects)

    def party(self):
        return 'Wooooooooo'

    def test(self,score):
        if score >70:
            return 'This is test is so easy'
        else:
            return 'That test was so hard'

    def be_poor(self,money = 0):
        if money > 0:
            return 'I can afford cheese today'#
        else:
            return 'Guess its pasta tonight'

