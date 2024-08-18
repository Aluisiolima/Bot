from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    print(request.values)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("""Oi! Que legal que você quer saber mais sobre nossos cursos! Na Qualifica📚, temos opções incríveis que podem transformar sua carreira.

Oferecemos cursos em várias áreas, como Tecnologia da Informação, Eletrônica, Mecânica e Design Gráfico. Se você está interessado em mergulhar no mundo da tecnologia, nossa formação em TI vai te preparar com as habilidades mais atuais. Para quem gosta de trabalhar com circuitos e dispositivos, o curso de Eletrônica é perfeito. E se você se interessa por máquinas e sistemas mecânicos, o curso de Mecânica vai te dar a base necessária para se destacar. Ah, e não podemos esquecer do Design Gráfico, ideal para quem tem uma paixão por criar e comunicar visualmente.

Cada curso é projetado para oferecer uma educação de qualidade, com prática e teoria na medida certa. Se você está pronto para dar o próximo passo na sua carreira, venha conhecer mais sobre a Qualifica📚. Estamos aqui para ajudar você a alcançar seus objetivos""")
    return str(resp)

@app.route("/")
def index():
    return "esta tudo ok"

if __name__ == '__main__':
    app.run()