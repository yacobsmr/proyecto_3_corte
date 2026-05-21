# CALCULADORA CIENTÍFICA GRAFICADORA

## ¿Qué es este programa?

Es una calculadora que funciona como un programa. Haces clic en las opciones del menú y escribes números para calcular cosas.

## Integrantes

- Yacobs Santiago Muñoz Rubio
- Carlos Andres Orjuela Tique

## Qué necesitas para ejecutarlo

- Python 3.6 o superior
- Nada más (no hay que instalar nada adicional)

## Cómo Ejecutar el Programa

### En Windows:
1. Abre la terminal (cmd o PowerShell)
2. Escribe: `python programa_1.py`
3. Presiona Enter

### En Linux/Mac:
```
python3 programa_1.py
```

## Qué puede hacer este programa

Tiene 6 opciones principales en el menú.

### Opción 1: Operaciones Básicas

Son cálculos simples que todos conocen. El programa te pide dos números.

- **Suma**: Sumar dos números (5 + 3 = 8)
- **Resta**: Restar dos números (10 - 4 = 6)
- **Multiplicación**: Multiplicar dos números (3 × 4 = 12)
- **División**: Dividir dos números (12 ÷ 3 = 4). Si intentas dividir por cero, el programa te avisa y no te deja.
- **Potencia**: Elevar un número a una potencia (2^3 = 8, que significa 2 × 2 × 2)

### Opción 2: Operaciones Científicas

Son operaciones más complejas. El programa usa fórmulas matemáticas especiales para calcularlas.

#### Factorial
Es multiplicar un número por todos los números menores hasta 1.
- Ejemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6
- El programa calcula esto multiplicando números de uno en uno

#### Raíz Cuadrada
Es el número que multiplicado por sí mismo da el número original.
- √9 = 3 (porque 3 × 3 = 9)
- √16 = 4 (porque 4 × 4 = 16)
- √2 = 1.414... (no es exacto)
- El programa mejora la aproximación 10 veces hasta que es muy precisa

#### Exponencial (e^x)
Es la constante e (2.71828...) elevada a una potencia x.
- e^0 = 1
- e^1 = 2.71828...
- e^2 = 7.389...
- El programa suma muchos términos pequeños para calcularlo

#### Seno
Es un valor que depende de un ángulo. El ángulo se da en radianes.
- sin(0) = 0
- sin(90 grados) = 1 (en radianes: 1.57)
- sin(180 grados) = 0 (en radianes: 3.14)
- El programa suma términos matemáticos para calcularlo

#### Coseno
Es similar al seno pero comienza en 1 en lugar de 0.
- cos(0) = 1
- cos(90 grados) = 0 (en radianes: 1.57)
- cos(180 grados) = -1 (en radianes: 3.14)

#### Logaritmo Natural
Es preguntar: "¿A qué potencia debo elevar e para obtener este número?"
- ln(1) = 0 (porque e^0 = 1)
- ln(e) = 1 (porque e^1 = e)
- ln(10) = 2.30... (porque e^2.30 = 10)

### Opción 3: Evaluar una Función

El programa tiene 3 funciones programadas:

1. **Función Lineal**: f(x) = 2x + 1
   - Si x = 0, resultado = 1
   - Si x = 5, resultado = 11
   - Si x = 10, resultado = 21

2. **Función Cuadrática**: f(x) = x²
   - Si x = 2, resultado = 4
   - Si x = 3, resultado = 9
   - Si x = 5, resultado = 25

3. **Función Cúbica**: f(x) = x³
   - Si x = 2, resultado = 8
   - Si x = 3, resultado = 27
   - Si x = 4, resultado = 64

### Opción 4: Graficar una Función en Consola

El programa dibuja la función usando caracteres * (asteriscos).

Ejemplo de una función lineal:
```
        *
       *
      *
     *
    *
   *
  *
 *
*
```

Cada * es un punto. Los puntos unidos forman la imagen de la función.

### Opción 5: Ver Historial

El programa guarda todas las operaciones que has hecho. Esta opción muestra la lista.

Ejemplo:
```
1. Suma: 5 + 3 = 8
2. Potencia: 2 ^ 3 = 8
3. Raíz cuadrada: √16 = 4.0
4. Función lineal: f(5) = 11
```

### Opción 6: Salir

Termina el programa.

## Conversiones: Grados a Radianes

Las funciones seno y coseno usan radianes, no grados.

- 180 grados = 3.14159 radianes
- 90 grados = 1.5708 radianes
- 45 grados = 0.7854 radianes
- 360 grados = 6.2832 radianes

Fórmula: **Radianes = Grados × 3.14159 / 180**

