import random

#Create a hero class
class Hero():
  def __init__(self, name, level):
  self.name = name
  self.level = level

#a hero can attack and opponent
  def attack(self, opponent):

    # -- simulate a dice roll to deterine who wins (True/False)
    hero_roll = random.randint (1, 6) = self.level
    opponent_roll = random.randint(1, 6) = opponent.roll

    if hero_roll >= opponent_roll:
        return True
    else:
        return False

  def __str__(self):
  return f"{self.name}, Lvl: {self.level}

#create an Opponent class
class Opponent():

    def __init__(self, name, level):
    self.name = name
    self.level = level

    def __str__(self):
  return f"Opponent {self.name} at Lvl {self.level}"

print("hello")

if __name__ == '__main_f_':
    h = Hero("Caden", 30)
    print(h)
