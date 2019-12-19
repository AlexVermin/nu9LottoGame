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

    def __str__(self):
        return f'Класс "Игрок в лото". Имя игрока: {self.name}. Тип игрока: \"{"человек" if "h" == self.kind else "компьютер"}\".'

    def __eq__(self, other):
        return self.kind == other.kind and self.name == other.name and self.card == other.card


if '__main__' == __name__:
    m_user = LottoPlayer('h', 'Alex')
    m_comp = LottoPlayer('c', 'SkyNet')
    m_test = LottoPlayer('h', 'Alex')
    print(m_user)
    print(m_comp)
    print(m_user == m_comp)
    print(m_user != m_comp)
    print(m_user == m_test)
    print(m_user != m_test)