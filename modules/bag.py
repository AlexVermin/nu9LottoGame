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
        Возвращает очередной случайный бочонок или -1, если бочонки закончились
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

    def __str__(self):
        return f'Класс "Мешочек с бочёнками". Осталось {self.count} бочёнков.'

    def __eq__(self, other):
        is_equal = self.count == other.count
        if is_equal:
            for i in range(1, 91):
                if i in self.numbers and i in other.numbers:
                    is_equal = self.numbers[i] == other.numbers[i]
                else:
                    if i not in self.numbers and i not in other.numbers:
                        is_equal = True
                if not is_equal:
                    break
        return is_equal

    def __gt__(self, other):
        return self.count > other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __le__(self, other):
        return self.count <= other.count

    def __lt__(self, other):
        return self.count < other.count


if '__main__' == __name__:
    m_bag = LottoBag()
    print(m_bag)
    m_bag1 = LottoBag()
    print('After init:')
    print(f'  == : {m_bag == m_bag1}')
    print(f'  != : {m_bag != m_bag1}')
    m_bag.shuffle()
    m_bag1.shuffle()
    print('After shuffle:')
    print(f'  == : {m_bag == m_bag1}')
    print(f'  != : {m_bag != m_bag1}')
    for t in range(10):
        m_bag.get_number()
        m_bag1.get_number()
    print('After 10 moves:')
    print(f'  == : {m_bag == m_bag1}')
    print(f'  != : {m_bag != m_bag1}')
