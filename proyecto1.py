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
    'ENTERO_SOBREPASADO',
    "TIPO_ENTERO",
    "TIPO_DECIMAL",
    "TIPO_CARACTER",
    "NUMERO_ENTERO",
    "LINEAS",
    "NUMERO_DECIMAL",
    'PALABRA_RESERVADA_STATIC',
    'PALABRA_RESERVADA_BOOL',
    'PALABRA_RESERVADA_IF',
    'PALABRA_RESERVADA_THEN',
    'PALABRA_RESERVADA_ELSE',
    'PALABRA_RESERVADA_DO',
    'PALABRA_RESERVADA_TO',
    'PALABRA_RESERVADA_BY',
    'PALABRA_RESERVADA_OR',
    'PALABRA_RESERVADA_AND',
    'PALABRA_RESERVADA_NOT',
    'PALABRA_RESERVADA_TRUE',
    'PALABRA_RESERVADA_FALSE',
    'PALABRA_RESERVADA_NULL',
    'SUMA_RESULTADO',
    'RESTA_RESULTADO',
    'MULTI_RESULTADO',
    'DIVI_RESULTADO',
    'INCREMENTO',
    'DECREMENTO',
    'OP_TERNARIO',
    'ASIGNACION',
    'COLON',
    'MENOR',
    'MENOR_IGUAL',
    'MAYOR',
    'MAYOR_IGUAL',
    'IGUAL',
    'DISTINTO',
    'PUNTOS_MAYOR_PUNTOS',
    'PUNTOS_MENOR_PUNTOS',
    'LLAVE_IZQ',
    'LLAVE_DER',
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
    "COMA",
    "CARACTER",
    "CARACTER_ERROR",
    "CADENA",
    'COMENTARIO_BLOQUE',   
)

# Definición de las reglas para los tokens
lista_de_tokens = []

t_PARENTESIS_IZQUIERDO = r'\(' 

t_PARENTESIS_DERECHO = r'\)'

t_OPERADOR_SUMA = r'\+'

t_OPERADOR_RESTA = r'\-'

t_OPERADOR_MULTIPLICAR = r'\*'

t_OPERADOR_MODULO = r'\%'

t_PUNTO_Y_COMA = r';'

t_CORCHETE_IZQUIERDO = r'\['

t_CORCHETE_DERECHO = r'\]'

t_LLAVE_IZQ = r'\{'

t_LLAVE_DER = r'\}'

t_COMA = r'\,'

def t_COMENTARIO_BLOQUE(t):
    r'/\*(.|\n)*?\*/'
    return t #Aquí debería haber un pass para que simplemente ignore los comentarios de bloque.

# Palabras reservadas
def t_PALABRA_RESERVADA_STATIC(t):
    r'static'
    return t

def t_PALABRA_RESERVADA_BOOL(t):
    r'bool'
    return t

def t_PALABRA_RESERVADA_IF(t):
    r'if'
    return t

def t_PALABRA_RESERVADA_THEN(t):
    r'then'
    return t

def t_PALABRA_RESERVADA_ELSE(t):
    r'else'
    return t

def t_PALABRA_RESERVADA_DO(t):
    r'do'
    return t

def t_PALABRA_RESERVADA_TO(t):
    r'to'
    return t

def t_PALABRA_RESERVADA_BY(t):
    r'by'
    return t

def t_PALABRA_RESERVADA_OR(t):
    r'or'
    return t

def t_PALABRA_RESERVADA_AND(t):
    r'and'
    return t

def t_PALABRA_RESERVADA_NOT(t):
    r'not'
    return t

def t_PALABRA_RESERVADA_TRUE(t):
    r'true'
    return t

def t_PALABRA_RESERVADA_FALSE(t):
    r'false'
    return t

def t_PALABRA_RESERVADA_NULL(t):
    r'null'
    return t

# Alteraciones al resultado.

def t_SUMA_RESULTADO(t):
    r'\+='
    return t

def t_RESTA_RESULTADO(t):
    r'-='
    return t

def t_MULTI_RESULTADO(t):
    r'\*='
    return t

def t_DIVI_RESULTADO(t):
    r'/='
    return t

def t_INCREMENTO(t):
    r'\+\+'
    return t

def t_DECREMENTO(t):
    r'--'
    return t

def t_ASIGNACION(t):
    r'='
    return t

# Operadores.

def t_OP_TERNARIO(t):
    r'\?'
    return t

def t_COLON(t):
    r':'
    return t

# Lógicos

def t_MENOR(t):
    r'<'
    return t

def t_MENOR_IGUAL(t):
    r'<='
    return t

def t_MAYOR(t):
    r'>'
    return t

def t_MAYOR_IGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_PUNTOS_MAYOR_PUNTOS(t):
    r':>:'
    return t

def t_PUNTOS_MENOR_PUNTOS(t):
    r':>:'
    return t

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
    return t #Debería ser pass para que no los tome en cuenta.

def t_OPERADOR_DIVIDIR(t):
    r'/'
    return t

def t_CARACTER_ERROR(t):#encontrar caracteres con error como 'hola'
    r'\'[a-zA-Z0-9][a-zA-Z0-9]+\''
    return t

def t_CADENA(t):
    r'\"[a-zA-Z0-9_][a-zA-Z0-9_]*\"'
    return t

def t_CARACTER(t): #econtrar caracter valido como 'a'
    r'\'[a-zA-Z]\''
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
    try:
        t.value=int(t.value)
        if t.value>=-2147483648 and t.value<=2147483647:
            t.value=int(t.value)
        else:
            print(f'Integer value out of bound {t.value}')
            t.type='ENTERO_SOBREPASADO'
    except ValueError:
        print(f'Error matching value {t.value}')
    return t

#regla para leer las lineas
def t_LINEAS(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"{contado_de_lineas} Caracter ilegal:", t.value[0])
    lista_de_tokens.append(f"{contado_de_lineas} Caracter ilegal: {t.value[0]}")
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

# Obtener tokens
while True:
    token = lexer.token()
    if not token:
        break  # No hay más tokens
    #IMPRESION DE TOKENS
    if token.type == "LINEAS":
        contado_de_lineas += 1#cada vez que lee una linea sumamos la variable contador_de_lineas
    else:
        print(f"{contado_de_lineas} encontre el token {token.type}: ", token.value)
        lista_de_tokens.append(f"{contado_de_lineas} encontre el token {token.type}: {token.value}")   

escribir_archivo(lista_de_tokens)
    
#nota las lineas en blanco de los archivos no los cuenta