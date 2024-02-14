import tkinter as tk
import ply.lex as lex

tokens = ('Palabra_R','identificador','operador','numero', 'Simbolo')

palabra_reser = ['altura', 'base', 'area']
identificador = ['yamilet', 'cristel', 'octubre']
delimitador = ['(', ')', '{', '}', ';', '.']



def t_identificador(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in palabra_reser:
        t.type = 'Palbra_R'
    elif t.value in identificador:
        t.type = 'identificador'


def t_simbolo(t):
    r'[( )]'
    t.type = 'simbolo'
    return t

def t_operador(t):
    r'[=, *, /]'
    t.type = 'operador'
    return t

def t_numero(t):
    r'\d+(\.\d+)?'
    t.type = 'numero'
    return t

lexer = lex.lex()

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    lineas_codigo = codigo.split("\n")
    tokens = []
    lexemas = []
    lineas = []

    for linea_numero, linea in enumerate(lineas_codigo, start=1):
        lexer.input(linea)
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok.type)
            lexemas.append(tok.value)
            lineas.append(linea_numero)

    texto_token.delete("1.0", tk.END)
    for token in tokens:
        texto_token.insert(tk.END, f"{token}\n")

    texto_lexema.delete("1.0", tk.END)
    for lexema in lexemas:
        texto_lexema.insert(tk.END, f"{lexema}\n")

    texto_linea.delete("1.0", tk.END)
    for linea_numero in lineas:
        texto_linea.insert(tk.END, f"{linea_numero}\n")

def borrar_contenido():
    entrada_texto.delete("1.0", tk.END)
    texto_token.delete("1.0", tk.END)
    texto_lexema.delete("1.0", tk.END)
    texto_linea.delete("1.0", tk.END)

ventana = tk.Tk()
ventana.geometry('400x450')
ventana.title("Analizador Lexico YCVS")
ventana.config(bg='#9e8fda')

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=8, width=50)
entrada_texto.place(x=100, y=70)

texto_token = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_token.place(x=100, y=270)
texto_lexema = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_lexema.place(x=250, y=270)
texto_linea = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_linea.place(x=400, y=270)

titulo_salida = tk.Label(ventana, text="TOKEN                    LEXEMA                   LINEA", font=("Arial", 10), bg='#da8fa5', fg='black')
titulo_salida.place(x=150, y=230)

boton_analizar = tk.Button(ventana, text="ANALIZAR", command=analizar_codigo)
boton_analizar.place(x=160, y=30)
boton_borrar = tk.Button(ventana, text=" ELIMINAR ", command=borrar_contenido)
boton_borrar.place(x=440, y=30)

ventana.mainloop()
