pacientes=[
    {"nombre": "Chao Yaegar",    "prevision": "Isapre",  "temperatura": 36.6,  "grave": False},
    {"nombre": "Hola Yaegar",    "prevision": "Isapre",  "temperatura": 36.6,  "grave": False},
    {"nombre": "Eren Yaegar",    "prevision": "Fodesa",  "temperatura": 36.6,  "grave": False},
]
def validaTemp(t):
    if t > 39:
        return True
    else:
        return False

def addPaciente():
    try:
        add = input("Ingrese el nombre del paciente nuevo: ")
        while add == "" or len(add) < 8:
            print("El nombre no puede estar vacío ni tener menos de 8 caracteres.")
            print("-"*30)
            add = input("Ingrese el nombre del paciente nuevo: ")   
        addPre = input("Ingrese la prevision del paciente nuevo (Fonasa, isapre o fodesa): ")
        while addPre.lower() not in ("fonasa", "isapre", "fodesa"):
            print("Prevision invalida, ingrese una de estas -> (Fonasa, isapre o fodesa)")
            addPre = input("Ingrese la prevision del paciente nuevo (Fonasa, isapre o fodesa): ")
        addTemp = float(input("Ingrese la temperatura del paciente nuevo: "))
        pacientes.append({"nombre": add,    "prevision": addPre,  "temperatura": addTemp,  "grave": validaTemp(addTemp)})
    except Exception as e:
        print("Error" ,e)

def showPaciente():
    c = 1
    for paciente in pacientes:
        print(f"{c}.- {paciente}")
        c+=1
    print("-"*30)

def cobrarPaciente():
    showPaciente()
    cobrar=int(input("¿A que paciente le va a cobrar?: "))
    if -1<cobrar<len(pacientes):
        print("Paciente no encontrado.")
    atencion = 25000
    if pacientes[cobrar-1]["prevision"] == "fonasa":
        total = atencion*0.46 
    elif pacientes[cobrar-1]["prevision"] == "isapre":
        total = atencion*0.73 
    elif pacientes[cobrar-1]["prevision"] == "fodesa":
        total = atencion*0.875
    else:
        print("Prevision inválida")

def eliminarPaciente():
    remove=int(input("Que paciente se va?: "))
    pacientes.pop(remove-1)

while True:
    try:
        print("1.- Agregar paciente")
        print("2.- Quitar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobrar a paciente")
        print("5.- Mostrar Pacientes")
        print("9.- Salir")
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                addPaciente() 
            case 2:
                showPaciente()
                eliminarPaciente()
            case 3:
                showPaciente()
                p=int(input("A que paciente le tomará la temperatura?: "))
                t=float
            case 4:
                showPaciente()
                 
            case 5:
                showPaciente()
            case 9:
                print("Saliendo")
                break 
            case _:
                print() 
    except Exception as e:
        print("Error" ,e)

