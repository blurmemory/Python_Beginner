juegosDicc={
   1:{"nombreJuego": "God of war", "genero": "hack-and-slash"},
   2:{"nombreJuego": "Stellar Blade", "genero": "hack-and-slash"},
   3:{"nombreJuego": "Heavy Rain", "genero": "drama interactivo"}
}
def agregarJuego():
   print("Cual es el nombre del videojuego?")
   nombre = input()
   print("Cual es el genero del videojuego?")
   genero = (input())
   nuevoKey=list(juegosDicc.keys())
   nuevoKey.sort()
   juegosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "genero": genero}


def MostrarJuegos():
   for key, juego in juegosDicc.items():
      print(f"{key} .-{juego}")


def eliminarProducto():
    MostrarJuegos()
    borrar=int(input("Cual Producto borrará?: "))
    if borrar in juegosDicc.keys():
        del juegosDicc[borrar]
    else:
       print("Producto no existe")


def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))
   if num in productosDicc.keys():
      nombre=input("Cual es el nombre nuevo?: ")
      precio=int(input("Cual es el precio nuevo?: "))
      productosDicc[num]={"nombre": nombre, "precio": precio}
   else:
      print("Producto no existe")
   nombre=input("Cual es el nombre nuevo?: ")
   precio=int(input("Cual es el precio nuevo?: "))
   productosDicc[num]={"nombre": nombre, "precio": precio}



def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear boleta y Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                  comprar()                 
               case 6:
                  crearBoleta()
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)
vegetalesMenuDiccionario()