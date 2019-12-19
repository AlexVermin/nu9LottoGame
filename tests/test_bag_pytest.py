from modules.bag import LottoBag


class TestLottoBag:

    def setup(self):
        self.obj = LottoBag()

    def test_init(self):
        assert self.obj.count == 0
        assert len(self.obj.numbers) == 0

    def test_shuffle(self):
        self.obj.shuffle()
        assert self.obj.count == 90
        m_sum = 0
        for k in self.obj.numbers:
            m_sum += self.obj.numbers[k]
        assert m_sum == 90

    def test_get_number(self):
        m_sum_def = 0
        m_sum_test = 0
        self.obj.shuffle()
        for i in range(1, 91):
            m_sum_def += i
            m_sum_test += self.obj.get_number()
        assert self.obj.count == 0
        assert m_sum_def == m_sum_test
        assert self.obj.get_number() == -1

    def test_get_rest(self):
        assert self.obj.get_rest() == 0
        self.obj.shuffle()
        assert self.obj.get_rest() == 90
        for i in range(1, 91):
            m_test = self.obj.get_number()
        assert self.obj.get_rest() == 0
