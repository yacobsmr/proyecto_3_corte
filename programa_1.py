
# CALCULADORA CIENTÍFICA GRAFICADORA

# Este programa implementa una calculadora que realiza operaciones matemáticas
# básicas y científicas, evalúa funciones, grafica en consola y guarda historial
# DECLARACIÓN DE VARIABLE GLOBAL - HISTORIAL
# Esta lista almacena todas las operaciones realizadas durante la ejecución
# Se utiliza para que el usuario pueda ver el registro de lo que ha calculado
historial = []


# SECCIÓN 1: OPERACIONES BÁSICAS
# Estas funciones realizan operaciones matemáticas simples entre dos números

# Función para sumar dos números
# Parámetros: a (primer número), b (segundo número)
# Retorna: el resultado de la suma
def sumar(a, b):
    # Se suman los dos números usando el operador +
    # El operador + suma el valor de 'a' más el valor de 'b'
    resultado = a + b
    # Se retorna el resultado de la suma
    return resultado

# Función para restar dos números
# Parámetros: a (número principal), b (número a restar)
# Retorna: el resultado de la resta
def restar(a, b):
    # Se restan los dos números usando el operador -
    # El operador - resta del valor de 'a' el valor de 'b'
    resultado = a - b
    # Se retorna el resultado de la resta
    return resultado

# Función para multiplicar dos números
# Parámetros: a (primer número), b (segundo número)
# Retorna: el resultado de la multiplicación
def multiplicar(a, b):
    # Se multiplican los dos números usando el operador *
    # El operador * multiplica 'a' por 'b'
    resultado = a * b
    # Se retorna el resultado de la multiplicación
    return resultado

# Función para dividir dos números
# Parámetros: a (dividendo), b (divisor)
# Retorna: el resultado de la división
def dividir(a, b):
    # Se verifica si el divisor (b) es cero
    # Esto es importante porque la división entre cero no está definida
    if b == 0:
        # Si el divisor es cero, se retorna un mensaje de error
        # El usuario necesita saber que no se puede dividir por cero
        return "Error: No se puede dividir entre cero"
    # Si el divisor no es cero, se procede a dividir
    # El operador / divide 'a' entre 'b'
    resultado = a / b
    # Se retorna el resultado de la división
    return resultado

# Función para calcular la potencia
# Parámetros: base (número a elevar), exponente (a qué potencia elevar)
# Retorna: el resultado de la potencia
def potencia(base, exponente):
    # Se inicializa el resultado en 1
    # Este es el valor neutro para la multiplicación
    resultado = 1
    # Se utiliza un ciclo 'for' para multiplicar 'base' por sí misma 'exponente' veces
    # 'range(exponente)' genera números desde 0 hasta exponente-1
    for i in range(exponente):
        # En cada iteración se multiplica el resultado actual por la base
        # Primera iteración: resultado = 1 * base = base
        # Segunda iteración: resultado = base * base = base^2
        # Y así sucesivamente hasta completar 'exponente' veces
        resultado = resultado * base
    # Se retorna el resultado final de la potencia
    return resultado

# SECCIÓN 2: OPERACIONES CIENTÍFICAS

# Estas funciones calculan operaciones matemáticas complejas usando métodos
# de aproximación, sin usar librerías externas como 'math'

# Función para calcular el factorial de un número
# Parámetro: n (número del cual calcular el factorial)
# Retorna: el factorial de n (n!)
def factorial(n):
    # Se verifica si n es un número negativo
    # El factorial solo está definido para números no negativos
    if n < 0:
        # Si es negativo, se retorna un mensaje de error
        return "Error: El factorial no está definido para números negativos"
    # Se inicializa el resultado en 1
    # Este es el valor inicial para comenzar a multiplicar
    resultado = 1
    # Se utiliza un ciclo 'for' para multiplicar todos los números desde 1 hasta n
    # 'range(1, n + 1)' genera números del 1 al n (incluyendo n)
    for i in range(1, n + 1):
        # En cada iteración se multiplica el resultado por el número actual
        # Primera iteración: resultado = 1 * 1 = 1
        # Segunda iteración: resultado = 1 * 2 = 2
        # Tercera iteración: resultado = 2 * 3 = 6
        # Y así sucesivamente hasta n
        resultado = resultado * i
    # Se retorna el resultado final del factorial
    return resultado

