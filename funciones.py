# Sin Argumento y con retorno


# def sumaRet():
#     n1=int(input("Ingrese un número: "))
#     n2=int(input("Ingrese un otro número: "))
#     return n1+n2
# print(sumaRet())

# Con argumento y sin retorno

# def saludoME(name):
#     print("Hola", name)
# saludoME("James Bond")

# def halfPrice(precio):
#     print("El precio es:", precio/2)
# p=int(input("Ingrese el precio: "))
# halfPrice(40000)

# def sumaRetArg(n1,n2):
#     return n1+n2
# print("El resultado de la suma es:", sumaRetArg(9,16))

def sum(n1,n2):
    return n1+n2 
def res(n1,n2):
    return n1+n2 
def mul(n1,n2):
    return n1+n2 
def div(n1,n2):
    return n1+n2 

op = 0
while True:
    try:
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        op=int(input("Ingrese una opción: "))
        match op:
             case 1:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                resultado=sum(num1,num2)
             case 2:  
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                res(num1,num2)
             case 3:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                resultado=mul(num1,num2)  
             case 4:  
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                resultado=div(num1,num2)
             case 5:  
                print("Saliendo...")
                break
             case _:
                  print("Opción Inválida")
        print("El resultado es:", resultado)  
    except Exception as e:
            print("Error:", e)