from twilio.rest import Client

client = Client("AC50e36926f48751d00b6677425dbcbdb4","a6e98b38367fddaeb65447ff539e118a")

for msg in client.messages.list():
   print(f"Deleting {msg.body}")
   msg.delete()

#msg = client.messages.create(
    # to ="+254777013736",
   # from_ = "+19377613476",
  #  body = "Hello from python"
 #)

#print(f"Created a message: {msg.sid}")