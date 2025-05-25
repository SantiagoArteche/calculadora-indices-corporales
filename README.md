# 📱 Calculadora de Índices Corporales

## 🎯 Objetivo General

El objetivo general de este proyecto es crear una aplicación que permita realizar cálculos de distintos **índices corporales**, como el **Índice de Masa Corporal (IMC)** y la **Tasa Metabólica Basal (TMB)**, proporcionando información útil para conocer el estado de salud de una persona.

## ✅ Objetivos Específicos

1. Crear funciones para realizar los cálculos necesarios.
2. Llamar funciones utilizando parámetros.
3. Componer funciones (llamar funciones desde otras funciones).
4. Crear y utilizar un módulo (conjunto de funciones).
5. Probar las funciones del módulo.
6. Construir interfaces de usuario para la interacción con la aplicación.

---

## 📝 Descripción de la Aplicación

Esta aplicación calcula diversos índices corporales que permiten conocer el estado de salud de una persona. Algunos de estos indicadores ayudan a determinar si hay sobrepeso, obesidad o consumo calórico inadecuado.

---

## ⚙️ Índices Corporales Calculados

### 📏 Índice de Masa Corporal (IMC)

El **IMC** estima si el peso de una persona es adecuado en relación con su altura.

**Fórmula:**

IMC = peso (kg) / altura² (m²)

**Clasificación según IMC:**

| IMC          | Categoría                   |
| ------------ | --------------------------- |
| < 16         | Delgadez severa             |
| 16 – 16.99   | Delgadez moderada           |
| 17 – 18.49   | Delgadez aceptable          |
| 18.5 – 24.99 | Peso normal                 |
| 25 – 29.99   | Sobrepeso                   |
| 30 – 34.99   | Obesidad tipo I             |
| 35 – 39.99   | Obesidad tipo II            |
| 40 – 49.99   | Obesidad tipo III o mórbida |
| > 50         | Obesidad tipo IV o extrema  |

---

### 💪 Porcentaje de Grasa Corporal (%GC)

Este porcentaje estima si el nivel de grasa en el cuerpo es adecuado.

**Fórmula:**

%GC = 1.2 _ IMC + 0.23 _ edad (años) - 5.4 - valor_género

**valor_género:**

- Masculino: 10.8
- Femenino: 0

**Rangos recomendados según edad y género:**

| Edad  | Hombres   | Mujeres   |
| ----- | --------- | --------- |
| 20–29 | 11% – 20% | 16% – 28% |
| 30–39 | 12% – 21% | 17% – 29% |
| 40–49 | 14% – 23% | 18% – 30% |
| 50–59 | 15% – 24% | 19% – 31% |

---

### 🔥 Tasa Metabólica Basal (TMB)

La **TMB** indica la cantidad mínima de calorías necesarias para mantener las funciones vitales del cuerpo en reposo.

**Fórmula:**

TMB = (10 _ peso) + (6.25 _ altura en cm) - (5 \* edad) + valor_género

**valor_género:**

- Masculino: 5
- Femenino: -161

---

### 🏃‍♂️ TMB Ajustada por Actividad Física

Se calcula multiplicando la TMB por un valor según el nivel de actividad física semanal:

| Actividad física                       | Valor |
| -------------------------------------- | ----- |
| Poco o ningún ejercicio                | 1.2   |
| Ejercicio ligero (1–3 días/semana)     | 1.375 |
| Ejercicio moderado (3–5 días/semana)   | 1.55  |
| Deportista (6–7 días/semana)           | 1.72  |
| Atleta (entrenamientos mañana y tarde) | 1.9   |

**Fórmula:**

TMB_ajustada = TMB \* valor_actividad

---

### 🥗 Calorías Diarias para Adelgazar

Para bajar de peso, se recomienda consumir entre un **15% y 20% menos** de las calorías indicadas por la TMB ajustada.

**Fórmulas:**

Calorías mínimas = TMB*ajustada * 0.80

Calorías máximas = TMB*ajustada * 0.85

##
> ⚠️ **Aviso**: Esta aplicación tiene fines educativos. Para una evaluación profesional, consulta con un especialista en salud o nutrición.
