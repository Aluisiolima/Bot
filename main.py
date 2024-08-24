from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from Response.Resposta import Response

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    msg_recebida = request.values.get("Body", "").lower()
    cliente = request.values.get("ProfileName", '')
    bot = Response(cliente,msg_recebida)
    print(msg_recebida)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(bot.read())
    return str(resp)

@app.route("/")
def index():
    return "esta tudo ok"

if __name__ == '__main__':
    app.run()