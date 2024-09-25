import sqlite3

conexao = sqlite3.connect("./database/mensagens.db")
conn = conexao.cursor()


def cria_mensagem():
    conn.execute('''create table mensagens (
                id_mensagens   INTEGER PRIMARY KEY,
                mensagem TEXT,
                acao text
                );''')
    
def inseri_mensagem(mensagens,ação):
    conn.execute("INSERT INTO mensagens (mensagem,acao) VALUES (?,?);",(mensagens,ação))
    conexao.commit()

# inseri_mensagem(input('mensagem: '),input('acao: '))

conn.close()

cursoDisponiveis = (('informatica basica', 49.99),( 'word',29.99), ('powerPoite' , 59.99))
dados = (("Whatsapp", 86981132378), ("insta", "@Ze da manga"))