from modulos import *


class EntryPlaceHolder(Entry):
    def __init__(self, master=None, placeholder = "PLACEHOLDER", color = '#2F4F4F'):
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)
        
        self.put_placeholder()
        
    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if(self['fg'] == self.placeholder_color):
            self.delete('0', END)
            self['fg'] = self.default_fg_color
            
    def focus_out(self, *args):
        if(not self.get()):
            self.put_placeholder()
