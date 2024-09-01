
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from Response.Resposta import Response
import database.banco as db

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    msg_recebida = request.values.get("Body", "").lower()
    cliente = request.values.get("ProfileName", '')
    bot = Response(cliente,msg_recebida)
    # print(request.values)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(bot.read())
    return str(resp)

@app.route("/adm")
def adm():
    return str(db.cursoDisponiveis)

@app.route("/")
def index():
    return "esta tudo ok"

if __name__ == '__main__':
    app.run(debug=True)