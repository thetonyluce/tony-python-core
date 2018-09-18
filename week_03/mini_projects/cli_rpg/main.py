#import our package from the other file
import random
from rpg import Hero, Opponent


#make a main() function
def main():
    print("Welcome to this confusing game!")
    play_game()

#create a play_game() function with the logic of it all
def play_game():
    opponents = [
        Opponent("Messi", 99),
        Opponent("Ratikic", 94),
        Opponent("Pique", 89),
    ]
    #create the hero
    hero = Hero("Caden", 100)

    #ask for usr input and run until quit
    while True:

        cmd = input("Enter [A] for attack or [Q] to quit:")

        #check for input validity
        while cmd not in ["A, "Q"]
            cmd = input("Enter [A] for attack or [Q] to quit:")

        if cmd == "Q"
            print ("Quitter")
            exit

        elif cmd == "A"
            opponent = random.choice(opponents)

            if hero.attack(opponent):
                print("You are a winning winner!")

            else:
                print('You are a losing loser.')
                time.sleep(5)
                print ("Try again if you're into random games.")


            random.choice(opponents)
            hero.attack(Opponent)


if __name__ == '__main__':
    print("ho")
