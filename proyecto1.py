import ply.lex as lex
def leer_archivo(texto):
    try:
        with open(texto, 'r') as entrada:
            contenido = entrada.read()
            return contenido
    except IOError:
        return print("Archivo no encontrado")

def escribir_archivo(lista):
    with open("salida.txt", 'w') as archivo:
        for i in lista:
            archivo.write(i + '\n')


#el orden en el que se escriben las funciones de las reglas si importa!!!!!!!
# Lista de nombres de tokens
tokens = (
    "TIPO_ENTERO",
    "TIPO_DECIMAL",
    "TIPO_CARACTER",
    "NUMERO_ENTERO",
    "LINEAS",
    "NUMERO_DECIMAL",
    "VARIABLE",
    "BUCLE_FOR",
    "BUCLE_WHILE",
    "PARENTESIS_IZQUIERDO",
    "PARENTESIS_DERECHO",
    "PALABRA_RESERVADA_RETURN",
    "PALABRA_RESERVADA_BREAK",
    "OPERADOR_SUMA",
    "OPERADOR_RESTA",
    "OPERADOR_MULTIPLICAR",
    "OPERADOR_DIVIDIR",
    "OPERADOR_MODULO",
    "NUMERO_DECIMAL_CON_ERROR",
    "NUMERO_DECIMAL_CON_ERROR2",
    "PUNTO_Y_COMA",
    "COMENTARIOS",
    "PALABRA_RESERVADA_MAIN",
    "VARIABLE_ERROR",
    "CORCHETE_IZQUIERDO",
    "CORCHETE_DERECHO",
    "COMA"
    
)

# Definición de las reglas para los tokens


t_PARENTESIS_IZQUIERDO = r'\(' 

t_PARENTESIS_DERECHO = r'\)'

t_OPERADOR_SUMA = r'\+'

t_OPERADOR_RESTA = r'\-'

t_OPERADOR_MULTIPLICAR = r'\*'

t_OPERADOR_MODULO = r'\%'

t_PUNTO_Y_COMA = r';'

t_CORCHETE_IZQUIERDO = r'\['

t_CORCHETE_DERECHO = r'\]'

t_COMA = r'\,'



def t_TIPO_ENTERO(t):
    r'int'
    return t

def t_TIPO_DECIMAL(t):
    r'float'
    return t

def t_TIPO_CARACTER(t):
    r'char'
    return t

def t_PALABRA_RESERVADA_BREAK(t):
    r'break'
    return t


def t_PALABRA_RESERVADA_RETURN(t):
    r'return'
    return t

def t_PALABRA_RESERVADA_MAIN(t):
    r'main'
    return t

def t_BUCLE_FOR(t):
    r'for'
    return t

def t_BUCLE_WHILE(t):
    r'while'
    return t

def t_COMENTARIOS(t):
    r'\/\/[^\n]*'
    return t

def t_OPERADOR_DIVIDIR(t):
    r'/'
    return t

def t_VARIABLE_ERROR(t):
    r'\d+[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value[0].isdigit():
        print("ERROR DE IDENTIFICADOR INICIA CON NUMERO")
    else:
        t_NUMERO_DECIMAL(t.value)
        t_NUMERO_ENTERO(t.value)

def t_VARIABLE(t):#variable bien escrita
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

#regla para el token numero decimal
def t_NUMERO_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convierte el valor del token a un flotante
    return t

def t_NUMERO_DECIMAL_CON_ERROR(t): #atrapa decimales sin numero a la izquierda del punto
    r'\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO_DECIMAL_CON_ERROR2(t):#atrapa decimales sin numero a la derecha del punto
    r'\d+\.'
    t.value = float(t.value)
    return t


# Regla para el token numero entero
def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)  # Convierte el valor del token a un entero
    return t

#regla para leer las lineas
def t_LINEAS(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"{contado_de_lineas} Carácter ilegal:", t.value[0])
    t.lexer.skip(1)

# Crear un lexer
lexer = lex.lex()

#pedir ruta del archivo
texto = input("Ingrese la ruta del archivo: ")
#llamar a la funcion leer archivo y su retorno asignarlo a la variable
contenido = leer_archivo(texto)

