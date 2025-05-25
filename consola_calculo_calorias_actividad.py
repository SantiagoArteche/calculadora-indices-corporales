from calculadora_indices import calcular_calorias_en_actividad

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En centímetros): "))
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Seleccioná tu género: 1 para masculino, 2 para femenino: "))
    actividad = int(input("Seleccioná tu frecuencia de actividad: " \
    "1 poco o ningún ejercicio\n" \
    "2 ejercicio ligero (1 a 3 días a la semana)\n" \
    "3 ejercicio moderado (3 a 5 días a la semana)\n" \
    "4 ejercicio moderado (6 - 7 días a la semana)\n" \
    "5 atleta (entrenamientos mañana y tarde): "))
    calculo_calorias_en_actividad = calcular_calorias_en_actividad(peso, altura, edad, genero, actividad)
    
    if calculo_calorias_en_actividad:
        print(f"La cantidad de calorías que quemas por día con tu frecuencia de actividad es de: {calculo_calorias_en_actividad} calorías")
except ValueError as error:
    print(error)
    print("El tipo de información que estas ingresando es incorrecto, asegurate de rellenar los valores con números.")