# Función para calcular la raíz cuadrada usando método de aproximación
# Se utiliza el método de Newton-Raphson para aproximar la raíz cuadrada
# Parámetro: n (número del cual calcular la raíz cuadrada)
# Retorna: la raíz cuadrada aproximada de n
def raiz_cuadrada(n):
    # Se verifica si n es negativo
    # La raíz cuadrada de un número negativo no existe en números reales
    if n < 0:
        # Si es negativo, se retorna un mensaje de error
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    # Se verifica si n es cero
    # La raíz cuadrada de cero es cero
    if n == 0:
        # Se retorna 0 directamente
        return 0
    # Se inicializa la aproximación con el valor n dividido entre 2
    # Este es un punto de partida razonable para el método de Newton-Raphson
    aproximacion = n / 2.0
    # Se define el número de iteraciones que hará el algoritmo
    # Más iteraciones significan mayor precisión
    # 10 iteraciones es suficiente para obtener una aproximación muy cercana
    iteraciones = 10
    # Se ejecuta un ciclo que itera 'iteraciones' veces
    for i in range(iteraciones):
        # Se calcula la siguiente aproximación usando la fórmula de Newton-Raphson
        # Esta fórmula es: aproximacion_nueva = (aproximacion_antigua + n / aproximacion_antigua) / 2
        # Esta fórmula converge rápidamente al valor real de la raíz
        aproximacion = (aproximacion + n / aproximacion) / 2.0
    # Se retorna la aproximación final de la raíz cuadrada
    return aproximacion

# Función para calcular la exponencial (e^x) usando serie de Taylor
# La serie de Taylor es: e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
# Parámetro: x (el exponente)
# Retorna: la aproximación de e^x
def exponencial(x):
    # Se inicializa el resultado en 1
    # Este es el primer término de la serie de Taylor
    resultado = 1
    # Se inicializa el término actual en 1
    # El término es el componente individual de la serie
    termino = 1
    # Se define el número de términos de la serie a calcular
    # Más términos significan mayor precisión
    # 20 términos es suficiente para una aproximación muy precisa
    numeros_terminos = 20
    # Se ejecuta un ciclo para sumar cada término de la serie
    for i in range(1, numeros_terminos):
        # Se calcula el siguiente término
        # Cada término es el anterior multiplicado por x/i
        termino = termino * x / i
        # Se suma el nuevo término al resultado
        resultado = resultado + termino
    # Se retorna la aproximación de e^x
    return resultado

# Función para calcular el seno usando serie de Taylor
# La serie de Taylor para seno es: sen(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
# Parámetro: x (ángulo en radianes)
# Retorna: la aproximación de seno(x)
def seno(x):
    # Se normaliza el ángulo al rango de -π a π
    # π es aproximadamente 3.14159265359
    # Esto mejora la precisión de la aproximación
    # El operador % calcula el residuo de la división
    pi = 3.14159265359
    # Se reduce x al rango de -2π a 2π dividiendo entre 2π y tomando residuo
    x = x % (2 * pi)
    # Si x es mayor que π, se resta 2π para llevarlo al rango de -π a π
    if x > pi:
        # Se resta 2π al valor de x
        x = x - 2 * pi
    # Se inicializa el resultado en 0
    resultado = 0
    # Se inicializa el término actual en x
    # El primer término de la serie es x mismo
    termino = x
    # Se define el número de términos a calcular
    # Más términos dan mayor precisión
    numeros_terminos = 20
    # Se ejecuta un ciclo para sumar cada término de la serie
    for i in range(1, numeros_terminos):
        # Se suma el término actual al resultado
        resultado = resultado + termino
        # Se calcula el siguiente término
        # Cada término alterna de signo y se divide por (2i)*(2i+1)
        termino = termino * (-x * x) / ((2 * i) * (2 * i + 1))
    # Se retorna la aproximación del seno
    return resultado

