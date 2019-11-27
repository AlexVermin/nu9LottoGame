"""
Реализация мешка с бочонками лото
"""
import random


class LottoBag:

    def __init__(self):
        self.count = 0
        self.numbers = {}

    def shuffle(self):
        """
        Сбрасывает состояние мешка к начальному
        :return: None
        """
        self.count = 90
        self.numbers = {k: 1 for k in range(1, 91)}

    def get_number(self):
        """
        Возвращает очередной случаййный бочонок или -1, если бочонки закончились
        :return: int
        """
        m_ret = None
        if self.count > 0:
            while True:
                m_ret = random.randint(1, 90)
                if self.numbers[m_ret]:
                    self.numbers[m_ret] = 0
                    self.count -= 1
                    break
        else:
            m_ret = -1
        return m_ret

    def get_rest(self):
        """
        Возвращает количество оставшихся бочонков в мешке
        :return: int
        """
        return self.count


if '__main__' == __name__:
    m_bag = LottoBag()
    m_bag.shuffle()
    print(m_bag.numbers)
    print(f'Осталось {m_bag.count} бочонков')
    for i in range(10):
        print(m_bag.get_number())
    print(m_bag.numbers)
    print(f'Осталось {m_bag.count} бочонков')
