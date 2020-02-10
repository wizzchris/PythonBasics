# Psydo Code
# Do monster class
# Do student Monster Class
# I need to inhert from the monster class

from MonsterClass import Monster
from SutdentMonster import StudentMonster

james = Monster('James', 5, 'Hands')
fred = StudentMonster('fred', 5, 'Scary Hands', '4256743', 'Chemistry')

print(Fred.subjects)

print(Fred.shout_strength)

##Example

class Monster():

    def __init__(self, name_arg, strength, scary_skills = []):
        self.name = name_arg
        self.strength = strength
        self.scary_skills = scary_skills

    def eat(self):
        return 'nom nom nom nom nom nom'

    def shout_strength(self):
        #We have access to the instance via the self function

        return