# Función para calcular el coseno usando serie de Taylor
# La serie de Taylor para coseno es: cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
# Parámetro: x (ángulo en radianes)
# Retorna: la aproximación de coseno(x)
def coseno(x):
    # Se normaliza el ángulo al rango de -π a π
    # Esto es similar a lo que se hace en la función seno
    pi = 3.14159265359
    # Se reduce x al rango de -2π a 2π
    x = x % (2 * pi)
    # Si x es mayor que π, se resta 2π
    if x > pi:
        x = x - 2 * pi
    # Se inicializa el resultado en 1
    # El primer término de la serie de coseno es 1
    resultado = 1
    # Se inicializa el término actual en 1
    termino = 1
    # Se define el número de términos a calcular
    numeros_terminos = 20
    # Se ejecuta un ciclo para sumar cada término de la serie
    for i in range(1, numeros_terminos):
        # Se calcula el siguiente término
        # Cada término alterna de signo y se divide por (2i-1)*(2i)
        termino = termino * (-x * x) / ((2 * i - 1) * (2 * i))
        # Se suma el término actual al resultado
        resultado = resultado + termino
    # Se retorna la aproximación del coseno
    return resultado

# Función para calcular el logaritmo natural usando serie de Taylor
# La serie de Taylor para ln(1+x) es: ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ...
# Parámetro: x (número del cual calcular el logaritmo)
# Retorna: la aproximación del logaritmo natural de x
def logaritmo_natural(x):
    # Se verifica si x es menor o igual a 0
    # El logaritmo solo está definido para números positivos
    if x <= 0:
        # Si x no es positivo, se retorna un mensaje de error
        return "Error: El logaritmo no está definido para números menores o iguales a 0"
    # Se verifica si x es 1
    # El logaritmo natural de 1 es 0
    if x == 1:
        # Se retorna 0 directamente
        return 0
    # Si x es mayor que 2, se utiliza la propiedad logarítmica
    # ln(x) = ln(2) + ln(x/2) para hacer la aproximación más precisa
    if x > 2:
        # Se calcula ln(x/2) y se suma ln(2) ≈ 0.693147
        return 0.693147 + logaritmo_natural(x / 2)
    # Se utiliza la serie de Taylor para x - 1
    # Esta fórmula aproxima bien cuando x está cercano a 1
    # Se calcula y = x - 1 para usar en la serie
    y = x - 1
    # Se inicializa el resultado en 0
    resultado = 0
    # Se inicializa el término actual en y
    termino = y
    # Se define el número de términos a calcular
    numeros_terminos = 20
    # Se ejecuta un ciclo para sumar cada término de la serie
    for i in range(1, numeros_terminos):
        # Se suma el término actual al resultado
        resultado = resultado + termino
        # Se calcula el siguiente término
        # Cada término alterna de signo y se multiplica por -y/(i+1)
        termino = termino * (-y * i) / (i + 1)
    # Se retorna la aproximación del logaritmo natural
    return resultado

# SECCIÓN 3: FUNCIÓN PARA EVALUAR FUNCIONES PREDEFINIDAS
# Esta función permite calcular el valor de una función para un valor de x

