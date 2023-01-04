from tkinter import *
from tkinter import ttk


janela = Tk()

janela.title("Paned Window")
janela.geometry("500x400")


panel1 = PanedWindow(bd=4, relief='raised', bg="red")
panel1.place(relx=0.001, rely=0.001, relheight=1, relwidth=1)
left_label = Label(panel1, text = "Painel Esquerdo")
panel1.add(left_label)

panel2 = PanedWindow(panel1,orient=VERTICAL ,bd=4, relief='raised', bg="red")
panel2.place(relx=0.001, rely=0.001, relheight=0.4, relwidth=0.4)

panel1.add(panel2)


top = Label(panel2, text = "Top")
panel2.add(top)


bottom = Label(panel2, text="Bottom")
panel2.add(bottom)

bt_save = Button(panel2,text="Salvar", foreground="yellow", background="blue", height=30, width=50)
bt_save.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.1)

#panel2.add(bt_save)


janela.mainloop()