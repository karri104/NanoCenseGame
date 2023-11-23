
class Game:
    def __init__(self):
        self.players = []
        self.cards = {}

    def add_player(self, player):
        self.players.append(player)

    def update_cards(self, cards):
        self.cards = cards


class Player:
    def __init__(self):
        self.cards = []
        self.cnts = 0

    def add_card(self, card):
        self.cards.append(card)

    def change_cnts(self, change):
        self.cnts += change
