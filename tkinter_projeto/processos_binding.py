
#PROCESSOS DE BIND: INTERAÇÕES QUE TEMOS COM A TELA. COMO OS BOTÕES SERÃO ACIONADOS, ETC.

from tkinter import *
from tkinter import ttk



janela = Tk()

janela.geometry("1200x720")


label = ttk.Label(janela, text="Começando...", background="gold")
label.place(relx=0.2, rely=0.2, relwidth=0.7, relheight=0.3)
label.bind('<Enter>', lambda e: label.configure(text="Movido o mouse para dentro"))
label.bind("<Leave>", lambda e: label.configure(text="Movido o mouse para fora"))
label.bind("<1>", lambda e: label.configure(text="Clicou com o botão esquerdo do mouse em %d, %d" % (e.x, e.y)))
label.bind("<Double-1>", lambda e: label.configure(text="Clicou duas vezes com o mouse para %d, %d" %(e.x, e.y)))
label.bind("<B3-Motion>", lambda e: label.configure(text= "Arraste o botão \n direito para %d, %d" % (e.x, e.y)))


janela.mainloop()