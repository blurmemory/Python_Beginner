pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]



# def colorEspe(lista, color):
#     for i in lista:
#         if color == i["color"]:
#             return "Disponible"
#     return "No existe"        



# print(colorEspe(pinturas, "verde"))

def mostrarPinturas(lista):
    if len(lista)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in lista:
            print(f"{c}.- {p}")
            c+=1

# mostrarPinturas(pinturas)

def quitarPintura(lista, color):
    for p in lista:
        if color == p["color"]:
            lista.remove(j)

quitarPintura()