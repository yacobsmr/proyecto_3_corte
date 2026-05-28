# CALCULADORA CIENTÍFICA GRAFICADORA
# Proyecto de Pensamiento Algorítmico

# Preparamos un espacio vacío llamado "historial" para guardar información. 
# La calculadora usará este sector para recordar todas las operaciones matemáticas exactas que el usuario realice durante la sesión, como si fuera la cinta de papel de una caja registradora.
historial = []


# ============================================================================
# SECCIÓN 0: REVISIÓN DE SEGURIDAD PARA LOS NÚMEROS INGRESADOS
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

# El factorial multiplica todos los números enteros desde el 1 hasta el número que pida el usuario (ejemplo: 4! es 1*2*3*4).
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


# ============================================================================
# SECCIÓN 3: EVALUACIÓN DE FUNCIONES MATEMÁTICAS
# ============================================================================

# Esta parte guarda las fórmulas matemáticas que el usuario puede elegir para probar con un número específico.
def evaluar_funcion(x):
    # Creamos un menú interno donde asociamos un nombre con la operación que debe hacer.
    funciones = {
        # Si elige lineal, el programa multiplica el número por 2 y le suma 1.
        "lineal": lambda x: 2 * x + 1,
        # Si elige cuadrática, el programa multiplica el número por sí mismo.
        "cuadratica": lambda x: x * x,
        # Si elige cúbica, el programa multiplica el número por sí mismo tres veces.
        "cubica": lambda x: x * x * x,
    }
    # Le devolvemos estas opciones al menú principal para que el usuario pueda elegir.
    return funciones


# ============================================================================
# SECCIÓN 4: DIBUJO DE GRÁFICAS EN PANTALLA
# ============================================================================

