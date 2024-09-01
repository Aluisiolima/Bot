import Response.templatsRespostas as tr
import Response.templastsMensangens as tm

class Response:
    def __init__(self,  cliente , msg):
        self.cliente = str(cliente)
        self.msg = str(msg)

    def read(self):
        if bool(set(self.msg.split()) & set(tm.metodosApresentacao)):
            return self.seed(action="apresentacao")
        
        elif self.msg in tm.metodosProdutos:
            return self.seed(action='curso')

        elif self.msg in tm.metodosRedes:
            return self.seed(action='redes')
        
        elif self.msg in tm.metodosSobre:
            return self.seed(action='sobre')
        
        else :
            return 'nao entedi sua mensagem poderia manda novamente'
    
    def seed(self,action):
        if action == 'apresentacao':
            return tr.resposta(self.cliente)
        elif action == 'curso':
            return tr.apresentarProdutos()
        elif action == 'redes':
            return tr.redes()
        elif action == 'sobre':
            return tr.sobre()
        else :
            return 'acao nao indentificada : error *404*'