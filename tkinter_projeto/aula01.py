from tkinter import *



#VARIÁVEL PARA A JANELA
janela = Tk()

class Application():
    def __init__(self):
        
        #INSTANCIANDO A JANELA NOVAMENTE DENTRO DA CLASSE, ASSOCIANDO AO ATRIBUTO.
        self.janela = janela
        
        #CHAMANDO A FUNÇÃO DE CONFIGURAÇÃO DA TELA.
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        janela.wait_window()
        
    def tela(self):
        #TÍTULO ACIMA DA JANELA
        self.janela.title("CADASTRO DE JOGADORES")
        
        #bg = PhotoImage(file = "soccer.png")
        
        #label1 = Label(self.janela, image = bg)
        #label1.pack(pady = 50)
        
        self.janela.configure(background="#000080")
        
        #LARGURA E ALTURA
        self.janela.geometry("1200x700")
        
        #NÃO PODE MUDAR A LARGURA, APENAS A ALTURA
        self.janela.resizable(False, True)
        
        
        self.janela.resizable(True, True)
        
        
        #DEFINIR O TAMANHO MÁXIMO DA TELA
        self.janela.maxsize(width=1720, height=1300)
        
        #DEFINIR O TAMANHO MÍNIMO DA TELA
        self.janela.minsize(width=900, height=900)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bg='#c0c0c0', highlightbackground='#27c7ad', highlightthickness=3)
        self.frame_1.place(relx= 0.04, rely=0.041, relwidth= 0.91, relheight=0.46)
        
        self.frame_2 = Frame(self.janela, bg='#c0c0c0', highlightbackground='#27c7ad', highlightthickness=3)
        self.frame_2.place(relx= 0.04, rely=0.52, relwidth= 0.91, relheight=0.46)
        
        # PLACE PACK GRID 
        # O PACK NÃO DEIXA-NOS COLOCAR OBJETOS EM POSIÇÕES ESPECÍFICAS
        # O PLACE PERMITE INSERIR OS ELEMENTOS NOS LOCAIS ESPECÍFICOS.

    def widgets_frame1(self):
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.frame_1,text="Limpar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.18, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON BUSCAR
        self.bt_limpar = Button(self.frame_1,text="Buscar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.31, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.frame_1,text="Cadastrar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.44, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.frame_1,text="Alterar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.57, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.frame_1,text="Apagar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.72, rely=0.08, relwidth=0.1, relheight=0.15)
        

        ## Criação da label e entrada do código
        self.lb_nomejogador = Label(self.frame_1, text = "Nome do Jogador")
        self.lb_nomejogador.place(relx=0.08, rely=0.35, relwidth=0.22, relheight=0.11)

        ##ENTRY = INPUT DO TKINTER
        self.nome_jogador_entry = Entry(self.frame_1)
        self.nome_jogador_entry.place(relx=0.08, rely=0.47, relwidth=0.22, relheight=0.09)
        
        self.lb_posição = Label(self.frame_1, text = "Posição")
        self.lb_posição.place(relx=0.37, rely=0.35, relwidth=0.14, relheight=0.11)

        self.posicao_entry = Entry(self.frame_1)
        self.posicao_entry.place(relx=0.37, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_time = Label(self.frame_1, text = "Time")
        self.lb_time.place(relx=0.57, rely=0.35, relwidth=0.14, relheight=0.11)

        self.time_entry = Entry(self.frame_1)
        self.time_entry.place(relx=0.57, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_valor = Label(self.frame_1, text = "Valor (em Euros)")
        self.lb_valor.place(relx=0.77, rely=0.35, relwidth=0.14, relheight=0.11)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.77, rely=0.47, relwidth=0.14, relheight=0.09)



Application()
#LOOPING PARA A JANELA APARECER



#OS FRAMES SÃO AS CAIXAS QUE SEPARAM OS ITENS DA TELA