# El programa lee los números y dibuja una línea usando asteriscos.
def graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura):
    # Pedimos la lista de fórmulas disponibles.
    funciones = evaluar_funcion(0)
    
    # Comprobamos que el usuario haya elegido un nombre que realmente existe en nuestra lista.
    if nombre_funcion not in funciones:
        print("Error: Función no encontrada")
        # Si se equivocó, detenemos el dibujo y salimos.
        return
    
    # Tomamos la fórmula correcta que el usuario pidió.
    funcion = funciones[nombre_funcion]
    # Calculamos la distancia que habrá entre cada punto evaluado para que la curva se vea suave (50 puntos en total).
    paso = (rango_fin - rango_inicio) / 50
    # Preparamos un espacio para guardar los resultados de cada punto.
    valores = []
    
    # Empezamos a revisar desde el primer número que el usuario puso como inicio.
    x = rango_inicio
    # Mientras no lleguemos al final del recorrido, seguimos avanzando.
    while x <= rango_fin:
        # Usamos la fórmula matemática para calcular dónde debe ir el punto en la pantalla.
        y = funcion(x)
        # Guardamos la altura de ese punto en nuestra memoria.
        valores.append(y)
        # Damos un pequeño paso hacia adelante para calcular el siguiente punto.
        x = x + paso
    
    # Buscamos cuál fue el punto más alto de todos.
    valor_maximo = max(valores)
    # Buscamos cuál fue el punto más bajo.
    valor_minimo = min(valores)
    
    # Si el punto más alto y el más bajo son iguales, la gráfica es una línea recta horizontal y la ajustamos para que se pueda dibujar sin error.
    if valor_maximo == valor_minimo:
        valor_maximo = valor_minimo + 1
    
    # Preparamos una cuadrícula invisible para armar el dibujo renglón por renglón.
    matriz = []
    # Vamos revisando desde arriba hacia abajo.
    for i in range(altura):
        # Preparamos un renglón vacío.
        fila = []
        # Revisamos todos los puntos calculados de izquierda a derecha.
        for j in range(len(valores)):
            # Escalamos el número real para que quepa exactamente en el tamaño de pantalla que pidió el usuario.
            valor_normalizado = (valores[j] - valor_minimo) / (valor_maximo - valor_minimo) * (altura - 1)
            
            # Si la altura actual coincide con la posición del punto, dibujamos un asterisco.
            if int(valor_normalizado) == altura - 1 - i:
                fila.append("*")
            # Si no coincide, dejamos el espacio en blanco para no manchar el dibujo.
            else:
                fila.append(" ")
        # Cuando terminamos de revisar el renglón entero, lo guardamos en la cuadrícula.
        matriz.append(fila)
    
    # Ahora que el dibujo está armado en la memoria, lo imprimimos línea por línea en la pantalla.
    for fila in matriz:
        print("".join(fila))
        
    # Medimos qué tan ancho quedó el dibujo.
    ancho = len(valores)
    # Dibujamos una línea recta en la base usando guiones.
    print("-" * ancho)
    
    # Preparamos los textos que mostrarán los números de referencia debajo del dibujo. Redondeamos para que no sean muy largos.
    eti_inicio = str(round(rango_inicio, 1))
    eti_fin = str(round(rango_fin, 1))
    eti_medio = str(round((rango_inicio + rango_fin) / 2.0, 1))
    
    # Creamos un renglón completamente vacío del mismo ancho que el dibujo.
    linea_etiquetas = [" "] * ancho
    
    # Escribimos el primer número al lado izquierdo del renglón.
    for i in range(len(eti_inicio)):
        if i < ancho:
            linea_etiquetas[i] = eti_inicio[i]
            
    # Calculamos dónde debe empezar el último número para que quede alineado a la derecha.
    pos_fin = ancho - len(eti_fin)
    # Escribimos el último número letra por letra.
    for i in range(len(eti_fin)):
        if pos_fin + i >= 0 and pos_fin + i < ancho:
            linea_etiquetas[pos_fin + i] = eti_fin[i]
            
    # Buscamos la mitad exacta del dibujo y acomodamos el número central para que quede centrado.
    pos_medio = (ancho // 2) - (len(eti_medio) // 2)
    # Escribimos el número central asegurándonos de que no choque ni se mezcle con los números de las orillas.
    for i in range(len(eti_medio)):
        if pos_medio + i > len(eti_inicio) and pos_medio + i < pos_fin:
            linea_etiquetas[pos_medio + i] = eti_medio[i]
            
    # Mostramos los números en pantalla justo debajo de la línea base.
    print("".join(linea_etiquetas))


# ============================================================================
# SECCIÓN 5: LECTURA DEL HISTORIAL
# ============================================================================

# El programa lee todo lo que se ha guardado y se lo muestra al usuario.
def mostrar_historial():
    # Si la lista de memoria no tiene nada adentro, el programa avisa que está vacía.
    if len(historial) == 0:
        print("Historial vacio")
    else:
        print("Historial de operaciones:")
        # Repasamos operación por operación, poniéndoles un número al lado para que sea fácil leerlas.
        for indice, operacion in enumerate(historial):
            # Imprimimos el número de orden y luego el detalle de la cuenta matemática.
            print(f"{indice + 1}. {operacion}")
        # Dejamos un renglón en blanco al final para que la pantalla se vea ordenada.
        print()


# ============================================================================
# SECCIÓN 6: PANTALLAS DE OPCIONES PARA EL USUARIO
# ============================================================================

# Esta parte maneja las opciones de suma, resta, multiplicación y división.
def menu_operaciones_basicas():
    # Creamos un interruptor encendido para que el menú se repita constantemente hasta que el usuario decida salir.
    continuar = True
    while continuar:
        # Mostramos las opciones en pantalla.
        print("Operaciones basicas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Potencia")
        print("6. Volver al menu principal")
        
        # Le pedimos al usuario que escriba un número para elegir.
        opcion_str = input("Seleccione una operacion: ")
        # Mandamos lo que escribió a nuestro sistema de seguridad. Si puso letras o símbolos, bloqueamos la acción.
        if not es_numero_valido(opcion_str, "int"):
            print("Entrada invalida.")
            # Obligamos al programa a detenerse y mostrar el menú otra vez.
            continue
            
        # Como pasó la prueba de seguridad, transformamos el texto en un número de verdad.
        opcion = int(opcion_str)
        
        # Si eligió 1, activamos la rutina de sumar.
        if opcion == 1:
            # Pedimos el primer número de la cuenta.
            num1_str = input("Ingrese el primer numero: ")
            # Revisamos que no intente ingresar texto.
            if not es_numero_valido(num1_str, "float"):
                print("Dato invalido.")
                continue
            # Pedimos el segundo número.
            num2_str = input("Ingrese el segundo numero: ")
            # Revisamos la seguridad de nuevo.
            if not es_numero_valido(num2_str, "float"):
                print("Dato invalido.")
                continue
                
            # Convertimos los textos en números con decimales que la calculadora pueda sumar.
            num1 = float(num1_str)
            num2 = float(num2_str)
            # Le pedimos al programa que haga la suma real.
            resultado = sumar(num1, num2)
            # Mostramos el resultado armando una frase clara.
            print(f"Resultado: {num1} + {num2} = {resultado}")
            # Escribimos un resumen de esta cuenta y lo guardamos en la memoria principal.
            historial.append(f"Suma: {num1} + {num2} = {resultado}")
        
        # Si eligió 2, seguimos los mismos pasos de seguridad pero para restar.
        elif opcion == 2:
            num1_str = input("Ingrese el primer numero: ")
            if not es_numero_valido(num1_str, "float"):
                print("Dato invalido.")
                continue
            num2_str = input("Ingrese el segundo numero: ")
            if not es_numero_valido(num2_str, "float"):
                print("Dato invalido.")
                continue
                
            num1 = float(num1_str)
            num2 = float(num2_str)
            # Llamamos a la herramienta matemática encargada de restar.
            resultado = restar(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
            historial.append(f"Resta: {num1} - {num2} = {resultado}")
        
        # Si eligió 3, preparamos la multiplicación.
        elif opcion == 3:
            num1_str = input("Ingrese el primer numero: ")
            if not es_numero_valido(num1_str, "float"):
                print("Dato invalido.")
                continue
            num2_str = input("Ingrese el segundo numero: ")
            if not es_numero_valido(num2_str, "float"):
                print("Dato invalido.")
                continue
                
            num1 = float(num1_str)
            num2 = float(num2_str)
            # El programa multiplica los dos valores confirmados.
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
            historial.append(f"Multiplicacion: {num1} * {num2} = {resultado}")
        
        # Si eligió 4, toca pedir los números para dividir.
        elif opcion == 4:
            num1_str = input("Ingrese el dividendo: ")
            if not es_numero_valido(num1_str, "float"):
                print("Dato invalido.")
                continue
            # Pedimos el número que va a partir al primero.
            num2_str = input("Ingrese el divisor: ")
            if not es_numero_valido(num2_str, "float"):
                print("Dato invalido.")
                continue
                
            num1 = float(num1_str)
            num2 = float(num2_str)
            # Entregamos los números limpios al bloque que sabe dividir.
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
            historial.append(f"Division: {num1} / {num2} = {resultado}")
        
        # Si eligió 5, configuramos el cálculo de potencia.
        elif opcion == 5:
            base_str = input("Ingrese la base: ")
            if not es_numero_valido(base_str, "float"):
                print("Dato invalido.")
                continue
            # Aquí es distinto, pedimos que el exponente obligatoriamente sea entero porque nuestra fórmula no maneja decimales.
            exponente_str = input("Ingrese el exponente: ")
            # Por eso usamos "int" en la revisión de seguridad.
            if not es_numero_valido(exponente_str, "int"):
                print("Dato invalido.")
                continue
                
            base = float(base_str)
            exponente = int(exponente_str)
            # Calculamos cuántas veces se multiplicará el número base.
            resultado = potencia(base, exponente)
            print(f"Resultado: {base} ^ {exponente} = {resultado}")
            historial.append(f"Potencia: {base} ^ {exponente} = {resultado}")
        
        # Si eligió 6, significa que quiere salir de este menú.
        elif opcion == 6:
            # Apagamos el interruptor que mantenía el menú funcionando.
            continuar = False
            print("Volviendo...")
        
        # Si escribió un número que no está entre el 1 y el 6, le avisamos.
        else:
            print("Opcion no valida.")

# Esta parte muestra y controla las operaciones matemáticas complejas.
def menu_operaciones_cientificas():
    # Volvemos a encender un interruptor para que este menú trabaje sin detenerse.
    continuar = True
    while continuar:
        # Imprimimos la lista de opciones científicas en pantalla.
        print("Operaciones cientificas")
        print("1. Factorial")
        print("2. Raiz cuadrada")
        print("3. Exponencial (e^x)")
        print("4. Seno (angulo en radianes)")
        print("5. Coseno (angulo en radianes)")
        print("6. Logaritmo natural")
        print("7. Volver al menu principal")
        
        # Esperamos a que el usuario digite su decisión.
        opcion_str = input("Seleccione una operacion cientifica: ")
        # Mandamos el texto al filtro para evitar que el programa se cuelgue si ingresan letras.
        if not es_numero_valido(opcion_str, "int"):
            print("Entrada invalida.")
            continue
            
        opcion = int(opcion_str)
        
        # Opcion 1: Iniciar el cálculo factorial.
        if opcion == 1:
            # Requerimos un número sin decimales porque el factorial no existe para partes fraccionadas.
            numero_str = input("Ingrese un numero entero: ")
            # Revisamos estrictamente bajo la regla "int" (entero).
            if not es_numero_valido(numero_str, "int"):
                print("Dato invalido.")
                continue
            numero = int(numero_str)
            # Mandamos el número limpio a la función encargada.
            resultado = factorial(numero)
            print(f"Factorial de {numero} = {resultado}")
            # Guardamos la cuenta final para que se pueda consultar después.
            historial.append(f"Factorial: {numero}! = {resultado}")
        
        # Opción 2: Buscar la raíz cuadrada.
        elif opcion == 2:
            numero_str = input("Ingrese un numero: ")
            if not es_numero_valido(numero_str, "float"):
                print("Dato invalido.")
                continue
            numero = float(numero_str)
            # Ordenamos al algoritmo que empiece a adivinar la raíz.
            resultado = raiz_cuadrada(numero)
            print(f"Raiz cuadrada de {numero} = {resultado}")
            historial.append(f"Raiz cuadrada: √{numero} = {resultado}")
        
        # Opción 3: Ejecutar la fórmula euleriana.
        elif opcion == 3:
            numero_str = input("Ingrese el exponente: ")
            if not es_numero_valido(numero_str, "float"):
                print("Dato invalido.")
                continue
            numero = float(numero_str)
            # Ponemos a sumar las fracciones del algoritmo exponencial.
            resultado = exponencial(numero)
            print(f"e^{numero} = {resultado}")
            historial.append(f"Exponencial: e^{numero} = {resultado}")
        
        # Opción 4: Analizar la onda del seno.
        elif opcion == 4:
            numero_str = input("Ingrese el angulo en radianes: ")
            if not es_numero_valido(numero_str, "float"):
                print("Dato invalido.")
                continue
            numero = float(numero_str)
            # Enviamos los grados para su procesamiento en la serie matemática.
            resultado = seno(numero)
            print(f"Seno({numero} rad) = {resultado}")
            historial.append(f"Seno: sen({numero} rad) = {resultado}")
        
        # Opción 5: Calcular el coseno.
        elif opcion == 5:
            numero_str = input("Ingrese el angulo en radianes: ")
            if not es_numero_valido(numero_str, "float"):
                print("Dato invalido.")
                continue
            numero = float(numero_str)
            # El programa calcula las distancias del coseno mediante correcciones seguidas.
            resultado = coseno(numero)
            print(f"Coseno({numero} rad) = {resultado}")
            historial.append(f"Coseno: cos({numero} rad) = {resultado}")
        
        # Opción 6: Encontrar el logaritmo.
        elif opcion == 6:
            numero_str = input("Ingrese un numero: ")
            if not es_numero_valido(numero_str, "float"):
                print("Dato invalido.")
                continue
            numero = float(numero_str)
            # Ejecutamos la reducción logarítmica.
            resultado = logaritmo_natural(numero)
            print(f"Logaritmo natural de {numero} = {resultado}")
            historial.append(f"Logaritmo natural: ln({numero}) = {resultado}")
        
        # Opción 7: Retirada.
        elif opcion == 7:
            # Rompemos el ciclo apagando la señal de continuación.
            continuar = False
            print("Volviendo...")
        
        # Respuesta para elecciones fuera del menú.
        else:
            print("Opcion no valida.")

# Esta sección permite al usuario probar fórmulas completas cambiando el valor de X.
def menu_evaluar_funcion():
    # Creamos un ciclo infinito, el programa solo saldrá si el usuario elige la opción 0.
    while True:
        # Cargamos el archivo interno que tiene las fórmulas.
        funciones = evaluar_funcion(0)
        print("Evaluar funcion")
        # Listamos en pantalla los nombres de las fórmulas disponibles numerándolas una por una.
        for i, nombre_funcion in enumerate(funciones.keys()):
            print(f"{i + 1}. {nombre_funcion}")
        
        # Pedimos el número de la fórmula que quiere probar.
        seleccion_str = input("Seleccione una funcion o 0 para volver: ")
        # Escaneamos posibles errores tipográficos del usuario.
        if not es_numero_valido(seleccion_str, "int"):
            print("Entrada invalida.")
            continue
            
        seleccion = int(seleccion_str)
        # Si digita el 0, destruimos el ciclo y regresamos a la pantalla principal.
        if seleccion == 0:
            return
            
        # Convertimos las opciones de fórmulas en una lista que se pueda leer por posición (primero, segundo, tercero).
        lista_funciones = list(funciones.keys())
        # Evitamos que el usuario escoja un número mayor a las opciones que existen.
        if seleccion < 1 or seleccion > len(lista_funciones):
            print("Opcion no valida.")
            continue
        
        # Rescatamos el nombre exacto de la fórmula que eligió buscando en la lista.
        nombre_funcion = lista_funciones[seleccion - 1]
        # Sacamos la instrucción matemática asociada a ese nombre.
        funcion = funciones[nombre_funcion]
        
        # Preguntamos qué número quiere meter dentro de la fórmula.
        x_str = input("Ingrese el valor de x: ")
        if not es_numero_valido(x_str, "float"):
            print("Entrada invalida.")
            continue
            
        x = float(x_str)
        # El programa inyecta el número del usuario adentro de la fórmula y resuelve la ecuación.
        resultado = funcion(x)
        # Mostramos en pantalla cómo quedó el cálculo completo.
        print(f"f({x}) = {resultado}")
        # Guardamos todo el suceso como registro en memoria.
        historial.append(f"Funcion {nombre_funcion}: f({x}) = {resultado}")
        # Terminamos el trabajo rompiendo el menú.
        break

# En este apartado se agrupan las órdenes previas para poder pintar la gráfica.
def menu_graficar_funcion():
    # Establecemos el funcionamiento cíclico para retener al usuario.
    while True:
        # Extraemos de nuevo el diccionario de fórmulas.
        funciones = evaluar_funcion(0)
        print("Graficar funcion")
        # Mostramos qué curvas matemáticas podemos dibujar.
        for i, nombre_funcion in enumerate(funciones.keys()):
            print(f"{i + 1}. {nombre_funcion}")
        
        # Atrapamos la instrucción que el usuario digita.
        seleccion_str = input("Seleccione una funcion o 0 para volver: ")
        # Evitamos daños en el código revisando el texto.
        if not es_numero_valido(seleccion_str, "int"):
            print("Entrada invalida.")
            continue
            
        seleccion = int(seleccion_str)
        # Puerta de salida trasera por si se arrepiente.
        if seleccion == 0:
            return
            
        lista_funciones = list(funciones.keys())
        # Cerco de protección numérico frente a rangos irreales.
        if seleccion < 1 or seleccion > len(lista_funciones):
            print("Opcion no valida.")
            continue
        
        # Obtenemos la referencia al motor de cálculo correcto.
        nombre_funcion = lista_funciones[seleccion - 1]
        
        # Preguntamos desde dónde en la línea de números (eje X) empezamos a medir.
        rango_inicio_str = input("Ingrese el inicio del rango: ")
        if not es_numero_valido(rango_inicio_str, "float"):
            print("Entrada invalida.")
            continue
            
        # Preguntamos en dónde terminamos el análisis visual.
        rango_fin_str = input("Ingrese el fin del rango: ")
        if not es_numero_valido(rango_fin_str, "float"):
            print("Entrada invalida.")
            continue
            
        # Averiguamos de cuántos renglones quiere el usuario que sea su dibujo (la altura).
        altura_str = input("Ingrese la altura de la grafica: ")
        # Esto tiene que ser un número entero sin puntos decimales, no se pueden hacer mitades de renglones en texto.
        if not es_numero_valido(altura_str, "int"):
            print("Entrada invalida.")
            continue
            
        rango_inicio = float(rango_inicio_str)
        rango_fin = float(rango_fin_str)
        altura = int(altura_str)
        
        # Entregamos todas las medidas validadas al sector encargado de pintar la pantalla.
        graficar_funcion(nombre_funcion, rango_inicio, rango_fin, altura)
        # Aseguramos el comprobante del gráfico en el arreglo principal.
        historial.append(f"Grafica: {nombre_funcion} de {rango_inicio} a {rango_fin}")
        # Salida exitosa hacia el punto anterior.
        break

# Este es el corazón operativo del programa que conecta y organiza todos los menús.
def main():
    # Inicializamos una variable para que el ciclo despierte.
    opcion = 0
    # El corazón late continuamente a menos que el usuario seleccione el botón número 6.
    while opcion != 6:
        # Mostramos la placa principal del programa según los requisitos del trabajo.
        print("CALCULADORA CIENTIFICA GRAFICADORA")
        print("1. Operaciones basicas")
        print("2. Operaciones cientificas")
        print("3. Evaluar funcion")
        print("4. Graficar funcion")
        print("5. Ver historial")
        print("6. Salir")
        
        # Esperamos la orden global del director de sistema.
        opcion_str = input("Seleccione una opcion: ")
        # Evaluamos el input para que no reviente el menú principal de entrada.
        if not es_numero_valido(opcion_str, "int"):
            print("Opcion no valida")
            continue
            
        # Consolidamos el valor limpio en formato manejable.
        opcion = int(opcion_str)
        
        # Si toca el 1, desviamos el flujo de trabajo hacia la calculadora estándar.
        if opcion == 1:
            menu_operaciones_basicas()
        # Si toca el 2, conectamos con los algoritmos complejos.
        elif opcion == 2:
            menu_operaciones_cientificas()
        # Si presiona el 3, abrimos el menú de pruebas analíticas.
        elif opcion == 3:
            menu_evaluar_funcion()
        # Si el comando es 4, enlazamos al motor gráfico matricial.
        elif opcion == 4:
            menu_graficar_funcion()
        # Con el 5, leemos en pantalla todo lo archivado en memoria.
        elif opcion == 5:
            mostrar_historial()
        # Si introduce el 6, despedimos limpiamente al usuario apagando el sistema.
        elif opcion == 6:
            print("Fin del programa")
        # Si introduce el 7, 8 o 20, le avisamos que debe usar botones reales.
        else:
            print("Opcion no valida")

# Esta es la puerta principal secreta de Python. Asegura que el código de la calculadora se corra y despierte si alguien abre este archivo directamente.
if __name__ == "__main__":
    main()