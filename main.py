from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    print(request.values)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("funcionou")
    return str(resp)

@app.route("/")
def index():
    return "esta tudo ok"

if __name__ == '__main__':
    app.run()