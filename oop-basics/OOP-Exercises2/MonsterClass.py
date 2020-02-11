
class Monster():
    def __init__(self, name, strength, scary_skills):
        self.name = name
        self.strength = strength
        self.scary_skills = scary_skills

    def eat(self, food = ''):
        return 'nom nom nom nom' + ' ' + food

    def sleep(self):
        return 'zzzzzzzzzzzz'

    def pay_taxes(self,amount = ''):
        if amount != '':
            return 'Why do i have to pay so many taxes. I have to pay ' + ' ' + amount + ' ' + 'pounds'
        else:
            return 'Why do i have to pay so many taxes.'

    def shout_strength(self):
        return 'R' * self.strength + '!' * self.strength