# Función para evaluar una función predefinida
# Parámetro: x (el valor en el que se evaluará la función)
# Retorna: el valor de la función evaluada en x
def evaluar_funcion(x):
    # Se crea un diccionario que contiene funciones predefinidas
    # Un diccionario es una estructura que relaciona claves con valores
    # Aquí las claves son los nombres de las funciones y los valores son las operaciones
    funciones = {
        # Función lineal: f(x) = 2x + 1
        # Esta es una función de primer grado (línea recta)
        "lineal": lambda x: 2 * x + 1,
        
        # Función cuadrática: f(x) = x²
        # Esta es una función de segundo grado (parábola)
        "cuadratica": lambda x: x * x,
        
        # Función cúbica: f(x) = x³
        # Esta es una función de tercer grado
        "cubica": lambda x: x * x * x,
    }
    # Se retorna el diccionario de funciones
    # El usuario posteriormente seleccionará una función del diccionario
    return funciones


# SECCIÓN 4: FUNCIÓN PARA GRAFICAR EN CONSOLA

# Esta función crea una representación visual de una función en la consola

# Función para graficar una función en consola
# Parámetros: 
#   - nombre_funcion (nombre de la función a graficar)
#   - rango_inicio (inicio del rango de x)
#   - rango_fin (fin del rango de x)
#   - altura (altura máxima de la gráfica)
def graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura):
    # Se obtiene el diccionario de funciones disponibles
    funciones = evaluar_funcion(0)
    
    # Se verifica si la función solicitada existe en el diccionario
    # Es importante validar esto para evitar errores
    if nombre_funcion not in funciones:
        # Si la función no existe, se imprime un mensaje de error
        print("Error: Función no encontrada")
        # Se retorna para terminar la ejecución de la función
        return
    
    # Se obtiene la función del diccionario
    # Esto permite acceder a la función específica que el usuario seleccionó
    funcion = funciones[nombre_funcion]
    
    # Se calcula el tamaño del paso entre puntos
    # Esto determina cuántos puntos se graficarán
    # Un paso más pequeño resulta en más puntos y una gráfica más precisa
    paso = (rango_fin - rango_inicio) / 50
    
    # Se crea una lista que almacenará los valores de la función
    # Una lista es una estructura que puede contener múltiples valores
    valores = []
    
    # Se recorren todos los valores de x desde el inicio hasta el fin
    # Se genera una lista de valores de x con el paso especificado
    x = rango_inicio
    # Se ejecuta un ciclo mientras x sea menor o igual al rango final
    while x <= rango_fin:
        # Se calcula el valor de la función en x
        # Se llamada la función con el valor x y se almacena el resultado
        y = funcion(x)
        # Se agrega el valor y a la lista de valores
        # La función append() añade un elemento al final de la lista
        valores.append(y)
        # Se incrementa x por el paso para pasar al siguiente punto
        x = x + paso
    
    # Se encuentra el valor máximo en la lista de valores
    # Esto es necesario para escalar correctamente la gráfica
    # La función max() retorna el valor más grande de la lista
    valor_maximo = max(valores)
    
    # Se encuentra el valor mínimo en la lista de valores
    # La función min() retorna el valor más pequeño de la lista
    valor_minimo = min(valores)
    
    # Se verifica si el máximo y mínimo son iguales
    # Esto evitaría una división por cero en el siguiente cálculo
    if valor_maximo == valor_minimo:
        # Si son iguales, se establecen como valores diferentes para que funcione la gráfica
        valor_maximo = valor_minimo + 1
    
    # Se crea una matriz para almacenar los caracteres de la gráfica
    # Una matriz es una lista de listas bidimensional
    # El número de filas es 'altura', el número de columnas es la cantidad de valores
    matriz = []
    
    # Se ejecuta un ciclo para crear cada fila de la matriz
    # 'range(altura)' genera números desde 0 hasta altura-1
    for i in range(altura):
        # Se crea una fila vacía (lista vacía)
        fila = []
        # Se ejecuta un ciclo para cada valor de la función
        for j in range(len(valores)):
            # Se normaliza el valor de la función al rango de 0 a altura-1
            # Esto permite que el valor quepa en la matriz
            # (valor - mínimo) / (máximo - mínimo) normaliza a 0-1
            # Se multiplica por (altura - 1) para escalarlo a 0 a altura-1
            valor_normalizado = (valores[j] - valor_minimo) / (valor_maximo - valor_minimo) * (altura - 1)
            
            # Se verifica si este punto debe tener un asterisco
            # Se redondea hacia abajo el valor normalizado usando int()
            # Si la altura actual (altura - 1 - i) coincide con el valor normalizado redondeado,
            # entonces se coloca un asterisco
            if int(valor_normalizado) == altura - 1 - i:
                # Se agrega un asterisco a la fila
                # El asterisco representa un punto de la función
                fila.append("*")
            else:
                # Si no hay punto en esta posición, se agrega un espacio
                fila.append(" ")
        # Se agrega la fila completa a la matriz
        matriz.append(fila)
    
    # Se imprime la gráfica
    # Se ejecuta un ciclo para cada fila de la matriz
    for fila in matriz:
        # Se convierte la fila (que es una lista de caracteres) en una cadena de texto
        # El método join() concatena todos los elementos de la lista
        # Se imprime la cadena resultante
        print("".join(fila))

