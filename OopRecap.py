"""
Topic: Pokemon Backpack
Date: 29/04/2024
Author: Hugo
"""

class Pokemon:
    def __init__(self, name: str, hp: int, type: str):
        self._name = name
        self._hp = hp
        self._type = type
        self._attacks = {}
    def add_attack(self, attackName: str, attackDamage: int):
        self._attacks[attackName] = attackDamage