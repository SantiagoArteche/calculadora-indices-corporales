from calculadora_indices import calcular_porcentaje_grasa

def porcentaje_de_grasa_recomendado(edad, valor_genero):
    if edad > 19:
        if valor_genero == 1:
            return "11% - 20%"
        else:
            return "16% - 28%"
    elif edad > 29:
        if valor_genero == 1:
            return "12% - 21%"
        else:
            return "17% - 29%"
    elif edad > 39:
        if valor_genero == 1:
            return "14% - 23%"
        else:
            return "18% - 30%"
    elif edad > 49:
        if valor_genero == 1:
            return "15% - 24%"
        else:
            return "19% - 31%"

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En metros): "))
    edad = int(input("Ingresa tu edad: "))
    genero = int(input("Seleccioná tu género: 1 para masculino, 2 para femenino: "))
    porcentaje_grasa = calcular_porcentaje_grasa(peso, altura, edad, genero)
    
    if porcentaje_grasa:
        print(f"Tu porcentaje de grasa corporal es de: {porcentaje_grasa}%")
        if edad >= 20 and edad <= 59:
            porcentaje_recomendado = porcentaje_de_grasa_recomendado(edad, genero)
            print(f"Tu porcentaje de grasa corporal recomendado esta entre: {porcentaje_recomendado}")
except ValueError as error:
    print(error)
    print("El tipo de información que estas ingresando es incorrecto, asegurate de rellenar los valores con números.")
