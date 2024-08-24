from Response.templats import resposta

class Response:
    def __init__(self,  cliente , msg):
        self.cliente = str(cliente)
        self.msg = str(msg)

    def read(self):
        if self.msg in ['oi', 'ola', 'olá', 'oiii', 'oiiii', 'bom dia' , 'boa tarde', 'boa noite']:
            return self.seed(action="apresentacao")
        else :
            return 'nao entedi sua mensagem poderia manda novamente'
    
    def seed(self,action):
        if action == "apresentacao":
            return resposta(self.cliente)