# Asignar la cadena de texto al lexer
lexer.input(contenido)
#variable para contar las lineas
global contado_de_lineas
contado_de_lineas = 1
lista_de_tokens = []
# Obtener tokens
while True:
    token = lexer.token()
    if not token:
        break  # No hay más tokens
    #IMPRESION DE TOKENS
    if token.type == "LINEAS":
        contado_de_lineas += 1#cada vez que lee una linea sumamos la variable contador_de_lineas

    if token.type == "TIPO_ENTERO":
        print(f"{contado_de_lineas} encontre el token INT: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token INT: {token.value}")

    if token.type == "TIPO_DECIMAL":
        print(f"{contado_de_lineas} encontre el token FLOAT: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token FLOAT: {token.value}")

    if token.type == "TIPO_CARACTER":
        print(f"{contado_de_lineas} encontre el token CHAR: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token CHAR: {token.value}")

    if token.type == "NUMERO_ENTERO":
        print(f"{contado_de_lineas} encontre el token NUMERO ENTERO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token NUMERO ENTERO: {token.value}")
        
    if token.type == "NUMERO_DECIMAL":
        print(f"{contado_de_lineas} encontre el token NUMERO DECIMAL: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token NUMERO DECIMAL: {token.value} ")

    if token.type == "VARIABLE":
        print(f"{contado_de_lineas} encontre el token VARIABLE: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token VARIABLE: {token.value} ")

    if token.type == "BUCLE_FOR":
        print(f"{contado_de_lineas} encontre el token FOR: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token FOR: {token.value} ")

    if token.type == "BUCLE_WHILE":
        print(f"{contado_de_lineas} encontre el token WHILE: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token WHILE: {token.value} ")

    if token.type == "PARENTESIS_IZQUIERDO":
        print(f"{contado_de_lineas} encontre el token PARENTESIS IZQUIERDO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token PARENTESIS IZQUIERDO: {token.value} ")

    if token.type == "PARENTESIS_DERECHO":
        print(f"{contado_de_lineas} encontre el token PARENTESIS DERECHO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token PARENTESIS DERECHO: {token.value} ")

    if token.type == "PALABRA_RESERVADA_RETURN":
        print(f"{contado_de_lineas} encontre el token RETURN: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token RETURN: {token.value} ")

    if token.type == "PALABRA_RESERVADA_BREAK":
        print(f"{contado_de_lineas} encontre el token BREAK: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token BREAK: {token.value} ")

    if token.type == "OPERADOR_SUMA":
        print(f"{contado_de_lineas} encontre el token SUMA: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token SUMA: {token.value} ")

    if token.type == "OPERADOR_RESTA":
        print(f"{contado_de_lineas} encontre el token RESTA: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token RESTA: {token.value} ")

    if token.type == "OPERADOR_MULTIPLICAR":
        print(f"{contado_de_lineas} encontre el token MULTIPLICAR: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token MULTIPLICAR: {token.value} ")

    if token.type == "OPERADOR_DIVIDIR":
        print(f"{contado_de_lineas} encontre el token DIVIDIR: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token DIVIDIR: {token.value} ")

    if token.type == "OPERADOR_MODULO":
        print(f"{contado_de_lineas} encontre el token MODULO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token MODULO: {token.value} ")

    if token.type == "NUMERO_DECIMAL_CON_ERROR":
        print(f"{contado_de_lineas} encontre el token NUMERO DECIMAL CON ERROR (NULL.DIGITO): ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token NUMERO DECIMAL CON ERROR (NULL.DIGITO): {token.value} ")

    if token.type == "NUMERO_DECIMAL_CON_ERROR2":
        print(f"{contado_de_lineas} encontre el token NUMERO DECIMAL CON ERROR (DIGITO.NULL): ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token NUMERO DECIMAL CON ERROR (DIGITO.NULL): {token.value} ")

    if token.type == "PUNTO_Y_COMA":
        print(f"{contado_de_lineas} encontre el token PUNTO Y COMA: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token PUNTO Y COMA: {token.value} ")

    if token.type == "COMENTARIOS":
        print(f"{contado_de_lineas} encontre el token COMENTARIOS: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token COMENTARIOS: {token.value} ")

    if token.type == "PALABRA_RESERVADA_MAIN":
        print(f"{contado_de_lineas} encontre el token MAIN: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token MAIN: {token.value} ")

    if token.type == "VARIABLE_ERROR":
        print(f"{contado_de_lineas} encontre el token VARIABLE MAL ESCRITA: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token VARIABLE MAL ESCRITA: {token.value} ")

    if token.type == "CORCHETE_IZQUIERDO":
        print(f"{contado_de_lineas} encontre el token CORCHETE IZQUIERDO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token CORCHETE IZQUIERDO: {token.value} ")

    if token.type == "CORCHETE_DERECHO":
        print(f"{contado_de_lineas} encontre el token CORCHETE DERECHO: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token CORCHETE DERECHO: {token.value} ")

    if token.type == "COMA":
        print(f"{contado_de_lineas} encontre el token COMA: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token COMA: {token.value} ")
    
    
escribir_archivo(lista_de_tokens)
    
#nota las lineas en blanco de los archivos no los cuenta