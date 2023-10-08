from src.AllMessages import AllMessages
from pprint import pprint

test = AllMessages(["MisterBalise", "Gibus"])
premierMessage = test.listMessages[1]
vingtiemeMessage = test.listMessages[20]
print(premierMessage)
print(vingtiemeMessage)
# print(premierMessage.author.name)
