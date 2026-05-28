# CALCULADORA CIENTÍFICA GRAFICADORA
# Proyecto de Pensamiento Algorítmico

# Preparamos un espacio vacío llamado "historial" para guardar información. 
# La calculadora usará este sector para recordar todas las operaciones matemáticas exactas que el usuario realice durante la sesión, como si fuera la cinta de papel de una caja registradora.
historial = []


# ============================================================================
# SECCIÓN 0: REVISIÓN DE SEGURIDAD Y TRADECTOR DE PALABRAS A NÚMEROS
# ============================================================================

# Esta herramienta revisa si el texto que el usuario escribió realmente es un número válido. 
# El programa bloquea letras, símbolos extraños o espacios en blanco antes de que la calculadora intente hacer la cuenta y falle.
def es_numero_valido(cadena, tipo="float"):
    # Primero, le quitamos los espacios en blanco que el usuario pudo dejar por accidente al principio o al final del texto.
    cadena = cadena.strip()
    
    # Si después de quitar los espacios no queda nada escrito, el programa sabe que el dato es inválido.
    if cadena == "":
        return False
        
    # Aquí revisamos si la calculadora necesita específicamente un número entero (un número sin decimales).
    if tipo == "int":
        # Miramos si el primer símbolo es un guion, lo que indicaría que es un número negativo.
        if cadena[0] == "-":
            # Si tiene un guion, confirmamos que el resto del texto contenga únicamente números.
            if len(cadena) > 1 and cadena[1:].isdigit():
                return True
            # Si solo escribió un guion sin números, rechazamos la entrada.
            return False
        else:
            # Si no es negativo, simplemente comprobamos que todo lo que escribió sean números.
            return cadena.isdigit()
            
    # Aquí revisamos si la calculadora acepta un número con decimales (flotante).
    if tipo == "float":
        # Empezamos a contar cuántos puntos decimales escribió el usuario.
        puntos = 0
        # Revisamos letra por letra todo el texto que ingresó.
        for char in cadena:
            # Si encontramos un punto, sumamos uno a nuestra cuenta.
            if char == '.':
                puntos = puntos + 1
                
        # Un número real solo puede tener un punto decimal. Si encontramos dos o más, es un error del usuario.
        if puntos > 1:
            return False
            
        # Creamos un texto nuevo donde pondremos los números pero dejaremos por fuera el punto decimal para poder revisarlos fácilmente.
        texto_limpio = ""
        for char in cadena:
            if char != '.':
                texto_limpio = texto_limpio + char
                
        # Si después de quitar el punto no queda nada, significa que el usuario solo escribió un punto. Eso no es un número.
        if texto_limpio == "":
            return False
            
        # Revisamos si el número decimal empieza con un signo negativo.
        if texto_limpio[0] == "-":
            # Verificamos que tenga números después del signo negativo.
            if len(texto_limpio) > 1 and texto_limpio[1:].isdigit():
                return True
            return False
        else:
            # Finalmente, si no es negativo, verificamos que el texto limpio contenga puros números válidos.
            return texto_limpio.isdigit()

# funciones pedidas para la explosicion
# Esta nueva herramienta traduce palabras como "pi" o "pi/2" a los números decimales reales que la computadora sí puede usar para calcular.
def obtener_valor_flotante(cadena):
    # Limpiamos los espacios y pasamos todo a minúsculas para que no importe si escriben en mayúsculas.
    texto = cadena.strip().lower()
    
    # Si el usuario escribió exactamente "pi", le entregamos el valor de la constante.
    if texto == "pi":
        return 3.14159265359
    # Si escribió "pi/2", hacemos la división y le entregamos el equivalente decimal de pi medios.
    if texto == "pi/2":
        return 1.57079632679
    # Si escribió "-pi", entregamos el valor negativo de la constante.
    if texto == "-pi":
        return -3.14159265359
    # Si escribió "-pi/2", entregamos el valor decimal negativo.
    if texto == "-pi/2":
        return -1.57079632679
    # Si escribió "2pi" o "2*pi", entregamos el valor de una vuelta completa en radianes.
    if texto == "2pi" or texto == "2*pi":
        return 6.28318530718
        
    # Si no escribió ninguna palabra clave, revisamos si ingresó un número normal con decimales.
    if es_numero_valido(cadena, "float"):
        return float(cadena)
        
    # Si no es ninguna de las anteriores, significa que es un texto inválido y devolvemos la señal de vacío.
    return None


