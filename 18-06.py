pacientes=[
    {"nombre": "Chao Yaegar",    "prevision": "Isapre",  "temperatura": 36.6,  "grave": False},
    {"nombre": "Hola Yaegar",    "prevision": "Isapre",  "temperatura": 36.6,  "grave": False},
    {"nombre": "Eren Yaegar",    "prevision": "Fodesa",  "temperatura": 36.6,  "grave": False},
]
def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
def agregarPaciente():
    nombre=input("Ingrese nombre: ")
    prevision=input("Ingrese prevision: ")
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
                "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")
def eliminarPaciente():
    mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci-1)
    print("Paciente eliminado.")
def tomarTemp():
    mostrarPacientes()
    paciente=int(input("Qué paciente le tomará la temperatura?: "))
    temperatura=float(input("Ingrese la temperatura del paciente: "))
    pacientes[paciente-1]["temperatura"]=temperatura
    pacientes[paciente-1]["grave"]=validarEstado(temperatura)
    print("Temperatura y estado actualizado")
def cobrarAtencion():
    total=0
    mostrarPacientes()
    cobrar = int(input("¿A que paciente le va a cobrar?: "))
    prevision = pacientes[cobrar-1]["prevision"]

    if prevision.lower() == "fonasa":
        total = 25000 * 0.46
    if prevision.lower() == "isapre":
        total = 25000 * 0.73
    if prevision.lower() == "fodesa":
        total = 25000 * 0.875
    else:
        print("Prevision invalida")
    print(f"El total a pagar es: {total}")
    

def menuPacientes():
    while True:
        try:
            print("1.- Ingresar paciente")
            print("2.- Quitar paciente")
            print("3.- Tomar Temperatura")
            print("4.- Cobra atencion")
            print("5.- Mostrar Pacientes")
            print("9.- Salir")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    agregarPaciente()
                case 2:
                    eliminarPaciente()
                case 3:
                    tomarTemp()
                case 4:
                    cobrarAtencion()
                case 5:
                    mostrarPacientes()
                case 9:
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print("Error:" , e)

menuPacientes()