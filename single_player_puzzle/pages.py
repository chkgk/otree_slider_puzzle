from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    timeout_seconds = 60


page_sequence = [Game]
