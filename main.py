from src.AllMessages import AllMessages
from pprint import pprint

test = AllMessages(["MisterBalise", "Gibus"])

for elem in test.listMessages[0:10]:
    print(elem)

