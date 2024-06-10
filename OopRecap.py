"""
Topic: Pokemon Backpack
Date: 29/04/2024
Author: Hugo
"""

class Pokemon:
    def __init__(self, name: str, hp: int, type: str, searchname: str):
        self._name = name
        self._hp = hp
        self._type = type
        self._searchname = searchname
        self._attacks = {}
    def add_attack(self, attackName: str, attackDamage: int):
        self._attacks[attackName] = attackDamage
    def get_name(self):
        return self._name
    def get_searchname(self):
        return self._searchname
    def get_type(self):
        return self._type
    def __str__(self):
        displayString = ''
        displayString += f'\nName: {self._name}'
        displayString += f'\nHP: {self._hp}'
        displayString += f'\nType: {self._type}'
        displayString += f'\nAttacks: | '

        for attack in self._attacks:
            displayString += attack + ' | '
        return displayString

class ShinyPokemon(Pokemon):
    def __init__(self, name: str, hp: int, type: str, searchname: str):
        super().__init__(name, hp, type, searchname)

    def __str__(self):
        return  '\n\n--[[ SHINY POKEMON ]]--' + super().__str__()

if __name__ == '__main__':
    yanmega = Pokemon('Yanmega', 80, 'Grass', 'yanm')
    yanmega.add_attack('Supersonic', 10)
    yanmega.add_attack('Cutting Wind', 120)

    pikipek = Pokemon('Pikipek', 60, 'Colorless', 'piki')
    pikipek.add_attack('Send Back', 0)
    pikipek.add_attack('Peck', 20)

    pikachu = ShinyPokemon('Pikachu', 80, 'Electric', 'pika')
    pikachu.add_attack('Thunderbolt', 30)

    print(yanmega)
    print(pikipek)
    print(pikachu)