
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION BUCLE_FOR BUCLE_WHILE CADENA CARACTER CARACTER_ERROR COLON COMA COMENTARIOS COMENTARIO_BLOQUE CORCHETE_DERECHO CORCHETE_IZQUIERDO DECREMENTO DISTINTO DIVI_RESULTADO ENTERO_SOBREPASADO IGUAL INCREMENTO LINEAS LLAVE_DER LLAVE_IZQ MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MULTI_RESULTADO NUMERO_DECIMAL NUMERO_DECIMAL_CON_ERROR NUMERO_DECIMAL_CON_ERROR2 NUMERO_ENTERO OPERADOR_DIVIDIR OPERADOR_MODULO OPERADOR_MULTIPLICAR OPERADOR_RESTA OPERADOR_SUMA OP_TERNARIO PALABRA_RESERVADA_AND PALABRA_RESERVADA_BOOL PALABRA_RESERVADA_BREAK PALABRA_RESERVADA_BY PALABRA_RESERVADA_DO PALABRA_RESERVADA_ELSE PALABRA_RESERVADA_FALSE PALABRA_RESERVADA_IF PALABRA_RESERVADA_MAIN PALABRA_RESERVADA_NOT PALABRA_RESERVADA_NULL PALABRA_RESERVADA_OR PALABRA_RESERVADA_RETURN PALABRA_RESERVADA_STATIC PALABRA_RESERVADA_THEN PALABRA_RESERVADA_TO PALABRA_RESERVADA_TRUE PARENTESIS_DERECHO PARENTESIS_IZQUIERDO PUNTOS_MAYOR_PUNTOS PUNTOS_MENOR_PUNTOS PUNTO_Y_COMA RESTA_RESULTADO SUMA_RESULTADO TIPO_CARACTER TIPO_DECIMAL TIPO_ENTERO VARIABLE VARIABLE_ERRORD : T LT : PALABRA_RESERVADA_BOOL\n         | TIPO_CARACTERL : VARIABLE LPLP : COMA VARIABLE LP\n          | epseps :'
    
_lr_action_items = {'PALABRA_RESERVADA_BOOL':([0,],[3,]),'TIPO_CARACTER':([0,],[4,]),'$end':([1,5,6,7,9,10,11,],[0,-1,-7,-4,-6,-7,-5,]),'VARIABLE':([2,3,4,8,],[6,-2,-3,10,]),'COMA':([6,10,],[8,8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'D':([0,],[1,]),'T':([0,],[2,]),'L':([2,],[5,]),'LP':([6,10,],[7,11,]),'eps':([6,10,],[9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> D","S'",1,None,None,None),
  ('D -> T L','D',2,'p_D','xd.py',396),
  ('T -> PALABRA_RESERVADA_BOOL','T',1,'p_T','xd.py',399),
  ('T -> TIPO_CARACTER','T',1,'p_T','xd.py',400),
  ('L -> VARIABLE LP','L',2,'p_L','xd.py',403),
  ('LP -> COMA VARIABLE LP','LP',3,'p_LP','xd.py',406),
  ('LP -> eps','LP',1,'p_LP','xd.py',407),
  ('eps -> <empty>','eps',0,'p_eps','xd.py',410),
]