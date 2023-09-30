import ply.lex as lex
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
    
)

# Definición de las reglas para los tokens


t_PARENTESIS_IZQUIERDO = r'\(' 

t_PARENTESIS_DERECHO = r'\)'

t_OPERADOR_SUMA = r'\+'

t_OPERADOR_RESTA = r'\-'

t_OPERADOR_MULTIPLICAR = r'\*'

t_OPERADOR_DIVIDIR = r'/'

t_OPERADOR_MODULO = r'\%'


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

def t_BUCLE_FOR(t):
    r'for'
    return t

def t_BUCLE_WHILE(t):
    r'while'
    return t

#funcion variable mal escrita melba

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
    print("Carácter ilegal:", t.value[0])
    t.lexer.skip(1)

# Crear un lexer
lexer = lex.lex()

# Cadena de texto de entrada
entrada = input("Texto: ")

# Asignar la cadena de texto al lexer
lexer.input(entrada)
#variable para contar las lineas
contado_de_lineas = 0

# Obtener tokens
while True:
    token = lexer.token()
    if not token:
        break  # No hay más tokens
    #IMPRESION DE TOKENS
    if token.type == "LINEAS":
        contado_de_lineas += 1#cada vez que lee una linea sumamos la variable contador_de_lineas
    if token.type == "TIPO_ENTERO":
        print("TIPO_ENTERO:", token.value)
    if token.type == "TIPO_DECIMAL":
        print("TIPO_DECIMAL:", token.value)
    if token.type == "TIPO_CARACTER":
        print("TIPO_CARACTER:", token.value)
    if token.type == "NUMERO_ENTERO":
        print("NUMERO_ENTERO:", token.value)
    if token.type == "NUMERO_DECIMAL":
        print("NUMERO_DECIMAL:", token.value)
    if token.type == "VARIABLE":
        print("VARIABLE:", token.value)
    if token.type == "BUCLE_FOR":
        print("BUCLE_FOR:", token.value)
    if token.type == "BUCLE_WHILE":
        print("BUCLE_WHILE:", token.value)
    if token.type == "PARENTESIS_IZQUIERDO":
        print("PARENTESIS_IZQUIERDO:", token.value)
    if token.type == "PARENTESIS_DERECHO":
        print("PARENTESIS_DERECHO:", token.value)
    if token.type == "PALABRA_RESERVADA_RETURN":
        print("PALABRA_RESERVADA_RETURN:", token.value)
    if token.type == "PALABRA_RESERVADA_BREAK":
        print("PALABRA_RESERVADA_BREAK:", token.value)
    if token.type == "OPERADOR_SUMA":
        print("OPERADOR_SUMA:", token.value)
    if token.type == "OPERADOR_RESTA":
        print("OPERADOR_RESTA:", token.value)
    if token.type == "OPERADOR_MULTIPLICAR":
        print("OPERADOR_MULTIPLICAR:", token.value)
    if token.type == "OPERADOR_DIVIDIR":
        print("OPERADOR_DIVIDIR:", token.value)
    if token.type == "OPERADOR_MODULO":
        print("OPERADOR_MODULO:", token.value)
    if token.type == "NUMERO_DECIMAL_CON_ERROR":
        print("DECIMAL_MAL_ESCRITO:", token.value)
    if token.type == "NUMERO_DECIMAL_CON_ERROR2":
        print("DECIMAL_MAL_ESCRITO:", token.value)
    
    
    