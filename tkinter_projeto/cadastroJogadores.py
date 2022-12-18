from tkinter import *
from tkinter import ttk
import sqlite3


#VARIÁVEL PARA A JANELA
janela = Tk()


class FuncoesTela():
    def limpa_tela(self):
        self.nome_jogador_entry.delete(0, END)
        self.posicao_entry.delete(0, END)
        self.time_entry.delete(0, END)
        self.valor_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("jogadores.bd")
        self.cursor = self.conn.cursor()
        
    def desconecta_bd(self):
        self.conn.close()

    def montaTabelas(self):
        self.conecta_bd()
        print("Conectando ao Banco de Dados!")
        
        #CRIAR TABELA
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS jogadores (
                        codigo INTEGER PRIMARY KEY,
                        nome_jogador CHAR(40) NOT NULL,
                        posicaojogador CHAR(40) NOT NULL,
                        time_jogador CHAR(40),
                        valor_jogador  INT(20)  NOT NULL
                            )""")
        
        self.conn.commit()
        print("BANCO DE DADOS CRIADO!!!")
        self.desconecta_bd()


class Application(FuncoesTela):
    def __init__(self):
        
        #INSTANCIANDO A JANELA NOVAMENTE DENTRO DA CLASSE, ASSOCIANDO AO ATRIBUTO.
        self.janela = janela
        #CHAMANDO A FUNÇÃO DE CONFIGURAÇÃO DA TELA.
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_dentro_do_frame2()
        self.montaTabelas()
        
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
        
        
        ## Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = "Código", bg='#c0c0c0', fg='#483D8B')
        self.lb_codigo.place(relx=0.085, rely=0.55, relwidth=0.10, relheight=0.11)
        
        self.codigo_entry = Entry(self.frame_1, fg='#2F4F4F')
        self.codigo_entry.place(relx=0.09, rely=0.62, relwidth=0.09, relheight=0.09)
        
        
        
        self.lb_nomejogador = Label(self.frame_1, text = "Nome do Jogador", bg='#c0c0c0', fg='#483D8B')
        self.lb_nomejogador.place(relx=0.08, rely=0.39, relwidth=0.22, relheight=0.11)
        
        ##ENTRY = INPUT DO TKINTER
        self.nome_jogador_entry = Entry(self.frame_1, fg='#2F4F4F')
        self.nome_jogador_entry.place(relx=0.08, rely=0.47, relwidth=0.22, relheight=0.09)
        
        self.lb_posição = Label(self.frame_1, text = "Posição", bg='#c0c0c0', fg='#483D8B')
        self.lb_posição.place(relx=0.37, rely=0.39, relwidth=0.14, relheight=0.11)

        self.posicao_entry = Entry(self.frame_1, fg='#2F4F4F')
        self.posicao_entry.place(relx=0.37, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_time = Label(self.frame_1, text = "Time", bg='#c0c0c0', fg='#483D8B')
        self.lb_time.place(relx=0.57, rely=0.39, relwidth=0.14, relheight=0.11)

        self.time_entry = Entry(self.frame_1, fg='#2F4F4F')
        self.time_entry.place(relx=0.57, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_valor = Label(self.frame_1, text = "Valor (Euros)", bg='#c0c0c0', fg='#483D8B')
        self.lb_valor.place(relx=0.77, rely=0.39, relwidth=0.14, relheight=0.11)

        self.valor_entry = Entry(self.frame_1, fg='#2F4F4F')
        self.valor_entry.place(relx=0.77, rely=0.47, relwidth=0.14, relheight=0.09)
        
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.frame_1,text="Limpar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.18, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON BUSCAR
        self.bt_buscar = Button(self.frame_1,text="Buscar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_buscar.place(relx=0.31, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_cadastrar = Button(self.frame_1,text="Cadastrar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_cadastrar.place(relx=0.44, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_alterar = Button(self.frame_1,text="Alterar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_alterar.place(relx=0.57, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_apagar = Button(self.frame_1,text="Apagar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'))
        self.bt_apagar.place(relx=0.72, rely=0.08, relwidth=0.1, relheight=0.15)
        






    def lista_dentro_do_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Nome")
        self.listaCli.heading("#2", text="Posição")
        self.listaCli.heading("#3", text="Time")
        self.listaCli.heading("#4", text="Valor(Euros)")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=70)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=30)
        self.listaCli.column("#3", width=20)
        
        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.90)
        
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)



Application()
#LOOPING PARA A JANELA APARECER



#OS FRAMES SÃO AS CAIXAS QUE SEPARAM OS ITENS DA TELA

