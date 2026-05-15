# total_ingresos = 0
# while True:
#     try:
#         pa = int(input("¿Cuántos pasajes desea veder?: "))
#         break
#     except Exception as e:
#         print(f"¡Error! {e}")
# for i in range(pa):
#     while True:
#         try:
#             n = int(input(f"Ingrese el precio que desee vender el pasaje {i+1}: "))
#             total_ingresos +=n
#             break
#         except ValueError as e:
#             print(f"¡Error! Solo números enteros {e}")
# print(f"El total de ingresos de la venta de pasajes fue de {total_ingresos}!")

'''



'''

# while True:
#     try:
#         pa = int(input("¿Cuántos bultos son?: "))
#         break
#     except Exception as e:
#         print(f"¡Error! {e}")
# bliviano=0
# bnormales=0
# for i in range(pa):
#     while True:
#         try:
#             n = float(input(f"Ingrese el peso bulto {i+1} (En kg): "))
#             if n <= 5:
#                 bliviano +=1
#             else:
#                 bnormales +=1
#             break
#         except ValueError as e:
#             print(f"¡Error! Solo números enteros {e}")

# print(f"Bultos Livianos: {bliviano * 1000}")
# print(f"Bultos Normales: {bnormales * 2000}")
# print(f"El total es: {bliviano * 1000 + bnormales * 2000}") 


# # Pedir la cantidad de notas al usuario 
# # luego pedir cada nota individualmente
# # calcular el promedio de todas las notas
# # mostrar si aprueba o no

while True:
        try:
            notas=int(input("Ingrese la cant de notas: "))
            break
        except Exception as e:
             print(f"¡Error! {e}")
suma=0
for i in range(notas):
    while True:
        try:
            n=float(input(f"Ingrese la nota {i+1}: "))
            suma=suma+n
            break
        except ValueError as e:
             print(f"¡Error! Solo números decimales {e}")
prom=suma/notas
print("El promedio es",round(prom,1) )

if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")
