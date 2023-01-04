from tkinter import *
from tkinter import ttk
import time


### CRIANDO BARRA DE LOADING ###


def step_progress_bar():
    #progress1.start(10)
    #progress1['value'] = progress1['value'] + 10
    #progress1['value'] = 10
    for x in range(10):
        progress1['value'] += 10
        janela.update_idletasks()
        time.sleep(1)


def stop():
    progress1.stop()


janela = Tk()
janela.title("Progress Bar")

janela.geometry("1200x720")

#progress1 = ttk.Progressbar(janela, orient=HORIZONTAL, length=300, mode='indeterminate')
progress1 = ttk.Progressbar(janela, orient=HORIZONTAL, length=300, mode='determinate')
progress1.place(relx=0.2, rely=0.2)


botao = Button(janela, text="Progresso", command=step_progress_bar)
botao.place(relx=0.27, rely=0.25)

botao2 = Button(janela, text="Parar", command=stop)
botao2.place(relx=0.27, rely=0.32)


janela.mainloop()