
from bunker import  BunkerCreator
from disaster import DisasterCreator
from players import PlayerCreator
import random
about_player = PlayerCreator()
info_disaster = DisasterCreator()



print("-------")

class Session :
    mass_with_3_quality = []


    def first_round(self):


        for i in about_player.mass_with_info:
            for q in range(3):
                print(i.pop())
            print("---next player---")
            self.mass_with_3_quality.append(i)
    def remove_player(self):
        x = random.randint(0,len(self.mass_with_3_quality)-1)
        del self.mass_with_3_quality[x]
        print(f"removed player number {x +1}")

    def regular_round(self):
        print("!---next round---!")

        for i in self.mass_with_3_quality:
            print("---next quality---")
            print(i.pop())
def main():
    game =Session()
    game.first_round()
    game.remove_player()
    game.regular_round()
    game.remove_player()
    game.regular_round()
    game.remove_player()
    game.regular_round()
if __name__ == "__main__":
    main()


















    