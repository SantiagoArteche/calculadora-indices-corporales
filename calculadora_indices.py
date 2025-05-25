def calcular_IMC(peso, altura):
    if not validar_info(peso, altura, None, None, None):
        return False

    indice_masa_corporal = peso / (altura ** 2) 
    return round(indice_masa_corporal, 2)
    
def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    if not validar_info(peso, altura, edad, valor_genero, None):
        return
    
    imc = calcular_IMC(peso, altura)
    valor_genero_conseguido = conseguir_valor_genero(valor_genero, "calcular_porcentaje_grasa")

    grasa_corporal = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero_conseguido
    return round(grasa_corporal, 2)

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    if not validar_info(peso, altura, edad, valor_genero, None):
        return
    
    tasa_metabolica_basal = conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)
    return round(tasa_metabolica_basal, 2)

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    if not validar_info(peso, altura, edad, valor_genero, valor_actividad):
        return
    
    tasa_metabolica_basal = conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)
    valor_actividad_conseguido = conseguir_valor_actividad(valor_actividad)
    return round(tasa_metabolica_basal * valor_actividad_conseguido, 2)

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    if not validar_info(peso, altura, edad, valor_genero, None):
        return
    
    tasa_metabolica_basal = conseguir_tasa_metabolica_basal(peso, altura, edad, valor_genero)
    rango_inferior = round(tasa_metabolica_basal * 0.80, 2)
    rango_superior = round(tasa_metabolica_basal * 0.85, 2)

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
        return 1.725
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
    if peso <= 0:
        print("El peso debe ser un número mayor a 0")
        return False
    elif altura <= 0:
        print("La altura debe ser un número mayor a 0")
        return False
    elif (edad and edad < 0) or edad == 0:
        print("La edad debe ser un número mayor a 0")
        return False
    elif (valor_genero and ((valor_genero < 0) or (valor_genero > 2))) or valor_genero == 0:
        print("Debe ingresar 1 en caso de que sea HOMBRE o 2 en caso de que sea MUJER")
        return False
    elif (valor_actividad and ((valor_actividad < 0) or (valor_actividad > 5))) or valor_actividad == 0:
        print("Ingreso incorrecto, elige entre las actividades disponibles ingresando un valor numerico del 1 al 5")
        return False
    
    return True