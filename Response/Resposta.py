from Response.templatsRespostas import resposta
from Response.templastsMensangens import apresentacao

class Response:
    def __init__(self,  cliente , msg):
        self.cliente = str(cliente)
        self.msg = str(msg).split()

    def read(self):
        if bool(set(self.msg) & set(apresentacao)):
            return self.seed(action="apresentacao")
        else :
            return 'nao entedi sua mensagem poderia manda novamente'
    
    def seed(self,action):
        if action == "apresentacao":
            return resposta(self.cliente)