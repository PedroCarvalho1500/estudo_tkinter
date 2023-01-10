from tkinter import *
from tkinter import ttk


janela = Tk()

h = ttk.Scrollbar(janela, orient=HORIZONTAL)
v = ttk.Scrollbar(janela, orient=VERTICAL)


# O CANVAS É UTILIZADO PARA DESENHAS FIGURAS DENTRO DO TKINTER.
# SCROLLREGION IRÁ HABILITAR AS ÁREAS ONDE O CANVAS PODERÁ ATUAR.
canvas = Canvas(janela, scrollregion=(0,0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
#canvas.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)


h['command'] = canvas.xview
v['command'] = canvas.yview


ttk.Sizegrip(janela).grid(column=1, row=1, sticky=(S,E))
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
h.grid(column=0, row=1, sticky=(W, E))
v.grid(column=1, row=0, sticky=(N, S))


janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

lastx, lasty = 0,0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', "paletteSelected")
    canvas.itemconfigure("palette", outline="white")
    canvas.addtag("paletteSelected", "withtag", "palette%s" % color)
    canvas.itemconfigure("paletteSelected", outline="#999999")
    
def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)
    

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)


id = canvas.create_rectangle((10,10,30,30), fill='blue', tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))

id = canvas.create_rectangle((10,35,30,55), fill='yellow', tags=('palette', 'paletteyellow'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("yellow"))

id = canvas.create_rectangle((10,60,30,80), fill='green', tags=('palette', 'palettegreen'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("green"))

setColor('black')
canvas.itemconfigure('palette', width=5)

janela.mainloop()