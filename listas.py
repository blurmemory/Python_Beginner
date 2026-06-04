# uso y explicacion de listas
#      -5   -4  -3  -2 -1
list = [91, -7, 44, 88, 4]
#       0   1   2  3   4

# for i in list:
#     print(i*2)

# pokemons=["Leafeon", "Ivysaur", "Metagross", "Psyduck", "Onorlax"]

# for p in pokemons:
#     print(p.upper())

fruit = ["Manzana", "Melon", "Tomate", "Banana", "Mango"]

for f in fruit:
    if f[-1].lower() == "a":
        print(f"La fruta {f} termina con A")
    else:
        print(f"La fruta {f} no termina con A")