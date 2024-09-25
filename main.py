
from flask import Flask,render_template,request
from twilio.twiml.messaging_response import MessagingResponse
from Response.Resposta import Response
from adm import *

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
def tela_adm():
    return adm()

@app.route("/")
def index():
    return render_template("index.html", title="my bot")

if __name__ == '__main__':
    app.run(debug=True)