# notas=[4.5,7.0,3.4,6.6,3.8]

# para sacar promedio se suma y se divide por la cantidad de nota

# def calculaProm(nota):
#     total = 0
#     for n in nota:
#         total+=n
#     prom=total/len(n)
#     return round(prom,1)
# print("El promedio es ",calculaProm(notas))

# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
#  
'''
1.- ingresar Pelucula
2.- quitar Pelucula
3.- ingresar Pelucula
4.- Mostar Peluculas
5.- Mostrar solo los titulos
6.- Salir
'''

peliculas = [
    {"titulo": "Inception", "Director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "año": 2010},
    {"titulo": "Gonjiam", "Director": "Beom-sik Jeong",
     "genero": "Thriller", "año": 2018},
    {"titulo": "Spiderman", "Director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "año": 2010},
]

def agregarPeli():
    nombrePel = input("Ingrese el nombre de la pelicula: ")
    if len(nombrePel) > 2:
        