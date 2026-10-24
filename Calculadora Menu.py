import Operaciones

def menu():
    while True:
        print("Calculadora Menu")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = Operaciones.suma(a, b)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = Operaciones.resta(a, b)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = Operaciones.multiplicación(a, b)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = Operaciones.división(a, b)
            print(f"El resultado de la división es: {resultado}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
