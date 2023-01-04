from modulos import *



class Validadores():
    def validate_entry_valor_jogador(self,text):
        if text == "": 
            return True
        try:
            value = int(text)
        except ValueError: 
            return False
        return 0 <= value <= 1000000000
    
    def validate_nome_jogador(self,text):
        #pattern = r'^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$'
        pattern = ""
        #if re.fullmatch(pattern, text) is None:
        #    return False
        
        return True
    
    
    def on_invalid(self):
        """
        Show the error message if the data is not valid
        :return:
        """
        self.show_message('Please enter a valid Name', 'red')