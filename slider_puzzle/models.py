from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Christian König gen. Kersting'

doc = """
Slider Puzzle game. Two players move sequentially.
"""


class Constants(BaseConstants):
    name_in_url = 'slider_puzzle'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_starting_player()


class Group(BaseGroup):
    puzzle_solved = models.BooleanField(initial=False)
    starting_player = models.IntegerField()
    move_history = models.LongStringField()

    def set_starting_player(self):
        self.starting_player = random.choice([player.id_in_group for player in self.get_players()])

class Player(BasePlayer):
    pass