import tkinter as tk
from OopRecap import Pokemon, ShinyPokemon

pokemonCards = []

yanmega = Pokemon('Yanmega', 80, 'Grass', 'yanm')
yanmega.add_attack('Supersonic', 10)
yanmega.add_attack('Cutting Wind', 120)
pokemonCards.append(yanmega)

pikipek = Pokemon('Pikipek', 60, 'Colorless', 'piki')
pikipek.add_attack('Send Back', 0)
pikipek.add_attack('Peck', 20)
pokemonCards.append(pikipek)

pikachu = ShinyPokemon('Pikachu', 80, 'Electric', 'pika')
pikachu.add_attack('Thunderbolt', 30)
pokemonCards.append(pikachu)

def searchPokemon(pokemonName: str):
    for pokemon in pokemonCards:
        if pokemonName.title() == pokemon.get_name():
            return pokemon

def get_input():
    pokemonName = entry.get()
    searchResult = searchPokemon(pokemonName)
    displayResult = ''

    if not searchResult:
        displayResult = 'No Pokemon Found'
    else:
        displayResult = str(searchResult)

    label['text'] = displayResult

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

lowerFrame = tk.Frame(root, bg='#21a3ff', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, wraplength=360, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()