# ============================================================================
# SECCIÓN 1: OPERACIONES MATEMÁTICAS BÁSICAS
# ============================================================================

# Esta herramienta toma el primer número y el segundo número para sumarlos directamente.
def sumar(a, b):
    resultado = a + b
    # Entrega el resultado final para que la calculadora lo muestre en pantalla.
    return resultado

# Esta herramienta toma un número principal y le quita la cantidad del segundo número.
def restar(a, b):
    resultado = a - b
    return resultado

# Esta herramienta aumenta el primer número tantas veces como lo indique el segundo número.
def multiplicar(a, b):
    resultado = a * b
    return resultado

# Esta herramienta reparte el primer número en las partes que indique el segundo número.
def dividir(a, b):
    # En matemáticas no existe la división por cero. Si el usuario intenta hacerlo, el programa lo detiene y le avisa del error.
    if b == 0:
        return "Error: No se puede dividir entre cero"
    resultado = a / b
    return resultado

# Esta herramienta multiplica un número por sí mismo varias veces.
def potencia(base, exponente):
    # Arrancamos la cuenta en 1, que es el punto de partida normal para multiplicar.
    resultado = 1
    # El programa repite la multiplicación tantas veces como indique el exponente.
    for i in range(exponente):
        # Cada vez que repite, multiplica lo que ya tiene por el número base.
        resultado = resultado * base
    return resultado


# ============================================================================
# SECCIÓN 2: OPERACIONES CIENTÍFICAS COMPLEJAS
# ============================================================================

# El factorial multiplica todos los números enteros desde el 1 hasta el número que pida el usuario.
def factorial(n):
    # Los números negativos no tienen factorial, así que el programa muestra un error si el usuario pone uno.
    if n < 0:
        return "Error: El factorial no está definido para números negativos"
    resultado = 1
    # Vamos pasando por todos los números del 1 al valor ingresado y los multiplicamos uno por uno.
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# Como no usamos herramientas automáticas, el programa adivina la raíz cuadrada acercándose poco a poco al resultado correcto.
def raiz_cuadrada(n):
    # No existen raíces cuadradas reales para números negativos, así que frenamos la operación aquí.
    if n < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    # La raíz de cero siempre será cero.
    if n == 0:
        return 0
    # Para empezar a adivinar, el programa toma la mitad del número.
    aproximacion = n / 2.0
    # Le decimos al programa que mejore su adivinanza 10 veces seguidas para que el resultado sea muy exacto.
    iteraciones = 10
    for i in range(iteraciones):
        # Esta es una fórmula matemática que corrige el error en cada intento y se acerca al valor real.
        aproximacion = (aproximacion + n / aproximacion) / 2.0
    return aproximacion

# Esta función calcula el valor de "e" elevado a un número, sumando pedacitos cada vez más pequeños.
def exponencial(x):
    resultado = 1
    termino = 1
    # Hacemos el cálculo 20 veces para asegurar que el número final sea preciso.
    numeros_terminos = 20
    for i in range(1, numeros_terminos):
        # Calculamos la siguiente pieza de la operación.
        termino = termino * x / i
        # Agregamos esta pieza al resultado total.
        resultado = resultado + termino
    return resultado