Ejemplo: 90 grados en radianes = 90 × 3.14159 / 180 = 1.5708

## Cómo funciona el programa

### Variable Historial

El programa tiene una lista llamada `historial` que es como una bolsa.

Cada vez que haces un cálculo, el programa pone ese cálculo en la bolsa.

```
historial = []
Después de hacer 5 + 3 = 8
historial = ["Suma: 5 + 3 = 8"]
```

### Funciones

El programa tiene funciones. Una función es un trozo de código que hace algo específico.

**Ejemplos**:
- `sumar(5, 3)` → devuelve 8
- `restar(10, 4)` → devuelve 6
- `potencia(2, 3)` → devuelve 8

### Ciclos (For y While)

Los ciclos repiten una acción varias veces.

**Ejemplo de ciclo for**:
```
Para calcular factorial de 5, el programa hace:
resultado = 1 × 1 = 1
resultado = 1 × 2 = 2
resultado = 2 × 3 = 6
resultado = 6 × 4 = 24
resultado = 24 × 5 = 120
```

**Ejemplo de ciclo while**:
El menú del programa es un ciclo while. Sigue mostrando opciones hasta que selecciones "Salir".

### Menúes

El programa tiene menúes con opciones numeradas.

El menú principal:
```
1. Operaciones básicas
2. Operaciones científicas
3. Evaluar función
4. Graficar función
5. Ver historial
6. Salir
```

Cuando selecciones 1, vas a otro menú. Cuando selecciones 6, se termina todo.

## Métodos para los cálculos

### Potencia
Multiplica el número por sí mismo varias veces:
- 2^3 = 2 × 2 × 2 = 8
- 5^2 = 5 × 5 = 25

### Raíz Cuadrada
El programa mejora una aproximación 10 veces:
- Intento 1: aproximación inicial
- Intento 2: mejor aproximación
- Intento 3: aún mejor
- ...
- Intento 10: muy precisa

Ejemplo para √16:
- Intento 1: 8
- Intento 2: 5
- Intento 3: 4.1
- Intento 4: 4.0 ← Ya está precisa

### Seno, Coseno, Exponencial, Logaritmo
El programa suma muchos términos pequeños. Más términos = más preciso.

Ejemplo simplificado:
```
e^1 = 1 + 1 + 0.5 + 0.166 + 0.041 + ... (20 términos)
e^1 ≈ 2.71828
```

## Precisión

Qué tan exactos son los resultados:

- Raíz cuadrada: 6 decimales correctos
- Exponencial: 10 decimales correctos
- Seno/Coseno: 8 decimales correctos
- Logaritmo: 8 decimales correctos

Por ejemplo, √2 da: 1.41421356 (8 decimales correctos)

## Validaciones

El programa verifica cosas:

- ❌ No te deja dividir por 0
- ❌ No te deja raíz de números negativos
- ❌ No te deja logaritmo de números ≤ 0
- ❌ No te deja factorial de números negativos

Si intentas hacer algo inválido, el programa te muestra un mensaje de error.

## Estructura del Código

El archivo `programa_1.py` tiene este orden:

1. **Variable historial** - Define la bolsa para guardar operaciones
2. **Operaciones básicas** - Funciones: sumar, restar, multiplicar, dividir, potencia
3. **Operaciones científicas** - Funciones: factorial, raíz, exponencial, seno, coseno, logaritmo
4. **Funciones predefinidas** - Las 3 funciones (lineal, cuadrática, cúbica)
5. **Graficación** - Función que dibuja las gráficas
6. **Historial** - Función que muestra lo guardado
7. **Menúes** - Funciones de cada menú
8. **Función principal** - Función main que inicia todo
9. **Línea de inicio** - Código que ejecuta main

Cada línea tiene comentarios que explican qué hace.

## Preguntas Frecuentes

**P: ¿Por qué el resultado tiene tantos decimales?**
A: Porque el programa es muy preciso. Si solo necesitas 2 decimales, ignora los demás.

**P: ¿Por qué usa radianes y no grados?**
A: Radianes es lo estándar en matemática. Puedes convertir: Radianes = Grados × 3.14159 / 180

**P: ¿Por qué no usa la librería math?**
A: El proyecto pide implementar todo manualmente para aprender cómo funcionan los algoritmos.

**P: ¿Por qué dibuja con caracteres y no usa matplotlib?**
A: Para no depender de librerías externas. Todo debe funcionar con solo Python.

**P: ¿Se guardan los datos al cerrar?**
A: No. El historial solo existe mientras el programa está abierto. Se pierde al cerrar.

---

**¡Ya puedes usar la Calculadora!**

Ejecuta: `python programa_1.py`