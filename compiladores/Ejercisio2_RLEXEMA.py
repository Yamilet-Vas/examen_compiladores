import re
import ply.lex as lex

rlexema = []

reservada = ( 'CADENA', )
tokens = reservada + ( 'RESERVADAMA','RESERVADAMI')

def t_RESERVADAMA (t):
    r'[for,do,while,if,else,FOR,DO,WHILE,IF,ELSE]+(\w\d)*'
    return t

def t_RESERVADAMI (t) :
    r'[FOR,DO,WHILE,IF,ELSE,FOR,DO,WHILE,IF,ELSE]+(\w\d)*'
    return t

def t_CADENA (t) :
    r'FORA,fora'
    return t

def t_error (t):
    global rlexema 
    estado = "** Token no válido en la línea {:4} no definido {:16} posición {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    rlexema.append (estado)
    t.lexer.skip (1)
def ingreso (data):
    global rlexema

    analizador = lex.lex ()
    analizador.input(data)

    rlexema.clear()
    while True:
        token = analizador.token()
        if not token:
            break
        estado = "** Línea {:4} Tipo {:16} palabra Reservada {:16} Posición {:4}".format(str(token.lineno), str(token.type), str(token.value), str(token.lexpos))
        rlexema.append(estado)
    return rlexema
analizador =lex.lex()

if __name__=='__main_':
    while True:
        data = input ("Ingrese la cadena:")
        ingreso(data)
    print(rlexema)