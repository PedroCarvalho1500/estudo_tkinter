from modulos import *


class FuncoesTela():
    def alterar_foto_jogador(self, default=1):
        if(default == 1):
            self.fotoJogador = Image.open("interrogacao.webp")
            self.foto_jogador.configure(width=380)
            self.renderFotoJogador = ImageTk.PhotoImage(self.fotoJogador)
        
        else:  
            self.imagebase64_to_png()  
            self.fotoJogador = Image.open("IMAGEM_BASE64_CONVERTED.png")
            self.foto_jogador.configure(width=380)
            
            self.renderFotoJogador = ImageTk.PhotoImage(self.fotoJogador)

        self.foto_jogador = Label(self.aba_jogadores, image=self.renderFotoJogador, bg='#c0c0c0', highlightbackground='#27c7af')
        self.foto_jogador.image = self.renderFotoJogador
        self.foto_jogador.destroy
        self.foto_jogador.place(relx=0.26, rely=0.58, relheight=0.40, relwidth=0.14)
        #self.foto_jogador.place(x=270, y=220, width=145, height=160)
        #self.foto_jogador.place(relx=0.43, rely=0.44, relheight=0.4, relwidth=0.4)
    
    def variaveis_tela_entries(self):
        self.nome_jogador = self.nome_jogador_entry.get()
        self.posicao_jogador = self.posicao_entry.get()
        self.time = self.time_entry.get()
        self.valor = self.valor_entry.get()

    
    def limpa_tela(self):
        self.nome_jogador_entry.delete(0, END)
        self.posicao_entry.delete(0, END)
        self.time_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.alterar_foto_jogador()
        

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
                        codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nomeJogador CHAR(40) NOT NULL,
                        posicaojogador CHAR(40) NOT NULL,
                        timeJogador CHAR(40),
                        valorJogador  INT(20)  NOT NULL,
                        fotoJogador  CHAR(10000)
                            )""")
        
        self.conn.commit()
        print("BANCO DE DADOS CRIADO!!!")
        self.desconecta_bd()

    def add_cliente(self):
        self.variaveis_tela_entries()
        
        if(self.nome_jogador_entry.get() == ""):
            msg = "É necessário preencher o campo Nome do Jogador!!!"
            messagebox.showinfo("Cadastro de Jogadores - Aviso!!!", msg)
        
        else:
            self.conecta_bd()
            
            self.cursor.execute(""" INSERT INTO jogadores (nomeJogador, posicaojogador, timeJogador, valorJogador, fotoJogador) 
                                VALUES(?,?,?,?,?)
                                """, (self.nome_jogador, self.posicao_jogador, self.time, self.valor, (self.convert_to_base64(self.imagemJogador))))
            
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()
            
            #self.imagebase64_to_png()
        
        
        
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT codigo,nomeJogador, posicaojogador, timeJogador, valorJogador FROM jogadores
                                    ORDER BY codigo ASC; """)
        
        for i in lista:
            self.listaCli.insert("", END, values=i)
          
        
        #self.imagemJogador_base64 = str(fotoDoJogadorBuscaBase64)
        #self.imagebase64_to_png()
        
        #self.fotoJogador = Image.open("")
        
        self.desconecta_bd()
        


    def buscaCliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        
        #self.nome_jogador_entry.insert(0, '%')
        #self.nome_jogador_entry.insert(END, '%')
        nome = self.nome_jogador_entry.get()
        
        #self.posicao_entry.insert(0, '%')
        #self.posicao_entry.insert(END, '%')
        posicaoJogador = self.posicao_entry.get()
        
        
        #self.time_entry.insert(0, '%')
        #self.time_entry.insert(END, '%')
        timeJogador = self.time_entry.get()
        
        #lista = self.cursor.execute("""SELECT codigo,nomeJogador, posicaojogador, timeJogador, valorJogador FROM jogadores
        #                            WHERE nomeJogador LIKE '%s' ORDER BY nomeJogador ASC;""" % nome)

        lista = self.cursor.execute("""SELECT codigo,nomeJogador, posicaojogador, timeJogador, valorJogador FROM jogadores
                                    WHERE nomeJogador LIKE ? AND posicaoJogador LIKE ? AND timeJogador LIKE ? ORDER BY codigo ASC;""", ("%"+nome+"%","%"+posicaoJogador+"%","%"+timeJogador+"%"))
        
        
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
            
        self.limpa_tela()


    #def images_base64(self):
    #    self.bt_cadastrar_base64 = 'CODIGO_BASE64'
        
        
    def convert_to_base64(self, image_file):
        with open(image_file, "rb") as img_file:
            my_string_base64 = base64.b64encode(img_file.read())
        return my_string_base64
    
    
    def uploadImg(self):
        self.imagemJogador = filedialog.askopenfilename()
        self.imagemJogador_base64 = self.convert_to_base64(self.imagemJogador)
        self.alterar_foto_jogador(0)
        #print(self.convert_to_base64(self.imagemJogador))


    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()
        
        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5 = self.listaCli.item(n, 'values')
            self.codigo_do_jogador = col1
            
            self.nome_jogador_entry.insert(END, col2)
            self.posicao_entry.insert(END, col3)
            self.time_entry.insert(END,col4)
            self.valor_entry.insert(END, col5)
        
        self.conecta_bd()
        fotoDoJogadorBuscaBase64 = self.cursor.execute("""SELECT fotoJogador FROM jogadores WHERE codigo == ?;""",[self.codigo_do_jogador])
        
        for i in fotoDoJogadorBuscaBase64:
            for j in i:
                self.imagemJogador_base64 = j
            
        self.alterar_foto_jogador(0)
            #self.imagemJogador_base64 = str(i)
            #print(self.imagemJogador_base64)


        #print("fotoDoJogadorBuscada "+str(fotoDoJogadorBuscaBase64))
        #self.imagemJogador_base64 = fotoDoJogadorBuscaBase64
        #self.imagebase64_to_png()
        #self.fotoJogador = Image.open("IMAGEM_BASE64_CONVERTED.png")
        
        self.desconecta_bd()
            
    def deleta_cliente(self):
        self.variaveis_tela_entries()
        self.conecta_bd()
        
        self.cursor.execute(""" DELETE FROM jogadores WHERE codigo = ? """, [self.codigo_do_jogador])
        self.conn.commit()
        
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
        self.desconecta_bd()

    def altera_cliente(self):
        self.variaveis_tela_entries()
        
        self.conecta_bd()
        
        self.cursor.execute(""" UPDATE jogadores SET nomeJogador = ?, posicaojogador = ?, timeJogador = ?, valorJogador = ?
                            WHERE codigo = ? """, (self.nome_jogador, self.posicao_jogador, self.time, self.valor, self.codigo_do_jogador))
        
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def imagebase64_to_png(self):
        image_64_decode = base64.b64decode(self.imagemJogador_base64)
        image_result = open('IMAGEM_BASE64_CONVERTED.png', 'wb')
        image_result.write(image_64_decode)

    def calendario(self):
        self.calendario1 = Calendar(self.aba_times, fg="gray75", bg="green", font=("Times", '9', 'bold'), locale="pt_br")
        self.calendario1.place(relx=0.5, rely=0.1)
        self.calDataInicio = Button(self.aba_times, text="Inserir Data", command=self.printDataEntry)
        self.calDataInicio.place(relx=0.55, rely=0.54, height=25, width=120)
        
    def printDataEntry(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calDataInicio.destroy()

