from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    form_model = 'group'
    timeout_seconds = 600

    def get_form_fields(self):
        if self.player.id_in_group == 1:
            return ['puzzle_solved', 'move_history']
        else:
            return []

    def js_vars(self):
        return {
            'game_id': "%s_%s" % (self.subsession.id, self.group.id),
            'player_id': self.player.id_in_group,
            'starting_player': self.player.id_in_group == self.group.starting_player,
            'board': [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, None]
                     ],
            'first_player': self.player.id_in_group == 1
        }

class WaitBeforeResults(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [Game, WaitBeforeResults, Results]
