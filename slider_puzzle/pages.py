from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    form_model = 'player'
    form_fields = ['puzzle_solved', 'move_history']

    timeout_seconds = 600

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
    def after_all_players_arrive(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)

        if p1.move_history == p2.move_history:
            self.group.move_history = p1.move_history
            self.group.move_histories_disagree = False

            if p1.puzzle_solved or p2.puzzle_solved:
                self.group.puzzle_solved = True
                p1.puzzle_solved = True
                p2.puzzle_solved = True
            else:
                self.group.puzzle_solved = False
        else:
            self.group.move_histories_disagree = True

class Results(Page):
    pass


page_sequence = [Game, WaitBeforeResults, Results]
