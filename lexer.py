import sys
import ply.lex as lex
from tabulate import tabulate
# Alejandro Ortega, Nicole Rios, Jhon Edison Parra

# https://www.dabeaz.com/ply/ply.html#ply_nn6
reserved = {
    #Las palabras reservadas
    'if': 'IF',
    'print'  : 'PRINT',
    'else' : 'ELSE',
}

tokens = list(reserved.values()) + [
    #Los tokens
    'SUMA',
    'IGUALDAD',
    'CONDICIONALES',
    'MENOS',
    'MULTIPLICAR',
    'DIVISION',
    'MENOSQUE',
    'MENOSOIGUAL',
    'MAYORQUE',
    'MAYOROIGUAL',
    'IGUAL',
    'DOBLEPUNTO',
    'PARENTESISIZ',
    'PARENTESISDE',
    'CORCHETEIZ',
    'CORCHETEDE',
    'LBLOCK',
    'RBLOCK',
    'COMA',
    'PUNTO',
    'COMILLASIMPLE',
    'COMILLASDOBLES',


    # variables

    # Others
    'VARIABLE',
    'NUMEROENT',
    'NUMERODEC',
    'CADENA1',
    'EXPRESIONESARITMETICAS',
]

# Expresiones regulares para los tokens simples
t_SUMA = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_IGUALDAD = r'=='
t_MENOSQUE = r'<'
t_MAYORQUE = r'>'
t_COMA = r','
t_PARENTESISIZ = r'\('
t_PARENTESISDE = r'\)'
t_CORCHETEIZ = r'\['
t_CORCHETEDE = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_DOBLEPUNTO = r':'
t_PUNTO = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'


def t_CONDICIONALES(t):
    r'([a-zA-Z]([\w])*)\s?([<|>])\s?([a-zA-Z]([\w])*)'
    return t

def t_EXPRESIONESARITMETICAS(t):
    r'([a-zA-Z]([\w])*)[-|+|/|*]([a-zA-Z]([\w])*)'
    return t


def t_CADENAVACIA(t):
    r'\[]'
    return t


def t_NUMEROENT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERODEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        return t
# El if verifica que no sea una palabra reservada

def t_CADENA1(t):
    r'\'([a-zA-Z,\d*,\s*]+)\''
    return t

def t_MENOSOIGUAL(t):
    r'<='
    return t

def t_MAYOROIGUAL(t):
    r'>='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMENTARIOENLINEAS(t):
    r'\'\'\'(\'?([a-zA-Z,\d*,\s*]+)\'?)\n*\'\'\''
    #r'([\{,\-]\s*[a-zA-Z]\s*[\w]*[\-,\}])'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIOSENLINEA(t):
    r'\#(\'?([a-zA-Z,\d*,\s*]+)\'?)\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Lexical error: " + str(t.value))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        res=[[str(i),str(tok.lineno),str(tok.type),str(tok.value)]]
        print(tabulate(res,headers=["Linea", "Linea del código", "Token", "Resultado"], tablefmt="fancy_grid"))
        #print(tabulate(rios3, headers='firstrow', tablefmt='fancy_grid'))
        #print("\t" + str(i) + " - " + "Line: " + str(tok.lineno) + "\t" + str(tok.type) + "\t-->  " + str(tok.value))
        i += 1
        # print(tok)


lexer = lex.lex()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        fin = 'prueba.py'
    else:
        fin = sys.argv[1]
    f = open(fin, 'r')
    data = f.read()
    # print (data)
    # lexer.input(data)
    test(data, lexer)
# input()