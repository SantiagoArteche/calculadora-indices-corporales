from calculadora_indices import calcular_calorias_en_reposo

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En centímetros): "))
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Seleccioná tu género: 1 para masculino, 2 para femenino: "))
    calculo_calorias_en_reposo = calcular_calorias_en_reposo(peso, altura, edad, genero)
    
    if calculo_calorias_en_reposo:
        print(f"En reposo quemas un total de: {calculo_calorias_en_reposo} calorías")
except ValueError as error:
    print(error)
    print("El tipo de información que estas ingresando es incorrecto, asegurate de rellenar los valores con números.")
