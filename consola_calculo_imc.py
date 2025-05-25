from calculadora_indices import calcular_IMC

def categoria_imc(imc):
    if imc < 16:
        return "delgadez severa"
    elif imc < 17:
        return "delgadez moderada"
    elif imc < 18.5:
        return "delgadez aceptable"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    elif imc < 35:
        return "obesidad tipo 1"
    elif imc < 40:
        return "obesidad tipo 2"
    elif imc < 50:
        return "obesidad tipo 3 o mórbida"
    else:
        return "obesidad tipo 4 o extrema"

try:
    peso = float(input("Ingresa tu peso (En KGs): "))
    altura = float(input("Ingresa tu altura (En metros): "))
    imc = calcular_IMC(peso, altura)
    
    if imc:
        categoria = categoria_imc(imc)
        print(f"Tu indice de masa corporal es de: {imc}. Tu categoría es: {categoria}")
except ValueError:
    print("Tanto el peso como la altura deben ser numeros.")


