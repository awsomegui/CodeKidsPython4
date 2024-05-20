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

root = tk.Tk()
root.title('Pokemon Card Wiki')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#21aeff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Card Info', font=40, command=get_input)
button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()