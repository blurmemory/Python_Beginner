# uso y explicacion de listas
#      -5   -4  -3  -2 -1
list = [91, -7, 44, 88, 4]
#       0   1   2   3   4

# for i in list:
#     print(i*2)

# pokemons=["Leafeon", "Ivysaur", "Metagross", "Psyduck", "Onorlax"]

# for p in pokemons:
#     print(p.upper())

# fruit = ["Manzana", "Melon", "Tomate", "Banana", "Mango"]

# for f in fruit:
#     if f[-1].lower() == "a":
#         print(f"La fruta {f} termina con A")
#     else:
#         print(f"La fruta {f} no termina con A")



# list1 = ["Diego", "Adolfo", "Mayte"]
# list2 = ["Robles", "Hinako", "Silva"]


# no=input("Agregue un nombre: ")
# ape=input("Agregue un apellido: ")


# list1.append(no)
# list2.append(ape)

# for f in range(len(list1)):
#     print(list1[f], list2[f])

toys = ["yo-yo", "tetris"]

def add():
    nameT = input("Ingrese el nombre del juguete: ")
    toys.append(nameT)
    print(f"Se ha añadido el juguete: {nameT}")
    print("-"*30)

def upd():
    show()
    upd = int(input("¿Que juguete desea actualizar: "))
    newT = input("Ingrese el nuevo juguete: ")
    toys[upd-1]=newT
    print("-"*30)

def delete():
    show()
    delete = int(input("¿Que juguete desea eliminar?: "))
    toys.pop(delete-1)
    print("Juguete Eliminado.")

def show():
    count = 1
    for t in toys:
        print(count,".-",t)
        count+=1
    print("-"*30)

def menuT():
    while True:
            try:
                op=0
                print("1.- Agregar Juguete")
                print("2.- Eliminar Juguete")
                print("3.- Actualizar Juguete")
                print("4.- Mostrar Juguete")
                print("5.- Salir")
                op=int(input("Ingrese una opción: "))
                match op:
                    case 1:
                        add()
                    case 2:
                        delete()
                    case 3:
                        show()
                        upd()
                    case 4:
                        show()
                    case 5:
                        print("Saliendo...")
                        break
                    case _:
                        print("Opción Inválida")
            except Exception as e:
                print("Error,", e)

listN = []
pares = []
impares = []

num = input("Ingrese números enteros separados por espacio: ")
listnum = num.split()

for p in listnum:
    listN.append(int(p))

for n in listN:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Los números pares son: {pares}")
print(f"Los números impares son: {impares}")
