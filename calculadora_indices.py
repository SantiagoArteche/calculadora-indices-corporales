def calcular_IMC(peso, altura):
    if not validar_info(peso, altura, False, False, False):
        return False

    masa_corporal = peso / (altura ** 2) 
    return masa_corporal
    
def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    if not validar_info("calcular_porcentaje_grasa"):
        return
    
    imc = calcular_IMC(peso, altura)
    valor_genero_conseguido = conseguir_valor_genero(valor_genero, "calcular_porcentaje_grasa")

    grasa_corporal = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero_conseguido
    return grasa_corporal

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    if not validar_info("calcular_calorias_en_reposo"):
        return
    
    return conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    if not validar_info("calcular_calorias_en_reposo"):
        return
    
    tasa_metabolica_basal = conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)
    valor_actividad_conseguido = conseguir_valor_actividad(valor_actividad)
    return tasa_metabolica_basal * valor_actividad_conseguido

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tasa_metabolica_basal = conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)
    rango_inferior = tasa_metabolica_basal * 0.80
    rango_superior = tasa_metabolica_basal * 0.85

    respuesta = f"Para adelgazar es recomendado que consumas entre: {rango_inferior} y {rango_superior} calorías al día"
    return respuesta
    
def conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero):
    valor_genero_conseguido = conseguir_valor_genero(valor_genero, "tasa_metabolica_basal")
    tasa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero_conseguido

    return tasa_metabolica_basal

def conseguir_valor_actividad(valor_actividad):
    if valor_actividad == 1:
        return 1.2
    elif valor_actividad == 2:
        return 1.375
    elif valor_actividad == 3:
        return 1.55
    elif valor_actividad == 4:
        return 1.72
    else:
        return 1.9
    
def conseguir_valor_genero(input_valor_genero, tipo_calculo):
    if tipo_calculo == "calcular_porcentaje_grasa":
        if(input_valor_genero == 1):
            valor_genero = 10.8
        else:
            valor_genero = 0
    else:
        if(input_valor_genero == 1):
            valor_genero = 5
        else:
            valor_genero = -161
            
    return valor_genero
        

def validar_info(peso, altura, edad, valor_genero, valor_actividad):
    if not isinstance(peso, float) or peso <= 0:
        print("El peso debe ser un número mayor a 0")
        return False
    elif not isinstance(altura, float) or altura <= 0:
        print("La altura debe ser un número mayor a 0")
        return False
    elif edad and (not isinstance(edad, int) or edad <= 0):
        print("La edad debe ser un número mayor a 0")
        return False
    elif valor_genero and (not isinstance(valor_genero, int) or ((valor_genero <= 0) or (valor_genero > 2))):
        print("Debe ingresar 1 en caso de que seas HOMBRE o 2 en caso de que seas MUJER")
        return False
    elif valor_actividad and (not isinstance(valor_actividad, int) or ((valor_actividad <= 0) or (valor_actividad > 5))):
        print("Ingreso incorrecto, elige entre las actividades disponibles ingresando un valor numererico del 1 al 5")
        return False
    
    return True