# ============================================================================
# SECCIÓN 5: FUNCIÓN PARA MOSTRAR HISTORIAL
# ============================================================================
# Esta función muestra todas las operaciones realizadas

# Función para mostrar el historial de operaciones
def mostrar_historial():
    # Se verifica si el historial está vacío
    # Si no hay operaciones registradas, se comunica al usuario
    if len(historial) == 0:
        # Si la longitud del historial es 0, significa que está vacío
        # Se imprime un mensaje indicando que no hay operaciones
        print("\n--- HISTORIAL VACÍO ---")
        print("No hay operaciones registradas aún.\n")
    else:
        # Si hay operaciones en el historial, se muestran todas
        print("\n--- HISTORIAL DE OPERACIONES ---")
        # Se ejecuta un ciclo para cada operación en el historial
        # 'enumerate()' proporciona el índice y el valor de cada elemento
        for indice, operacion in enumerate(historial):
            # Se imprime cada operación con su número
            # indice + 1 se usa porque los humanos contamos desde 1, no desde 0
            print(f"{indice + 1}. {operacion}")
        print()

# ============================================================================
# SECCIÓN 6: FUNCIONES DEL MENÚ
# ============================================================================
# Estas funciones manejan las opciones del menú principal

# Función para mostrar el menú de operaciones básicas
def menu_operaciones_basicas():
    # Esta variable controla si el usuario desea continuar en este menú
    continuar = True
    # Se ejecuta un ciclo mientras continuar sea True
    while continuar:
        # Se imprime el menú de operaciones básicas
        print("\n========== OPERACIONES BÁSICAS ==========")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Volver al menú principal")
        print("==========================================")
        
        # Se solicita al usuario que seleccione una opción
        # input() obtiene texto del usuario
        # int() convierte ese texto a un número entero
        opcion = int(input("Seleccione una operación: "))
        
        # Se verifica cuál opción seleccionó el usuario
        # if verifica la primera condición
        if opcion == 1:
            # El usuario seleccionó suma
            # Se solicitan dos números al usuario
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            # Se llama la función sumar con los números ingresados
            # Se almacena el resultado en una variable
            resultado = sumar(num1, num2)
            # Se imprime el resultado
            print(f"Resultado: {num1} + {num2} = {resultado}")
            # Se agrega la operación al historial
            # format() o f-string crea una cadena de texto con los valores
            historial.append(f"Suma: {num1} + {num2} = {resultado}")
        
        # elif verifica la siguiente condición (si la anterior fue falsa)
        elif opcion == 2:
            # El usuario seleccionó resta
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            # Se llama la función restar
            resultado = restar(num1, num2)
            # Se imprime el resultado
            print(f"Resultado: {num1} - {num2} = {resultado}")
            # Se agrega al historial
            historial.append(f"Resta: {num1} - {num2} = {resultado}")
        
        elif opcion == 3:
            # El usuario seleccionó multiplicación
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            # Se llama la función multiplicar
            resultado = multiplicar(num1, num2)
            # Se imprime el resultado
            print(f"Resultado: {num1} * {num2} = {resultado}")
            # Se agrega al historial
            historial.append(f"Multiplicación: {num1} * {num2} = {resultado}")
        
        elif opcion == 4:
            # El usuario seleccionó división
            num1 = float(input("Ingrese el dividendo (número a dividir): "))
            num2 = float(input("Ingrese el divisor (número que divide): "))
            # Se llama la función dividir
            resultado = dividir(num1, num2)
            # Se imprime el resultado
            print(f"Resultado: {num1} / {num2} = {resultado}")
            # Se agrega al historial
            historial.append(f"División: {num1} / {num2} = {resultado}")
        
        elif opcion == 5:
            # El usuario seleccionó potencia
            base = float(input("Ingrese la base (número a elevar): "))
            exponente = int(input("Ingrese el exponente (a qué potencia elevar): "))
            # Se llama la función potencia
            resultado = potencia(base, exponente)
            # Se imprime el resultado
            print(f"Resultado: {base} ^ {exponente} = {resultado}")
            # Se agrega al historial
            historial.append(f"Potencia: {base} ^ {exponente} = {resultado}")
        
        elif opcion == 6:
            # El usuario seleccionó volver
            # Se establece continuar como False para salir del ciclo
            continuar = False
            # Se imprime un mensaje de regreso
            print("Volviendo al menú principal...")
        
        else:
            # Si la opción no es válida
            # Se imprime un mensaje de error
            print("Opción no válida. Por favor, intente de nuevo.")

