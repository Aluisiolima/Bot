import database.banco as db

def resposta(clinte) :
     return f"""Oi  {clinte}! Que legal que você quer saber mais sobre nossos cursos! Na Qualifica📚, temos opções incríveis que podem transformar sua carreira.

    Oferecemos cursos em várias áreas, como Tecnologia da Informação, Eletrônica, Mecânica e Design Gráfico. Se você está interessado em mergulhar no mundo da tecnologia, nossa formação em TI vai te preparar com as habilidades mais atuais.
    Oq gostaria de ver agora? digite:
    1 para curso
    2 para saber mais sobre nois !!!
    3 para ver nossa redes sociais 😁"""



def apresentarProdutos():
     a = ''
     for key,value in db.cursoDisponiveis:
          a += f'curso de *{key}* no valor de _{value}_\n'

     return f'termos disponiveis no momentos os cursos de :\n{a}' 