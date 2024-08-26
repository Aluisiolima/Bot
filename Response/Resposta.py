from Response.templatsRespostas import resposta
from Response.templastsMensangens import apresentacao

class Response:
    def __init__(self,  cliente , msg):
        self.cliente = str(cliente)
        self.msg = str(msg)

    def read(self):
        if bool(set(self.msg.split()) & set(apresentacao)):
            return self.seed(action="apresentacao")
        
        elif self.msg == '1':
            return 'entao vc deseja ver nosso cursos ? digite *ok*  '

        else :
            return 'nao entedi sua mensagem poderia manda novamente'
    
    def seed(self,action):
        if action == "apresentacao":
            return resposta(self.cliente)