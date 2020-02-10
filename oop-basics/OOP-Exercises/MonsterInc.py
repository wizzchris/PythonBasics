# Psydo Code
# Do monster class
# Do student Monster Class
# I need to inhert from the monster class

from MonsterClass import Monster
from SutdentMonster import StudentMonster

james = Monster('James', 5, 'Hands')
fred = StudentMonster('fred', 5, 'Scary Hands', '4256743')

fred.setter_subjects(['Chem','bio','food tech'])
print(fred.getter_subjects())

