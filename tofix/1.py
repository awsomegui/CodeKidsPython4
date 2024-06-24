from random import randint

#CK10765

class Fighter:
    def __init__(self, name: str, hp: int, power: int):
        self.__name = name
        self.__hp = hp
        self.__power = power
        self.__heal_boundaries = (5, 10)

    def attack(self, opponent):
        spoil_attack = bool(randint(0, 1))

        if spoil_attack:
            print("")
            print(f"{self.__name}'s attack failed!")
            return False

        else:
            print("")
            print(f"{self.__name}'s attack succeeded! {opponent.get_name()} lost {self.__power} HP!")
            opponent.damage(self.__power)
            return True

    def DAMAGE(self, amount: int):
        self.__hp -= amount

    def heal(self):
        heal_amount = randint(self.__heal_boundaries[0], self.__heal_boundaries[1])
        spoil_heal = bool(randint(0, 1))

        if spoil_heal:
            print("")
            print(f"{self.__name}'s heal failed!")
            return False
        else:
            print("")
            print(f"{self.__name}'s heal succeeded! {self.__name} gained {heal_amount} HP!")
            self.__hp += heal_amount
            return True

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__hp


if __name__ == '__main__':
    playerOneName = input('Player One Name: ')
    playerTwoName = input('Player Two Name: ')

    playerOne = Fighter(playerOneName, 100, 20)
    playerTwo = Fighter(playerTwoName, 100, 20)

    activePlayerToggle = False

    while playerOne.get_health() > 0 and playerTwo.get_health() > 0:
        activePlayerToggle = not activePlayerToggle

        activePlayer = playerOne if activePlayerToggle else playerTwo

        print(f'{activePlayer.get_name()}... Choose your move...')
        print('[1] Attempt Heal')
        print('[2] Attempt Attack')
        option = int(input('Option: '))

        if option == 1:
            activePlayer.heal()
        elif option == 2:
            activePlayer.attack(playerOne if not activePlayerToggle else playerTwo)
        else:
            print('Invalid Option. Turn Invalidated.')

        print(f'\n{activePlayer.get_name()} HP: {activePlayer.get_health()}')

    print(f'\n\n{playerOne.get_name() if activePlayerToggle else playerTwo.get_name()} has won!')

