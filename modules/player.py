"""
Реализация игрока

.kind - тип игрока: c - компьютер, h - человек
"""
from modules.card import LottoCard


class LottoPlayer:

    def __init__(self, p_kind, p_name):
        self.card = LottoCard()
        if p_kind in 'hc':
            self.kind = p_kind
        else:
            self.kind = 'c'
        self.finished = False
        self.failed = False
        self.name = p_name

    def make_move(self, p_number, p_act):
        if 'c' == self.kind:
            self.card.mark(p_number)
        else:
            if p_act:
                if self.card.has_number(p_number):
                    self.card.mark(p_number)
                else:
                    self.failed = True
            else:
                if self.card.has_number(p_number):
                    self.failed = True
        self.finished = not self.card.get_rest()

    def prepare(self):
        self.card.shuffle()
        self.failed = False
        self.finished = False


if '__main__' == __name__:
    m_user = LottoPlayer('h', 'Alex')
