from tkinter import *
from tkinter import ttk

def atualizalabel():
    global valor
    label.config(text=valor)
    
def insere(num):
    global valor
    if num == "CE":
        valor = ""
        print("\ncálculo apagado!")
    else:
        if "ERRO" in valor:
            valor =""    
        valor+=num
        print("\nvalor sendo inserido: "+num)
        print("valor na label será: "+valor)
        
    atualizalabel()
    
def calcular():
    global valor
    try:
        valor = valor.lstrip('0') #limpa zeros iniciais
        valor = eval(valor)
        if valor % 1 == 0: 
            valor = int(valor) 
        valor = str(valor)
        print("\nresultado:"+valor)
    except SyntaxError:
        valor = "ERRO, TENTE NOVAMENTE"
    except ZeroDivisionError:
        valor = "ERRO, DIVISÃO POR ZERO"
        
    atualizalabel()

root = Tk()
root.resizable(False, False)
frm = ttk.Frame(root, padding=0)
frm.grid()

valor = ""

#interface
root.title("Calculadora")
ttk.Label(text="Calculadora by Dankrutov").grid(sticky = W, columnspan=2, row=0)

label = ttk.Label(text="",font="bold", borderwidth=2, relief="solid", width = 25,anchor="e")
label.grid(sticky = E, columnspan=3, row=1)

ttk.Button(text="1", command= lambda: insere("1")).grid(column=0, row=2)
ttk.Button(text="2", command= lambda: insere("2")).grid(column=1, row=2)
ttk.Button(text="3", command= lambda: insere("3")).grid(column=2, row=2)

ttk.Button(text="4", command= lambda: insere("4")).grid(column=0, row=3)
ttk.Button(text="5", command= lambda: insere("5")).grid(column=1, row=3)
ttk.Button(text="6", command= lambda: insere("6")).grid(column=2, row=3)

ttk.Button(text="7", command= lambda: insere("7")).grid(column=0, row=4)
ttk.Button(text="8", command= lambda: insere("8")).grid(column=1, row=4)
ttk.Button(text="9", command= lambda: insere("9")).grid(column=2, row=4)

ttk.Button(text="0", command= lambda: insere("0")).grid(column=1, row=5)

ttk.Button(text=".", command= lambda: insere(".")).grid(column=0, row=6)
ttk.Button(text="*", command= lambda: insere("*")).grid(column=1, row=6)
ttk.Button(text="/", command= lambda: insere("/")).grid(column=2, row=6)

ttk.Button(text="%", command= lambda: insere("%")).grid(column=0, row=7)
ttk.Button(text="-", command= lambda: insere("-")).grid(column=1, row=7)
ttk.Button(text="+", command= lambda: insere("+")).grid(column=2, row=7)

ttk.Button(text="CE", width = 24, command= lambda: insere("CE")).grid(columnspan=2, row=8)
ttk.Button(text="=", command= lambda: calcular()).grid(column=2, row=8)

root.mainloop()