'''
PROYECTO: Clasificación y Control de Calidad - Embotelladora de Jugos

1. Captura de datos y validación:
- Solicitar volumen de líquido (ml).
- Validar rango: entre 400 y 600 ml. (Bucle hasta que sea correcto).

2. Control de precisión (Uso de Valor Absoluto):
- Volumen ideal: 500 ml.
- Diferencia absoluta = abs(ideal - real).
- Clasificación: 
    Diferencia > 15 ml: "Margen Alto".
    Diferencia <= 15 ml: "Precisión Estándar".

3. Selección de tipo de producto:
- Opción 1: Concentrado (Etiqueta: "Néctar").
- Opción 2: Diluido (Etiqueta: "Refresco").
- Validar que solo se elija 1 o 2.

4. Costo de logística por destino:
- Opción 1: Envío Local ($10).
- Opción 2: Envío Nacional ($25).
- Validar que solo se elija 1 o 2.

5. Resultado final:
- Mostrar en una sola línea: Producto, Precisión y Costo de envío.
'''
import random as rnd
import time
vol_liquid = rnd.randint(200, 1000)
vol_real = 500
while vol_liquid < 400 or vol_liquid > 600:
    print("Error, Fuera de rango")
    vol_liquid = rnd.randint(200, 1000)
    time.sleep(1)
else:
    dif = abs(vol_real - vol_liquid)
    if dif > 15:
        clas = "Margen Alto"
    else:
        clas = "Precisión Estándar"

prod = int(input("Que producto desea? 1.- Néctar 2.- Refresco: "))
while prod != 1 and prod != 2:
    print("Fuera de rango")
    prod = int(input("Que producto desea? 1.- Néctar 2.- Refresco: "))
else:
    if prod == 1:
        sticker = "Néctar"
    else:
        sticker = "Refresco"

dest = int(input("Cual sería el tipo de envio? 1.- Envío Local 2.- Envío Nacional: "))
while dest != 1 and dest != 2:
    print("Fuera de rango")
    dest = int(input("Cual sería el tipo de envio? 1.- Envío Local 2.- Envío Nacional: "))
else:
    if dest == 1:
        destino = "Envío local"
        costo = 10
    else:
        destino = "Envío Nacional"
        costo = 25
print(f"{sticker} {clas} {destino} {costo}$")