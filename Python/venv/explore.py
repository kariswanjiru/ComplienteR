from twilio.rest import Client

for msg in Client.messages.list():
   print(f"Deleting {msg.body}")
   msg.delete()

msg = client.messages.create(
     to ="+254777013736",
    from_ = "+19377613476",
    body = "Hello from python"
 )

print(f"Created a message: {msg.sid}")