# El programa calcula el seno de un ángulo sumando y restando fracciones.
def seno(x):
    # Guardamos el valor de Pi con muchos decimales.
    pi = 3.14159265359
    # Ajustamos el ángulo para que no sea un número gigante y sea más fácil de calcular.
    x = x % (2 * pi)
    if x > pi:
        x = x - 2 * pi
    resultado = 0
    termino = x
    numeros_terminos = 20
    # Hacemos 20 repeticiones para que la suma final se acerque muchísimo al valor real del seno.
    for i in range(1, numeros_terminos):
        resultado = resultado + termino
        # Esta fórmula matemática alterna entre sumar y restar partes cada vez más chicas.
        termino = termino * (-x * x) / ((2 * i) * (2 * i + 1))
    return resultado

# Funciona igual que el seno, pero calcula el coseno del ángulo.
def coseno(x):
    pi = 3.14159265359
    # Achicamos el ángulo al tamaño de un solo círculo para no perder exactitud.
    x = x % (2 * pi)
    if x > pi:
        x = x - 2 * pi
    # El coseno siempre arranca la suma desde el número 1.
    resultado = 1
    termino = 1
    numeros_terminos = 20
    # Ejecutamos la corrección matemática 20 veces.
    for i in range(1, numeros_terminos):
        # Construimos la fracción necesaria para afinar el resultado.
        termino = termino * (-x * x) / ((2 * i - 1) * (2 * i))
        # Sumamos la fracción al monto total.
        resultado = resultado + termino
    return resultado

# Calcula el logaritmo natural aproximando el número paso a paso.
def logaritmo_natural(x):
    # El logaritmo no funciona con el cero ni con números negativos.
    if x <= 0:
        return "Error: El logaritmo no está definido para números menores o iguales a 0"
    # Si el usuario pide el logaritmo de 1, la respuesta es 0 automáticamente.
    if x == 1:
        return 0
    # Si el número es muy grande, lo partimos a la mitad para que la fórmula no falle y luego compensamos el resultado.
    if x > 2:
        return 0.693147 + logaritmo_natural(x / 2)
    # Ajustamos el número restándole 1 para que la suma funcione bien.
    y = x - 1
    resultado = 0
    termino = y
    numeros_terminos = 20
    # Repetimos el ajuste fraccionario 20 veces.
    for i in range(1, numeros_terminos):
        resultado = resultado + termino
        termino = termino * (-y * i) / (i + 1)
    return resultado
# Herramienta pedida pra la exposicion
# Esta herramienta calcula la tangente de un ángulo dividiendo su valor del seno entre su valor del coseno.
def tangente(x):
    s = seno(x)
    c = coseno(x)
    
    c_absoluto = c
    if c_absoluto < 0:
        c_absoluto = -c_absoluto
        
    # Si el coseno está muy cerca de cero, la división se bloquea para evitar fallos catastróficos.
    if c_absoluto < 0.000001:
        return "Error: La tangente no esta definida para este angulo (division por cero)"
        
    return s / c


# ============================================================================
# SECCIÓN 3: EVALUACIÓN DE FUNCIONES MATEMÁTICAS
# ============================================================================

# Esta parte guarda las fórmulas matemáticas que el usuario puede elegir para probar o para dibujar en la pantalla.
def evaluar_funcion(x):
    # Creamos un menú interno donde asociamos un nombre o abreviación con la operación exacta que debe hacer el programa.
    funciones = {
        "lineal": lambda x: 2 * x + 1,
        "cuadratica": lambda x: x * x,
        "cubica": lambda x: x * x * x,
        "ln": lambda x: logaritmo_natural(x),
        "exp": lambda x: exponencial(x),
        "sin": lambda x: seno(x),
        "cos": lambda x: coseno(x),
        "tan": lambda x: tangente(x)
    }
    return funciones


# ============================================================================
# SECCIÓN 4: DIBUJO DE GRÁFICAS EN PANTALLA
# ============================================================================

