from calculadora_indices import calcular_IMC

def categoria_imc(imc):
    if imc < 16:
        return "Delgadez Severa"
    elif imc < 17:
        return "Delgadez Moderada"
    elif imc < 18.5:
        return "Delgadez Aceptable"
    elif imc < 25:
        return "Peso Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad Tipo 1"
    elif imc < 40:
        return "Obesidad Tipo 2"
    elif imc < 50:
        return "Obesidad Tipo 3 o Mórbida"
    else:
        return "Obesidad Tipo 4 o Extrema"

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En metros): "))
    imc = calcular_IMC(peso, altura)
    
    if imc:
        categoria = categoria_imc(imc)
        print(f"Tu índice de masa corporal es de: {imc}\nTu categoría es: {categoria}")
except ValueError as error:
    print(error)
    print("El tipo de información que estas ingresando es incorrecto, asegurate de rellenar los valores con números.")


