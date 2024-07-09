from src.AllMessages import AllMessages
from src.ImageBuilder import ImageBuilder

test = AllMessages(["MisterBalise", "Gibus"])
a = test.parseMessage(test.listMessages[0:5])
for elem in a:
    print(elem)
# for elem in test.listMessages[0:5]:
#     print(elem)
builder = ImageBuilder()
builder.build(a)
a = 0