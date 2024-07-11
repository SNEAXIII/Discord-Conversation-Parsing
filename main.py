from src.AllMessages import AllMessages
from src.ImageBuilder import ImageBuilder

allMessages = AllMessages(["MisterBalise", "Gibus"])
# messages = allMessages.parseMessage(allMessages.messages[3316:3316+3])
# messages = allMessages.parseMessage(allMessages.messages[11796:11796+1])
# messages = allMessages.parseMessage(allMessages.messages[30165:30165+2])
messages = allMessages.parseMessage(allMessages.messages[30095:30095+4])
# messages = allMessages.parseMessage(allMessages.messages[12589:12601])

builder = ImageBuilder()
builder.build(messages)

# for message in messages:
#     print(message)
# allMessages.reset()
allMessages.reset()
allMessages.afficheMessagesQuiContiennentTexte(["Coucou"], 5)
