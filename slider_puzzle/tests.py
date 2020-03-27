from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Game, {'puzzle_solved': random.choice([True, False])}
        yield pages.Results
