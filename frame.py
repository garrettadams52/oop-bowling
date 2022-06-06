import random

class Frame:
    def __init__ (self, frame, player):
        self.frame = frame + 1
        self.player = player
        self.result = []

    def __new__(self, frame, player):
        result = []
        result.append(random.randint(0,10))
        if result[0] == 10:
            return [10,'strike']
        result.append(random.randint(0,10-result[0]))
        if result[1]+result[0] == 10:
            result.append('spare')
        return result