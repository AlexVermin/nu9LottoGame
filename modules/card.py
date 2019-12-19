"""
Реализует функционал карты для игры в лото
"""
import random
import math


class LottoCard:

    def __init__(self):
        self.rows = []
        self.rest_num = 0
        self.shuffle()

    def shuffle(self):
        self.rest_num = 15
        m_ctr = {k: 1 for k in range(1, 91)}
        self.rows.clear()
        for i in range(3):
            self.rows.append({})
            for j in range(5):
                while True:
                    m_num = random.randint(1, 90)
                    if m_ctr[m_num]:
                        m_test = [math.trunc(q/10) if q < 90 else 8 for q in self.rows[i].keys()]
                        # print(m_test, math.trunc(m_num/10))
                        if math.trunc(m_num/10) not in m_test:
                            m_ctr[m_num] = 0
                            self.rows[i][m_num] = 0
                            break

    def get_rest(self):
        """
        Возвращает количество "незачеркнутых" чисел на карте
        :return:
        """
        return self.rest_num

    def has_number(self, p_number):
        m_res = 0
        for i in range(3):
            if p_number in self.rows[i].keys():
                m_res = i+1
                break
        return m_res

    def mark(self, p_number):
        m_row = self.has_number(p_number)
        if m_row:
            self.rows[m_row-1][p_number] = 1
            self.rest_num -= 1

    def __str__(self):
        return f'Класс "Карта для игры в лото". Осталось {self.rest_num} незачёркнутых чисел.'

    def __eq__(self, other):
        is_equal = self.rest_num == other.rest_num
        if is_equal:
            for row in range(3):
                for num in self.rows[row]:
                    is_equal = (other.has_number(num) != 0)
                    if not is_equal:
                        break
        return is_equal

    def __gt__(self, other):
        return self.rest_num > other.rest_num

    def __ge__(self, other):
        return self.rest_num >= other.rest_num

    def __le__(self, other):
        return self.rest_num <= other.rest_num

    def __lt__(self, other):
        return self.rest_num < other.rest_num


if '__main__' == __name__:
    m_card = LottoCard()
    print(m_card.rows, m_card.rest_num)
    print(m_card.has_number(90))
    m_card.mark(25)
    print(m_card.rows, m_card.rest_num)
    m_add = LottoCard()
    print(m_add.rows, m_add.rest_num)
    print(m_card == m_add)
    print(m_card != m_add)
    m_test = m_card
    print(m_card.rows, m_test.rest_num)
    print(m_card.rows, m_test.rest_num)
    print(m_card == m_test)
    print(m_card != m_test)
    print(list(m_card.rows[0].keys())[0])
