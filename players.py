
class Game:
    def __init__(self):
        self.turn_length = 1
        self.game_length = 0
        self.players = []
        self.player_count = len(self.players)
        self.replicates = []
        self.cards = []
        self.card_count = 0
        self.turn = 1

    def add_player(self, player):
        self.players.append(player)

    def update_game_length(self):
        self.game_length = self.turn * self.turn_length

    def check_replicates(self):
        for player in self.players:
            if player.replicate:
                player.replicate = False
                self.replicates.append(player)

    def check_cnts(self):
        for player in self.players:
            if player.cnts < 0:
                player.cnts = 0


class Player:
    def __init__(self,):
        self.name = ""
        self.discard_pile = []
        self.sustainability_loop = []
        self.cnts = 0
        self.strike = 0
        self.immune = False
        self.replicate = False
        self.loop = False
        self.skips = 0

    def add_card(self, card):
        self.discard_pile.append(card)

    def change_cnts(self, change):
        self.cnts += change

    def change_name(self, name):
        self.name = name

    def check_immunity(self):
        if self.immune:
            self.immune = False
            return True
        else:
            return False

    def check_strike(self):
        if self.strike != 0:
            return True
        else:
            return False
