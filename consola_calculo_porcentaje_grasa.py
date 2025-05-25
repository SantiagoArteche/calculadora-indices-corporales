from calculadora_indices import calcular_porcentaje_grasa

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En metros): "))
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Seleccioná tu género: 1 para masculino, 2 para femenino: "))
    porcentaje_grasa = calcular_porcentaje_grasa(peso, altura, edad, genero)
    
    if porcentaje_grasa:
        print(f"Tu porcentaje de grasa corporal es de: {porcentaje_grasa}%")
except ValueError as error:
    print(error)
    print("Error en el ingreso de información.")
