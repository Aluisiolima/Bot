from twilio.rest import Client


account_sid = 'AC7279e5e40c8356c7a6cda8e130dad697'
auth_token = '245cfdb87a6baccbf78234787cf5b799'

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='eai',
  to='whatsapp:+558681132378'
)

print(message.sid)