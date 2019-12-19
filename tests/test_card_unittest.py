import unittest
from modules.card import LottoCard


class TestLottoCard(unittest.TestCase):

    def setUp(self):
        self.card = LottoCard()

    def test_init_and_shuffle(self):
        self.assertEqual(self.card.rest_num, 15)
        self.assertEqual(len(self.card.rows), 3)

    def test_get_rest(self):
        self.assertEqual(self.card.get_rest(), 15)
        for i in self.card.rows[1]:
            self.card.mark(i)
        self.assertEqual(self.card.get_rest(), 10)

    def test_has_number(self):
        self.assertFalse(self.card.has_number(95))
        self.assertFalse(self.card.has_number(105))
        for r in self.card.rows:
            for n in r:
                self.assertTrue(self.card.has_number(n))

    def test_mark(self):
        m_cnt = 0
        for r in self.card.rows:
            for n in r:
                m_cnt += 1 if r[n] else 0
        self.assertEqual(m_cnt, 0)
        self.assertEqual(self.card.get_rest(), 15)
        self.card.mark(97)
        m_cnt = 0
        for r in self.card.rows:
            for n in r:
                m_cnt += 1 if r[n] else 0
        self.assertEqual(m_cnt, 0)
        self.assertEqual(self.card.get_rest(), 15)
        for r in self.card.rows:
            for n in r:
                self.card.mark(n)
        m_cnt = 0
        for r in self.card.rows:
            for n in r:
                m_cnt += 1 if r[n] else 0
        self.assertEqual(m_cnt, 15)
        self.assertEqual(self.card.get_rest(), 0)

    def test_str(self):
        self.assertEqual(self.card.__str__(), 'Класс "Карта для игры в лото". Осталось 15 незачёркнутых чисел.')
        self.card.mark(list(self.card.rows[0].keys())[0])
        self.assertEqual(self.card.__str__(), 'Класс "Карта для игры в лото". Осталось 14 незачёркнутых чисел.')

    def test_eq(self):
        self.assertTrue(self.card == self.card)
        tmp = LottoCard()
        self.assertFalse(self.card == tmp)
        self.card.mark(list(self.card.rows[0].keys())[0])
        self.assertFalse(self.card == tmp)
        self.assertGreater(tmp, self.card)
        self.assertGreaterEqual(tmp, self.card)
        self.assertLess(self.card, tmp)
        self.assertLessEqual(self.card, tmp)
