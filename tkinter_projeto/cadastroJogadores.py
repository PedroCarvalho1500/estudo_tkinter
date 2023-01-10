from modulos import *
from validEntry import *
from gradiente import *
from relatorios import *
from funcoes_tela import *
from placeHolder import *

#GERANDO UM EXECUTÁVEL
#pyinstaller --onefile --noconsole --windowed --icon='soccer.png' cadastroJogadores.py
#--hidden-import='PIL._tkinter_finder' cadastroJogadores.py

#VARIÁVEL PARA A JANELA
janela = tix.Tk()




class Application(FuncoesTela, Relatorios, GradientFrame, Validadores):
    def __init__(self):
        
        #INSTANCIANDO A JANELA NOVAMENTE DENTRO DA CLASSE, ASSOCIANDO AO ATRIBUTO.
        self.janela = janela
        
        #self.images_base64()
        
        self.validaEntradas()
        #CHAMANDO A FUNÇÃO DE CONFIGURAÇÃO DA TELA.
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_dentro_do_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
            
        
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
        self.image = Image.open("soccer.png")
        self.render = ImageTk.PhotoImage(self.image)
        
        self.fotoJogador = Image.open("interrogacao.webp")
        self.renderFotoJogador = ImageTk.PhotoImage(self.fotoJogador)
        
        self.frame_1 = Frame(self.janela, bg='#c0c0c0', highlightbackground='#27c7af')
        self.frame_1.place(relx= 0.04, rely=0.041, relwidth= 0.91, relheight=0.46)
        
        self.frame_2 = Frame(self.janela, bg='#c0c0c0', highlightbackground='#27c7ad', highlightthickness=3)
        self.frame_2.place(relx= 0.04, rely=0.52, relwidth= 0.91, relheight=0.46)
        
        
        self.imagemJogador_base64 = ''
        #b1 = Button(self.janela, image=imagem_jogador)
        #b1.pack(pady=10)
        #b1.image = imagem_jogador
        
        
        # PLACE PACK GRID 
        # O PACK NÃO DEIXA-NOS COLOCAR OBJETOS EM POSIÇÕES ESPECÍFICAS
        # O PLACE PERMITE INSERIR OS ELEMENTOS NOS LOCAIS ESPECÍFICOS.

    def widgets_frame1(self):

        #CRIAÇÃO DE ABAS NO TKINTER
        #IMPLEMENTAR POSTERIORMENTE AS ABAS DE CADASTRO DE JOGADORES, TIMES, CAMPEONATOS/LIGAS E SELEÇÕES
        self.abas = ttk.Notebook(self.frame_1)
        #self.aba_jogadores = GradientFrame(self.abas)
        self.aba_jogadores = Frame(self.abas)
        self.aba_times = Frame(self.abas)
        
        self.aba_jogadores.configure(background="#c0c0c0")
        self.aba_times.configure(background="#696969")
        self.abas.add(self.aba_jogadores, text="Cadastro de Jogadores")
        self.abas.add(self.aba_times, text="Cadastro de Times")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
        
        
        
        self.img = Label(self.aba_jogadores, image=self.render, background="#c0c0c0")
        self.img.image = self.render
        self.img.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.22)
        
        
        
        
        #self.img.place(x=-170, y=-30)
        ## Criação da label e entrada do código
        #self.lb_codigo = Label(self.frame_1, text = "Código", bg='#c0c0c0', fg='#483D8B')
        #self.lb_codigo.place(relx=0.085, rely=0.55, relwidth=0.10, relheight=0.11)
        
        #self.codigo_entry = Entry(self.frame_1, fg='#2F4F4F')
        #self.codigo_entry.place(relx=0.09, rely=0.62, relwidth=0.09, relheight=0.09)
        
        self.foto_jogador = Label(self.aba_jogadores, image=self.renderFotoJogador)
        self.foto_jogador.image = self.renderFotoJogador
        #self.foto_jogador.place(x=270, y=220, width=150, height=170)
        self.foto_jogador.place(relx=0.26, rely=0.58, relheight=0.40, relwidth=0.14)
        
        
        self.lb_nomejogador = Label(self.aba_jogadores, text = "Nome do Jogador", bg='#c0c0c0', fg='#483D8B')
        self.lb_nomejogador.place(relx=0.21, rely=0.39, relwidth=0.22, relheight=0.11)
        
        ##ENTRY = INPUT DO TKINTER
        self.nome_jogador_entry = EntryPlaceHolder(self.aba_jogadores, "Digite o nome do Jogador")
        #self.nome_jogador_entry = Entry(self.aba_jogadores, fg='#2F4F4F', validate="key", validatecommand=self.valida_nome)
        self.nome_jogador_entry.place(relx=0.21, rely=0.47, relwidth=0.22, relheight=0.09)
        
        
        #button_upload_photo = Button(self.aba_jogadores, text='Carregar Foto', command=self.UploadAction, bg='#c0c0c0')
        #button_upload_photo.place(relx=0.47, rely=0.60, relwidth=0.14, relheight=0.11)
        
        #image = Image.open()
        #render = ImageTk.PhotoImage(image)
        
        #img = Label(self.aba_jogadores, image=render, bg='#c0c0c0')
        #img.image = render
        #img.place(x=-160, y=-10)
        
        self.lb_posição = Label(self.aba_jogadores, text = "Posição", bg='#c0c0c0', fg='#483D8B')
        self.lb_posição.place(relx=0.47, rely=0.39, relwidth=0.14, relheight=0.11)

        self.posicao_entry = Entry(self.aba_jogadores, fg='#2F4F4F')
        self.posicao_entry.place(relx=0.47, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_time = Label(self.aba_jogadores, text = "Time", bg='#c0c0c0', fg='#483D8B')
        self.lb_time.place(relx=0.66, rely=0.39, relwidth=0.14, relheight=0.11)

        self.time_entry = Entry(self.aba_jogadores, fg='#2F4F4F')
        self.time_entry.place(relx=0.66, rely=0.47, relwidth=0.14, relheight=0.09)
        
        self.lb_valor = Label(self.aba_jogadores, text = "Valor (Euros)", bg='#c0c0c0', fg='#483D8B')
        self.lb_valor.place(relx=0.85, rely=0.39, relwidth=0.14, relheight=0.11)

        self.valor_entry = Entry(self.aba_jogadores, fg='#2F4F4F', validate="key", validatecommand=self.vcmd2)
        self.valor_entry.place(relx=0.85, rely=0.47, relwidth=0.14, relheight=0.09)
        
        #ESTILIZAÇÃO DO BOTÃO LIMPAR
        self.canvas_bt = Canvas(self.aba_jogadores, bd=0, bg="black", highlightbackground="gold", highlightthickness=5)
        self.canvas_bt.place(relx=0.20, rely=0.06, relwidth=0.721, relheight=0.19)
        
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_limpar = Button(self.aba_jogadores,text="Limpar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' ,command=self.limpa_tela)
        self.bt_limpar.place(relx=0.25, rely=0.08, relwidth=0.1, relheight=0.15)
        
        self.balao_limpar = tix.Balloon(self.aba_jogadores)
        self.balao_limpar.bind_widget(self.bt_limpar, balloonmsg = "Clique aqui para Limpar os valores preenchidos nos campos")
        
        
        ## CRIAÇÃO BUTTON BUSCAR
        self.bt_buscar = Button(self.aba_jogadores,text="Buscar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' , command=self.buscaCliente)
        self.bt_buscar.place(relx=0.38, rely=0.08, relwidth=0.1, relheight=0.15)
        
        self.balao_buscar = tix.Balloon(self.aba_jogadores)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = "Digite nos campos os valores do jogador que deseja buscar")
        
        
    
        self.bt_uploadPhoto = Button(self.aba_jogadores, text="Upload Photo ", font= ("verdana",10,'bold'), border=2, bg="#aaf111", activebackground='#108ecb' ,activeforeground='white' , command=self.uploadImg)
        self.bt_uploadPhoto.place(relx=0.50, rely=0.60, relwidth=0.1, relheight=0.15)
        

 
        #self.bt_cadastrar = PhotoImage(data=base64.b64decode(self.bt_cadastrar_base64))
        
        
        
        #CRIAÇÃO DO IMG_NOVO
        #self.imgNovo = PhotoImage(file="new_button.jpg")
        
        #O SUBSAMPLE IRÁ DAR AS COORDENADAS DESEJADAS PARA O TAMANHO DO BOTÃO
        #self.imgNovo = self.imgNovo.subsample(-6,-6)
        #self.style = ttk.Style()
        #self.style.configure("BW.TButton", relwidth=1, relheight=1, foreground= "yellow", borderwidth=0, bordercolor = "blue", background="#27c7af", image=self.imgNovo)
        
        
        
        ## CRIAÇÃO BUTTON LIMPAR
        #self.bt_cadastrar = ttk.Button(self.frame_1, style="BW.TButton", command=self.add_cliente)
        self.bt_cadastrar = Button(self.aba_jogadores,text="Cadastrar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' , command=self.add_cliente)
        self.bt_cadastrar.place(relx=0.51, rely=0.08, relwidth=0.1, relheight=0.15)
        
        self.balao_cadastrar = tix.Balloon(self.aba_jogadores)
        self.balao_cadastrar.bind_widget(self.bt_cadastrar, balloonmsg = "Clique aqui para cadastrar um novo jogador com os valores preenchidos nos campos")
        #self.bt_cadastrar.config(image = self.imgNovo)
        
        
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_alterar = Button(self.aba_jogadores,text="Alterar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' , command=self.altera_cliente)
        self.bt_alterar.place(relx=0.64, rely=0.08, relwidth=0.1, relheight=0.15)
        
        self.balao_alterar = tix.Balloon(self.aba_jogadores)
        self.balao_alterar.bind_widget(self.bt_alterar, balloonmsg = "Clique aqui para alterar o jogador com os novos valores preenchidos nos campos")
        
        
        ## CRIAÇÃO BUTTON LIMPAR
        self.bt_apagar = Button(self.aba_jogadores,text="Apagar", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' , command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.77, rely=0.08, relwidth=0.1, relheight=0.15)
        
        self.balao_apagar = tix.Balloon(self.aba_jogadores)
        self.balao_apagar.bind_widget(self.bt_apagar, balloonmsg = "Clique aqui para deletar o jogador selecionado")



        #self.bt_abrirJanela2 = Button(self.aba_jogadores,text="Abrir Janela 2", border=2, bg="#aaf111", font=('verdana', 10, 'bold'),activebackground='#108ecb' ,activeforeground='white' , command=self.janela2)
        #self.bt_abrirJanela2.place(relx=0.90, rely=0.08, relwidth=0.1, relheight=0.15)
        
        
        
        
        #### DROPDROWN BUTTON ####
        #self.Tipvar = StringVar()
        #self.TipV = ("Masculino", "Feminino")
        #self.Tipvar.set("Masculino")
        #self.popupMenu = OptionMenu(self.aba_times, self.Tipvar, *self.TipV)
        #self.popupMenu.place(relx=0.2, rely=0.2, relwidth=0.15, relheight=0.15)
        #self.sexo = self.Tipvar.get()
        #print(self.sexo)
        
        ### Calendário ###
        self.bt_calendario = Button(self.aba_times, text= "Data", command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02, relheight=0.1, relwidth=0.2)
        self.entry_data = Entry(self.aba_times, width=10)
        self.entry_data.place(relx=0.5, rely=0.12, relheight=0.1, relwidth=0.2 )
        


    def lista_dentro_do_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Posição")
        self.listaCli.heading("#4", text="Time")
        self.listaCli.heading("#5", text="Valor(Euros)")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=5)
        self.listaCli.column("#2", width=80)
        self.listaCli.column("#3", width=30)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=30)
        
        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.90)
        
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)
        
        
        # BIND SIGNIFICA TODA VEZ QUE FICAR UMA INTERAÇÃO COM A LISTA
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        
        #INSTANCIANDO O MENU BAR
        menubar = Menu(self.janela, tearoff=0)
        
        #CONFIGURANDO A PARTE DE CIMA, O MENUBAR
        self.janela.config(menu=menubar)
        
        #UMA VARIÁVEL PARA CADA MENUBAR, OU SEJA, CADA COLUNA DENTRO D
        filemenu = Menu(menubar, tearoff=0, bg="#FFDEAD", activeborderwidth=2, activeforeground="#F8F8FF", activebackground="#000000", font=('verdana', 10, 'bold'))
        filemenu2 = Menu(menubar, tearoff=0, bg="#FFDEAD", activeborderwidth=2, activeforeground="#F8F8FF", activebackground="#000000", font=('verdana', 10, 'bold'))
        filemenu3 = Menu(menubar, tearoff=0, bg="#FFDEAD", activeborderwidth=2, activeforeground="#F8F8FF", activebackground="#000000", font=('verdana', 10, 'bold'))

        def quit(): self.janela.destroy()
        
        
        menubar.add_cascade(label="Opções", menu=filemenu, background="#FFDEAD", font=('verdana', 10, 'bold') )
        menubar.add_cascade(label= "Sobre", menu= filemenu2, background="#FFDEAD", font=('verdana', 10, 'bold'))
        menubar.add_cascade(label= "Relatórios", menu= filemenu3, background="#FFDEAD", font=('verdana', 10, 'bold'))
        
        
        filemenu.add_command(label="Sair", command= quit,font=('verdana', 10, 'bold'))
        filemenu.add_command(label="Página de Clubes", command=lambda: print("CLICOU EM PÁGINA DE CLUBES"), font=('verdana', 10, 'bold'))
        
        filemenu2.add_command(label="Versão do Sistema", command=lambda: print("VERSÃO v0.1.0"))
        
        filemenu3.add_command(label="Ficha do Jogador", command=self.geraRelatorioJogador)

    def janela2(self):
        self.janela2 = Toplevel()
        self.janela2.title("Janela 2")
        self.janela2.configure(background='green')
        self.janela2.geometry("400x200")
        self.janela2.resizable(False, False)
        
        # DE ONDE A JANELA VEIO, ISTO É: A JANELA 2 VEM DA JANELA 1
        self.janela2.transient(self.janela)
        
        # A JANELA IRÁ FICAR A FRENTE DA OUTRA
        self.janela2.focus_force()
        
        #IMPEDIR QUE QUALQUER COISA SEJA DIGITADA NA OUTRA JANELA
        self.janela2.grab_set()



    def validaEntradas(self):
        self.vcmd2 = (self.janela.register(self.validate_entry_valor_jogador), "%P")
        self.valida_nome = (self.janela.register(self.validate_nome_jogador), "%P")

Application()
#LOOPING PARA A JANELA APARECER



#OS FRAMES SÃO AS CAIXAS QUE SEPARAM OS ITENS DA TELA