# El programa lee los números y dibuja una línea usando asteriscos.
def graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura):
    funciones = evaluar_funcion(0)
    
    if nombre_funcion not in funciones:
        print("Error: Función no encontrada")
        return
    
    funcion = funciones[nombre_funcion]
    paso = (rango_fin - rango_inicio) / 50
    valores = []
    
    x = rango_inicio
    while x <= rango_fin:
        y = funcion(x)
        
        # Si la función da error de texto en un punto (como logaritmo negativo), lo mandamos a cero para proteger la gráfica.
        if type(y) == str:
            y = 0.0
            
        valores.append(y)
        x = x + paso
    
    valor_maximo = max(valores)
    valor_minimo = min(valores)
    
    if valor_maximo == valor_minimo:
        valor_maximo = valor_minimo + 1
    
    matriz = []
    for i in range(altura):
        fila = []
        for j in range(len(valores)):
            valor_normalizado = (valores[j] - valor_minimo) / (valor_maximo - valor_minimo) * (altura - 1)
            
            if int(valor_normalizado) == altura - 1 - i:
                fila.append("*")
            else:
                fila.append(" ")
        matriz.append(fila)
    
    for fila in matriz:
        print("".join(fila))
        
    ancho = len(valores)
    print("-" * ancho)
    
    eti_inicio = str(round(rango_inicio, 1))
    eti_fin = str(round(rango_fin, 1))
    eti_medio = str(round((rango_inicio + rango_fin) / 2.0, 1))
    
    linea_etiquetas = [" "] * ancho
    
    for i in range(len(eti_inicio)):
        if i < ancho:
            linea_etiquetas[i] = eti_inicio[i]
            
    pos_fin = ancho - len(eti_fin)
    for i in range(len(eti_fin)):
        if pos_fin + i >= 0 and pos_fin + i < ancho:
            linea_etiquetas[pos_fin + i] = eti_fin[i]
            
    pos_medio = (ancho // 2) - (len(eti_medio) // 2)
    for i in range(len(eti_medio)):
        if pos_medio + i > len(eti_inicio) and pos_medio + i < pos_fin:
            linea_etiquetas[pos_medio + i] = eti_medio[i]
            
    print("".join(linea_etiquetas))


# ============================================================================
# SECCIÓN 5: LECTURA DEL HISTORIAL
# ============================================================================

def mostrar_historial():
    if len(historial) == 0:
        print("Historial vacio")
    else:
        print("Historial de operaciones:")
        for indice, operacion in enumerate(historial):
            print(f"{indice + 1}. {operacion}")
        print()


# ============================================================================
# SECCIÓN 6: PANTALLAS DE OPCIONES PARA EL USUARIO
# ============================================================================

def menu_operaciones_basicas():
    continuar = True
    while continuar:
        print("Operaciones basicas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Potencia")
        print("6. Volver al menu principal")
        
        opcion_str = input("Seleccione una operacion: ")
        if not es_numero_valido(opcion_str, "int"):
            print("Entrada invalida.")
            continue
            
        opcion = int(opcion_str)
        
        if opcion == 1:
            num1_str = input("Ingrese el primer numero: ")
            num1 = obtener_valor_flotante(num1_str)
            if num1 is None:
                print("Dato invalido.")
                continue
                
            num2_str = input("Ingrese el segundo numero: ")
            num2 = obtener_valor_flotante(num2_str)
            if num2 is None:
                print("Dato invalido.")
                continue
                
            resultado = sumar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
            historial.append(f"Suma: {num1} + {num2} = {resultado}")
        
        elif opcion == 2:
            num1_str = input("Ingrese el primer numero: ")
            num1 = obtener_valor_flotante(num1_str)
            if num1 is None:
                print("Dato invalido.")
                continue
                
            num2_str = input("Ingrese el segundo numero: ")
            num2 = obtener_valor_flotante(num2_str)
            if num2 is None:
                print("Dato invalido.")
                continue
                
            resultado = restar(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
            historial.append(f"Resta: {num1} - {num2} = {resultado}")
        
        elif opcion == 3:
            num1_str = input("Ingrese el primer numero: ")
            num1 = obtener_valor_flotante(num1_str)
            if num1 is None:
                print("Dato invalido.")
                continue
                
            num2_str = input("Ingrese el segundo numero: ")
            num2 = obtener_valor_flotante(num2_str)
            if num2 is None:
                print("Dato invalido.")
                continue
                
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
            historial.append(f"Multiplicacion: {num1} * {num2} = {resultado}")
        
        elif opcion == 4:
            num1_str = input("Ingrese el dividendo: ")
            num1 = obtener_valor_flotante(num1_str)
            if num1 is None:
                print("Dato invalido.")
                continue
                
            num2_str = input("Ingrese el divisor: ")
            num2 = obtener_valor_flotante(num2_str)
            if num2 is None:
                print("Dato invalido.")
                continue
                
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
            historial.append(f"Division: {num1} / {num2} = {resultado}")
        
        elif opcion == 5:
            base_str = input("Ingrese la base: ")
            base = obtener_valor_flotante(base_str)
            if base is None:
                print("Dato invalido.")
                continue
                
            exponente_str = input("Ingrese el exponente (entero): ")
            if not es_numero_valido(exponente_str, "int"):
                print("Dato invalido.")
                continue
                
            exponente = int(exponente_str)
            resultado = potencia(base, exponente)
            print(f"Resultado: {base} ^ {exponente} = {resultado}")
            historial.append(f"Potencia: {base} ^ {exponente} = {resultado}")
        
        elif opcion == 6:
            continuar = False
            print("Volviendo...")
        else:
            print("Opcion no valida.")

def menu_operaciones_cientificas():
    continuar = True
    while continuar:
        print("Operaciones cientificas")
        print("1. Factorial")
        print("2. Raiz cuadrada")
        print("3. Exponencial (e^x)")
        print("4. Seno (angulo en radianes)")
        print("5. Coseno (angulo en radianes)")
        print("6. Logaritmo natural")
        print("7. Volver al menu principal")
        
        opcion_str = input("Seleccione una operacion cientifica: ")
        if not es_numero_valido(opcion_str, "int"):
            print("Entrada invalida.")
            continue
            
        opcion = int(opcion_str)
        
        if opcion == 1:
            numero_str = input("Ingrese un numero entero: ")
            if not es_numero_valido(numero_str, "int"):
                print("Dato invalido.")
                continue
            numero = int(numero_str)
            resultado = factorial(numero)
            print(f"Factorial de {numero} = {resultado}")
            historial.append(f"Factorial: {numero}! = {resultado}")
        
        elif opcion == 2:
            numero_str = input("Ingrese un numero: ")
            numero = obtener_valor_flotante(numero_str)
            if numero is None:
                print("Dato invalido.")
                continue
                
            resultado = raiz_cuadrada(numero)
            print(f"Raiz cuadrada de {numero} = {resultado}")
            historial.append(f"Raiz cuadrada: √{numero} = {resultado}")
        
        elif opcion == 3:
            numero_str = input("Ingrese el exponente: ")
            numero = obtener_valor_flotante(numero_str)
            if numero is None:
                print("Dato invalido.")
                continue
                
            resultado = exponencial(numero)
            print(f"e^{numero} = {resultado}")
            historial.append(f"Exponencial: e^{numero} = {resultado}")
        
        elif opcion == 4:
            numero_str = input("Ingrese el angulo en radianes: ")
            numero = obtener_valor_flotante(numero_str)
            if numero is None:
                print("Dato invalido.")
                continue
                
            resultado = seno(numero)
            print(f"Seno({numero} rad) = {resultado}")
            historial.append(f"Seno: sen({numero} rad) = {resultado}")
        
        elif opcion == 5:
            numero_str = input("Ingrese el angulo en radianes: ")
            numero = obtener_valor_flotante(numero_str)
            if numero is None:
                print("Dato invalido.")
                continue
                
            resultado = coseno(numero)
            print(f"Coseno({numero} rad) = {resultado}")
            historial.append(f"Coseno: cos({numero} rad) = {resultado}")
        
        elif opcion == 6:
            numero_str = input("Ingrese un numero: ")
            numero = obtener_valor_flotante(numero_str)
            if numero is None:
                print("Dato invalido.")
                continue
                
            resultado = logaritmo_natural(numero)
            print(f"Logaritmo natural de {numero} = {resultado}")
            historial.append(f"Logaritmo natural: ln({numero}) = {resultado}")
        
        elif opcion == 7:
            continuar = False
            print("Volviendo...")
        else:
            print("Opcion no valida.")

def menu_evaluar_funcion():
    while True:
        funciones = evaluar_funcion(0)
        print("Evaluar funcion")
        for i, nombre_funcion in enumerate(funciones.keys()):
            print(f"{i + 1}. {nombre_funcion}")
        
        seleccion_str = input("Seleccione una funcion o 0 para volver: ")
        if not es_numero_valido(seleccion_str, "int"):
            print("Entrada invalida.")
            continue
            
        seleccion = int(seleccion_str)
        if seleccion == 0:
            return
            
        lista_funciones = list(funciones.keys())
        if seleccion < 1 or seleccion > len(lista_funciones):
            print("Opcion no valida.")
            continue
        
        nombre_funcion = lista_funciones[seleccion - 1]
        funcion = funciones[nombre_funcion]
        
        x_str = input("Ingrese el valor de x: ")
        x = obtener_valor_flotante(x_str)
        if x is None:
            print("Entrada invalida.")
            continue
            
        resultado = funcion(x)
        print(f"f({x}) = {resultado}")
        historial.append(f"Funcion {nombre_funcion}: f({x}) = {resultado}")
        break

def menu_graficar_funcion():
    while True:
        funciones = evaluar_funcion(0)
        print("Graficar funcion")
        for i, nombre_funcion in enumerate(funciones.keys()):
            print(f"{i + 1}. {nombre_funcion}")
        
        seleccion_str = input("Seleccione una funcion o 0 para volver: ")
        if not es_numero_valido(seleccion_str, "int"):
            print("Entrada invalida.")
            continue
            
        seleccion = int(seleccion_str)
        if seleccion == 0:
            return
            
        lista_funciones = list(funciones.keys())
        if seleccion < 1 or seleccion > len(lista_funciones):
            print("Opcion no valida.")
            continue
        
        nombre_funcion = lista_funciones[seleccion - 1]
        
        rango_inicio_str = input("Ingrese el inicio del rango: ")
        rango_inicio = obtener_valor_flotante(rango_inicio_str)
        if rango_inicio is None:
            print("Entrada invalida.")
            continue
            
        rango_fin_str = input("Ingrese el fin del rango: ")
        rango_fin = obtener_valor_flotante(rango_fin_str)
        if rango_fin is None:
            print("Entrada invalida.")
            continue
            
        altura_str = input("Ingrese la altura de la grafica: ")
        if not es_numero_valido(altura_str, "int"):
            print("Entrada invalida.")
            continue
            
        altura = int(altura_str)
        
        graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura)
        historial.append(f"Grafica: {nombre_funcion} de {rango_inicio} a {rango_fin}")
        break

# Este es el corazón operativo del programa que conecta y organiza todos los menús.
def main():
    opcion = 0
    while opcion != 6:
        print("CALCULADORA CIENTIFICA GRAFICADORA")
        print("1. Operaciones basicas")
        print("2. Operaciones cientificas")
        print("3. Evaluar funcion")
        print("4. Graficar funcion")
        print("5. Ver historial")
        print("6. Salir")
        
        opcion_str = input("Seleccione una opcion: ")
        if not es_numero_valido(opcion_str, "int"):
            print("Opcion no valida")
            continue
            
        opcion = int(opcion_str)
        
        if opcion == 1:
            menu_operaciones_basicas()
        elif opcion == 2:
            menu_operaciones_cientificas()
        elif opcion == 3:
            menu_evaluar_funcion()
        elif opcion == 4:
            menu_graficar_funcion()
        elif opcion == 5:
            mostrar_historial()
        elif opcion == 6:
            print("Fin del programa")
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()