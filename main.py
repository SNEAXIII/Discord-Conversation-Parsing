from src.AllMessages import AllMessages
from src.ImageBuilder import ImageBuilder

allMessages = AllMessages(["MisterBalise", "Gibus"])
messages = allMessages.parseMessage(allMessages.listMessages[0:5])
auteurs = allMessages.listAuteur

for message in messages:
    print(message)

builder = ImageBuilder()
builder.build(messages)
a = 0