# Función para mostrar el menú de operaciones científicas
def menu_operaciones_cientificas():
    # Esta variable controla si el usuario desea continuar en este menú
    continuar = True
    # Se ejecuta un ciclo mientras continuar sea True
    while continuar:
        # Se imprime el menú de operaciones científicas
        print("\n========== OPERACIONES CIENTÍFICAS ==========")
        print("1. Factorial")
        print("2. Raíz cuadrada")
        print("3. Exponencial (e^x)")
        print("4. Seno (ángulo en radianes)")
        print("5. Coseno (ángulo en radianes)")
        print("6. Logaritmo natural")
        print("7. Volver al menú principal")
        print("=============================================")
        
        # Se solicita la opción al usuario
        opcion = int(input("Seleccione una operación científica: "))
        
        # Se verifica cuál opción seleccionó el usuario
        if opcion == 1:
            # El usuario seleccionó factorial
            # Se solicita un número entero
            numero = int(input("Ingrese un número entero (0 o mayor): "))
            # Se llama la función factorial
            resultado = factorial(numero)
            # Se imprime el resultado
            print(f"Factorial de {numero} = {resultado}")
            # Se agrega al historial
            historial.append(f"Factorial: {numero}! = {resultado}")
        
        elif opcion == 2:
            # El usuario seleccionó raíz cuadrada
            numero = float(input("Ingrese un número (0 o mayor): "))
            # Se llama la función raiz_cuadrada
            resultado = raiz_cuadrada(numero)
            # Se imprime el resultado
            print(f"Raíz cuadrada de {numero} = {resultado}")
            # Se agrega al historial
            historial.append(f"Raíz cuadrada: √{numero} = {resultado}")
        
        elif opcion == 3:
            # El usuario seleccionó exponencial
            numero = float(input("Ingrese el exponente: "))
            # Se llama la función exponencial
            resultado = exponencial(numero)
            # Se imprime el resultado
            print(f"e^{numero} = {resultado}")
            # Se agrega al historial
            historial.append(f"Exponencial: e^{numero} = {resultado}")
        
        elif opcion == 4:
            # El usuario seleccionó seno
            # Se solicita el ángulo en radianes
            numero = float(input("Ingrese el ángulo en radianes: "))
            # Se llama la función seno
            resultado = seno(numero)
            # Se imprime el resultado
            print(f"Seno({numero} rad) = {resultado}")
            # Se agrega al historial
            historial.append(f"Seno: sen({numero} rad) = {resultado}")
        
        elif opcion == 5:
            # El usuario seleccionó coseno
            # Se solicita el ángulo en radianes
            numero = float(input("Ingrese el ángulo en radianes: "))
            # Se llama la función coseno
            resultado = coseno(numero)
            # Se imprime el resultado
            print(f"Coseno({numero} rad) = {resultado}")
            # Se agrega al historial
            historial.append(f"Coseno: cos({numero} rad) = {resultado}")
        
        elif opcion == 6:
            # El usuario seleccionó logaritmo natural
            numero = float(input("Ingrese un número (mayor a 0): "))
            # Se llama la función logaritmo_natural
            resultado = logaritmo_natural(numero)
            # Se imprime el resultado
            print(f"Logaritmo natural de {numero} = {resultado}")
            # Se agrega al historial
            historial.append(f"Logaritmo natural: ln({numero}) = {resultado}")
        
        elif opcion == 7:
            # El usuario seleccionó volver
            # Se establece continuar como False
            continuar = False
            # Se imprime un mensaje
            print("Volviendo al menú principal...")
        
        else:
            # Si la opción no es válida
            print("Opción no válida. Por favor, intente de nuevo.")

