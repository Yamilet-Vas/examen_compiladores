import tkinter as tk
import ply.lex as lex

tokens = ('PALABRA_R','IDENTIFICADOR','SIMBOLO','OPERADOR','NUMERO','FINAL', 'NOESTADEFINIDO')

palabra_reser = ['base', 'altura', 'Area']
identificador = ['yamilet', 'Octubre']
operador = ['*', '/']

t_ignore = ' \t'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in palabra_reser:
        t.type = 'PALABRA_R'
    elif t.value in identificador:
        t.type = 'IDENTIFICADOR'
    else:
        t.type = "NOESTADEFINIDO"
    return t

def t_OPERADOR(t):
    r'[\*\)\/]'
    t.type = 'OPERADOR'
    return t

def t_SIMBOLO(t):
    r'[\(\)\=]'
    t.type = 'SIMBOLO'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.type = 'NUMERO'
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
ventana.geometry('1000x1000')
ventana.title("Analizador Lexico YCVS_A210601")
ventana.config(bg='#9e8fda')

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=8, width=50)
entrada_texto.place(x=100, y=70)

texto_token = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_token.place(x=100, y=270)
texto_lexema = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_lexema.place(x=250, y=270)
texto_linea = tk.Text(ventana, font=("Arial", 12), bg="#90a6da", fg="purple", height=20, width=17)
texto_linea.place(x=400, y=270)


titulo_salida = tk.Label(ventana, text="Token                 Lexema                Linea", font=("Arial", 14), bg='#da8fa5', fg='black')
titulo_salida.place(x=150, y=230)

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_codigo)
boton_analizar.place(x=160, y=30)
boton_borrar = tk.Button(ventana, text=" Eliminar ", command=borrar_contenido)
boton_borrar.place(x=440, y=30)

ventana.mainloop()