import random
class Ghost(object):
    def __init__(self):
        pass
    def choise_colors(self):
        color=["white", "yellow", "purple","red"]
        return random.choice(color)
gos=Ghost()
print(gos.choise_colors())