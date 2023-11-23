
class Game:
    def __init__(self):
        self.turn_length = 1
        self.game_length = 0
        self.players = []
        self.player_count = len(self.players)
        self.cards = []
        self.card_count = 0
        self.turn = 1

    def add_player(self, player):
        self.players.append(player)

    def update_game_length(self):
        self.game_length = self.turn * self.turn_length


class Player:
    def __init__(self, name):
        self.name = ""
        self.discard_pile = []
        self.cnts = 0

    def add_card(self, card):
        self.discard_pile.append(card)

    def change_cnts(self, change):
        self.cnts += change
