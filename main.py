from src.AllMessages import AllMessages
from src.ImageBuilder import ImageBuilder

allMessages = AllMessages(["MisterBalise", "Gibus"])
messages = allMessages.parseMessage(allMessages.messages[0:5])

for message in messages:
    print(message)

builder = ImageBuilder()
builder.build(messages)