# Función para el menú de evaluación de funciones
def menu_evaluar_funcion():
    # Se obtiene el diccionario de funciones
    funciones = evaluar_funcion(0)
    
    # Se imprime el menú de funciones disponibles
    print("\n========== EVALUAR FUNCIÓN ==========")
    print("Funciones disponibles:")
    # Se itera sobre cada función en el diccionario
    # enumerate() proporciona el índice comenzando desde 0
    for i, nombre_funcion in enumerate(funciones.keys()):
        # Se imprime cada función disponible
        # Se suma 1 al índice porque los usuarios cuentan desde 1
        print(f"{i + 1}. {nombre_funcion}")
    print("====================================")
    
    # Se solicita al usuario que seleccione una función
    seleccion = int(input("Seleccione una función (número): "))
    
    # Se convierte el diccionario a una lista para acceder por índice
    lista_funciones = list(funciones.keys())
    
    # Se verifica si la selección está en el rango válido
    # La selección debe estar entre 1 y la cantidad de funciones
    if seleccion < 1 or seleccion > len(lista_funciones):
        # Si está fuera de rango, se imprime un error
        print("Opción no válida")
        return
    
    # Se obtiene el nombre de la función seleccionada
    # Se resta 1 a seleccion porque las listas comienzan en 0
    nombre_funcion = lista_funciones[seleccion - 1]
    
    # Se obtiene la función del diccionario
    funcion = funciones[nombre_funcion]
    
    # Se solicita el valor de x
    x = float(input("Ingrese el valor de x: "))
    
    # Se evalúa la función con el valor x
    resultado = funcion(x)
    
    # Se imprime el resultado
    print(f"f({x}) = {resultado}")
    
    # Se agrega al historial
    historial.append(f"Función {nombre_funcion}: f({x}) = {resultado}")

