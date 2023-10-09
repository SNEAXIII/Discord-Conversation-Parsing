from src.AllMessages import AllMessages
from pprint import pprint

test = AllMessages(["MisterBalise", "Gibus"])
premierMessage = test.listMessages[11]
vingtiemeMessage = test.listMessages[20]
print(premierMessage)
print(vingtiemeMessage)
# print(premierMessage.author.name)
for elem in test.listMessages[0:30]:
    print(elem)