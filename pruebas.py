import calculadora_indices

print("PRUEBAS\n")

hombre_IMC, mujer_IMC = calculadora_indices.calcular_IMC(81, 1.75), calculadora_indices.calcular_IMC(58, 1.69)

print("Cálculos IMC")
print(hombre_IMC)
print(mujer_IMC)

print("")


valor_hombre_10_8 = 1
valor_mujer_0 = 2
hombre_PG, mujer_PG = calculadora_indices.calcular_porcentaje_grasa(81, 1.75, 20, valor_hombre_10_8), calculadora_indices.calcular_porcentaje_grasa(58, 1.69, 21, valor_mujer_0)

print("Cálculos porcentaje grasa")
print(f"{hombre_PG}%")
print(f"{mujer_PG}%")

print("")

valor_hombre_5 = 1
valor_mujer_menos_161 = 2
hombre_CR, mujer_CR = calculadora_indices.calcular_calorias_en_reposo(81, 175, 20, valor_hombre_5), calculadora_indices.calcular_calorias_en_reposo(58, 169, 21, valor_mujer_menos_161)

print("Cálculos calorias en reposo")
print(f"{hombre_CR} cal")
print(f"{mujer_CR} cal")

print("")

valor_hombre_5 = 1
valor_mujer_menos_161 = 2
valor_ejercicio_moderado_1_55 = 3
valor_deportista_1_725 = 4

hombre_CA= calculadora_indices.calcular_calorias_en_actividad(81, 175, 20, valor_hombre_5, valor_ejercicio_moderado_1_55) 
mujer_CA = calculadora_indices.calcular_calorias_en_actividad(58, 169, 21, valor_mujer_menos_161, valor_deportista_1_725)

print("Cálculos calorias en actividad")
print(f"{hombre_CA} cal")
print(f"{mujer_CA} cal")

print("")

valor_hombre_5 = 1
valor_mujer_menos_161 = 2

hombre_AD = calculadora_indices.consumo_calorias_recomendado_para_adelgazar(81, 175, 20, valor_hombre_5)
mujer_AD = calculadora_indices.consumo_calorias_recomendado_para_adelgazar(58, 169, 21, valor_mujer_menos_161)

print("Cálculos calorias adelgazar")
print(hombre_AD)
print(mujer_AD)

print("")
