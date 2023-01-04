from modulos import *


class Relatorios():
    def printJogador(self):
        webbrowser.open("jogador.pdf")
        
    def geraRelatorioJogador(self):
        self.j = canvas.Canvas("jogador.pdf")
        
        self.codigoRel =  self.codigo_do_jogador
        self.nome_jogadorRel = self.nome_jogador_entry.get()
        self.posicao_jogadorRel = self.posicao_entry.get()
        self.timeRel = self.time_entry.get()
        self.valorRel = self.valor_entry.get()
        
        self.j.setFont("Helvetica-Bold", 22)
        self.j.drawString(200, 790, "Ficha do Jogador")
        
        self.j.drawString(50, 700, 'Código: ')
        self.j.drawString(50, 620, 'Nome do Jogador: ')
        self.j.drawString(50, 600, 'Posição do Jogador: ')
        self.j.drawString(50, 580, 'Time do Jogador: ')
        self.j.drawString(50, 560, 'Valor do Jogador:')
        
        self.j.setFont("Helvetica", 18)
        self.j.drawString(150, 700, self.codigoRel)
        self.j.drawString(280, 620, self.nome_jogadorRel)
        self.j.drawString(280, 600, self.posicao_jogadorRel)
        self.j.drawString(280, 580, self.timeRel)
        self.j.drawString(280, 560, self.valorRel)
        
        
        #self.j.rect(60,300,500,1300, fill=False, stroke=True)
        self.j.showPage()
        self.j.save()
        self.printJogador()