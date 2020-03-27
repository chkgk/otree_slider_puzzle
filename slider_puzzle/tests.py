from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):
    def play_round(self):
        if self.player.id_in_group == 1:
            yield pages.Game, {'puzzle_solved': random.choice([True, False]), 'move_history': 'bot got no moves'}
        else:
            yield pages.Game
        yield pages.Results
