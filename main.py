from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from Response.Resposta import Response

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    msg_resposta = request.values.get('Body', '')
    print(msg_resposta)
    resp = MessagingResponse(Response.seed())
    msg = resp.message()
    msg.body()
    return str(resp)

@app.route("/")
def index():
    return "esta tudo ok"

if __name__ == '__main__':
    app.run(debug=True)