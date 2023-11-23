
class Game:
    def __init__(self):
        self.players = []
        self.cards = {}
        self.card_count = 0
        self.invalid_ids = []
        self.turn = 0

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, name):
        self.name = ""
        self.cards = []
        self.cnts = 0

    def add_card(self, card):
        self.cards.append(card)

    def change_cnts(self, change):
        self.cnts += change