# Función para el menú de graficación
def menu_graficar_funcion():
    # Se obtiene el diccionario de funciones
    funciones = evaluar_funcion(0)
    
    # Se imprime el menú de graficación
    print("\n========== GRAFICAR FUNCIÓN ==========")
    print("Funciones disponibles:")
    # Se itera sobre cada función disponible
    for i, nombre_funcion in enumerate(funciones.keys()):
        # Se imprime cada función
        print(f"{i + 1}. {nombre_funcion}")
    print("======================================")
    
    # Se solicita al usuario que seleccione una función
    seleccion = int(input("Seleccione una función (número): "))
    
    # Se convierte el diccionario a una lista
    lista_funciones = list(funciones.keys())
    
    # Se verifica si la selección es válida
    if seleccion < 1 or seleccion > len(lista_funciones):
        # Si no es válida, se imprime un error
        print("Opción no válida")
        return
    
    # Se obtiene el nombre de la función
    nombre_funcion = lista_funciones[seleccion - 1]
    
    # Se solicita el rango de valores para x
    rango_inicio = float(input("Ingrese el inicio del rango (valor de x inicial): "))
    rango_fin = float(input("Ingrese el fin del rango (valor de x final): "))
    
    # Se solicita la altura de la gráfica
    altura = int(input("Ingrese la altura de la gráfica (número de filas): "))
    
    # Se llama la función para graficar
    graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura)
    
    # Se agrega al historial
    historial.append(f"Gráfica: {nombre_funcion} de {rango_inicio} a {rango_fin}")

# ============================================================================
# SECCIÓN 7: MENÚ PRINCIPAL
# ============================================================================
# Esta es la función principal que maneja todo el programa

# Función principal
def main():
    # Esta variable controla si el programa debe continuar ejecutándose
    ejecutar = True
    
    # Se ejecuta un ciclo mientras ejecutar sea True
    while ejecutar:
        # Se imprime el menú principal
        print("\n╔════════════════════════════════════════════════════╗")
        print("║   CALCULADORA CIENTÍFICA GRAFICADORA             ║")
        print("║   Pensamiento Algorítmico - Proyecto 3           ║")
        print("╚════════════════════════════════════════════════════╝")
        
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Operaciones básicas")
        print("2. Operaciones científicas")
        print("3. Evaluar una función")
        print("4. Graficar una función en consola")
        print("5. Ver historial de operaciones")
        print("6. Salir del programa")
        print("--------------------")
        
        # Se solicita al usuario que seleccione una opción
        # input() obtiene la entrada del usuario como texto
        # int() convierte ese texto a número entero
        opcion = int(input("Seleccione una opción: "))
        
        # Se verifica cuál opción seleccionó el usuario
        # if verifica la primera condición
        if opcion == 1:
            # El usuario seleccionó operaciones básicas
            # Se llama la función del menú de operaciones básicas
            menu_operaciones_basicas()
        
        # elif verifica la siguiente condición (si la anterior fue falsa)
        elif opcion == 2:
            # El usuario seleccionó operaciones científicas
            # Se llama la función del menú de operaciones científicas
            menu_operaciones_cientificas()
        
        elif opcion == 3:
            # El usuario seleccionó evaluar función
            # Se llama la función del menú de evaluación
            menu_evaluar_funcion()
        
        elif opcion == 4:
            # El usuario seleccionó graficar función
            # Se llama la función del menú de graficación
            menu_graficar_funcion()
        
        elif opcion == 5:
            # El usuario seleccionó ver historial
            # Se llama la función para mostrar el historial
            mostrar_historial()
        
        elif opcion == 6:
            # El usuario seleccionó salir
            # Se establece ejecutar como False para terminar el ciclo
            ejecutar = False
            # Se imprime un mensaje de despedida
            print("\n¡Gracias por usar la Calculadora Científica Graficadora!")
            print("Fin del programa.\n")
        
        else:
            # Si la opción no es válida (no está entre 1 y 6)
            # Se imprime un mensaje de error
            print("\nOpción no válida. Por favor, seleccione una opción entre 1 y 6.\n")

# ============================================================================
# SECCIÓN 8: INICIALIZACIÓN DEL PROGRAMA
# ============================================================================
# Esta sección ejecuta el programa cuando se corre el archivo

# Se verifica si el archivo se está ejecutando directamente
# (no si se está importando desde otro archivo)
# __name__ es una variable especial que vale "__main__" cuando se corre directamente
if __name__ == "__main__":
    # Se llama la función main() para iniciar el programa
    main()
