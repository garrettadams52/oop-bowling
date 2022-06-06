from player import Player
from frame import Frame


class Game:
    def __init__(self, players, frame = 0):
        self.players = []
        for x in players:
            self.players.append(Player(x))
        self.frame = frame

    def play(self):
        for x in range(10):
            for y in self.players:
                hold = Frame(x,y)
                y.scores.append(hold)

        for k in self.players:
            print(k.calc())
            print(k.scores, k.player)


