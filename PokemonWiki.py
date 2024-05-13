import tkinter as tk
from OopRecap import Pokemon, ShinyPokemon

pokemonCards = []

yanmega = Pokemon('Yanmega', 80, 'Grass')
yanmega.add_attack('Supersonic', 10)
yanmega.add_attack('Cutting Wind', 120)

pikipek = Pokemon('Pikipek', 60, 'Colorless')
pikipek.add_attack('Send Back', 0)
pikipek.add_attack('Peck', 20)

pikachu = ShinyPokemon('Pikachu', 80, 'Electric')
pikachu.add_attack('Thunderbolt', 30)

def searchPokemon(pokemonName: str):
    pass

def get_input():
    pass

HEIGHT = 500
WIDTH = 600