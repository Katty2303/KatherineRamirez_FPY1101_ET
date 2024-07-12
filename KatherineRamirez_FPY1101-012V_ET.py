import os
import time
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldosTrabajadores = {}

def limpiarPantalla():
    os.system("cls")

def tiempo():
    time.sleep(2)

def menu():
    print("*"*10, "MENÚ", "*"*10)
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def asignar():
    limpiarPantalla()
    print("*"*10, "ASIGNACIÓN DE SUELDOS", "*"*10)
    for i in trabajadores:
        sueldosAleatorios = random.randint(300000,2500000)   
        print(f"\nNombre empleado {i}, sueldo ${sueldosAleatorios}")
        sueldosTrabajadores[i] = sueldosAleatorios

def clasificar():
    limpiarPantalla()
    contTrabajador = 0
    print("*"*10, "CLASIFICACIÓN DE SUELDOS", "*"*10)
    print(f"\nSueldos menores a $800.000 TOTAL: ")
    for minSueldo in sueldosTrabajadores.values():
        for minNombre in sueldosTrabajadores.keys():
            if minSueldo < 800000:
                print("\nNombre empleado     Sueldo")
                print(minNombre," "*4,minSueldo)

    print(f"\nSueldos entre $800.000 y $2.000.000: ")
    for entreSueldo in sueldosTrabajadores.values():
        for entreNombre in sueldosTrabajadores.keys():
            if entreSueldo > 800000 and entreSueldo < 2000000:
                print("\nNombre empleado     Sueldo")
                print(entreNombre," "*4,entreSueldo)

    print(f"\nSueldos superiores a $2.000.000 TOTAL: ")
    for sobreSueldo in sueldosTrabajadores.values():
        for sobreNombre in sueldosTrabajadores.keys():
            if sobreSueldo >  2000000:
                print("\nNombre empleado     Sueldo")
                print(sobreNombre," "*4,sobreSueldo)

    print(f"\nTOTAL SUELDOS: $")

def estadisticas():
    limpiarPantalla()
    print("*"*10, "ESTADÍSTICAS", "*"*10)

def reporte():
    limpiarPantalla()
    print("*"*10, "REPORTE DE SUELDOS", "*"*10)

def salir():
    limpiarPantalla()
    print("Desarrollado por Katherine Ramírez")
    print("RUT 16.244.560-k")
    print("Finalizando programa...")

def opMenu():
    try:
        opciones = True
        while opciones == True:
            limpiarPantalla()
            menu()
            opElegida = int(input("Ingrese una opción del menú: "))
            if opElegida == 1:
                asignar()
            elif opElegida == 2:
                clasificar()
            elif opElegida == 3:
                estadisticas()
            elif opElegida == 4:
                salir()
            else:
                print("La opción elegida no es correcta")
                tiempo()
            input("Escriba Enter para continuar...")
            tiempo()
    except ValueError:
        print("El valor ingresado no es correcto")

opMenu()


