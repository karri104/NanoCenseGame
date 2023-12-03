
class Game:
    def __init__(self):
        self.id = ""
        self.turn_length = 1
        self.players = []
        self.player_count = len(self.players)
        self.replicates = []
        self.cards = []
        self.card_count = 0
        self.turn = 1

    def add_player(self, player):
        self.players.append(player)

    def check_replicates(self):
        for player in self.players:
            if player.replicate:
                player.replicate = False
                self.replicates.append(player)

    def check_cnts(self):
        for player in self.players:
            if player.cnts < 0:
                player.cnts = 0
                return False
            elif player.cnts >= 12:
                return True


class Player:
    def __init__(self,):
        self.name = ""
        self.discard_pile = []
        self.sustainability_loop = []
        self.cnts = 0
        self.strike = 0
        self.strike_count = 0
        self.immune = False
        self.replicate = False
        self.loop = False
        self.loop_count = 0
        self.skips = 0
        self.skip_count = 0
        self.loop_card_count = 0
        self.points = 0

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


class Holder():
    def __init__(self):
        # Game count per player count
        self.game_count = 0
        # Number of games that end in cards running out
        self.out_of_cards = 0
        # Number of games that end in a person getting 12 CNTs
        self.winner = 0
        # Running total of average points
        self.total_points = 0
        # Running total of average CNTs
        self.total_cnts = 0
        # Running total of game_lengths
        self.total_length = 0
        # Running total of turns
        self.total_turns = 0
        # Running total of average sustainability loop cards received
        self.total_loop_card_count = 0
        # Running total of average turns skipped by failed loop creation
        self.total_loop_count = 0
        # Running total of average sustainability loop lengths
        self.total_loop_length = 0
        # Running total of average strikes
        self.total_strikes = 0
        # Running total of average skips
        self.total_skips = 0
