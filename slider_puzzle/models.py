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
    starting_player = models.IntegerField()
    move_history = models.LongStringField()
    move_histories_disagree = models.BooleanField()
    puzzle_solved = models.BooleanField(initial=False)

    def set_starting_player(self):
        self.starting_player = random.choice([player.id_in_group for player in self.get_players()])
        for player in self.get_players():
            player.is_starting_player = self.starting_player == player.id_in_group

class Player(BasePlayer):
    move_history = models.LongStringField()
    is_starting_player = models.BooleanField()
    puzzle_solved = models.BooleanField(initial=False)

