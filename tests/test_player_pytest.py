import math
from modules.player import LottoPlayer


class TestLottoPlayer:

    def setup(self):
        self.hum = LottoPlayer('h', 'Player')
        self.com = LottoPlayer('c', 'SkyNet')

    def test_init(self):
        wt = LottoPlayer('x', 'XaKeP')
        assert self.hum.kind in 'hc'
        assert self.hum.kind == 'h'
        assert self.hum.name == 'Player'
        assert self.hum.card.get_rest() == 15
        assert len(self.hum.card.rows) == 3
        assert self.hum.finished is False
        assert self.hum.failed is False
        ###
        assert self.com.kind == 'c'
        assert self.com.name == 'SkyNet'
        assert self.com.card.get_rest() == 15
        assert len(self.com.card.rows) == 3
        assert self.com.finished is False
        assert self.com.failed is False
        ###
        assert wt.kind == 'c'
        assert wt.name == 'XaKeP'
        assert wt.card.get_rest() == 15
        assert len(wt.card.rows) == 3
        assert wt.finished is False
        assert wt.failed is False

    def test_prepare(self):
        self.hum.prepare()
        assert self.hum.kind in 'hc'
        assert self.hum.kind == 'h'
        assert self.hum.name == 'Player'
        assert self.hum.card.get_rest() == 15
        assert len(self.hum.card.rows) == 3
        assert self.hum.finished is False
        assert self.hum.failed is False
        self.com.prepare()
        assert self.com.kind == 'c'
        assert self.com.name == 'SkyNet'
        assert self.com.card.get_rest() == 15
        assert len(self.com.card.rows) == 3
        assert self.com.finished is False
        assert self.com.failed is False
        
    def test_make_move(self):
        # зачеркнуть несуществующее число =>
        self.hum.prepare()
        self.com.prepare()
        self.hum.make_move(95, True)
        assert self.hum.failed is True  # должен взвестись флаг проигрыша для человека
        assert self.hum.card.get_rest() == 15
        self.com.make_move(95, True)
        assert self.com.failed is False  # а компьюеру - всё равно, он не ошибается
        assert self.com.card.get_rest() == 15
        # ну и проверим, что после одного хода никто не завершил игру
        assert self.hum.finished is False
        assert self.com.finished is False
        # пропустить несуществующее число =>
        self.hum.prepare()
        self.com.prepare()
        self.hum.make_move(95, False)
        assert self.hum.failed is False  # человек не ошибся
        assert self.hum.card.get_rest() == 15
        self.com.make_move(95, False)
        assert self.com.failed is False  # а компьюер - тем более
        assert self.com.card.get_rest() == 15
        # зачеркнуть существующее число =>
        self.hum.prepare()
        self.com.prepare()
        self.hum.make_move(list(self.hum.card.rows[0].keys())[1], True)
        assert self.hum.failed is False  # человек не ошибся
        assert self.hum.card.get_rest() == 14
        self.com.make_move(list(self.com.card.rows[0].keys())[1], True)
        assert self.com.failed is False  # а компьюер - тем более
        assert self.com.card.get_rest() == 14
        # пропустить существующее число =>
        self.hum.prepare()
        self.com.prepare()
        self.hum.make_move(list(self.hum.card.rows[0].keys())[1], False)
        assert self.hum.failed is True  # человек ошибся, флаг ошибки взведён
        assert self.hum.card.get_rest() == 15
        self.com.make_move(list(self.com.card.rows[0].keys())[1], False)
        assert self.com.failed is False  # а компьюер не ошибается
        assert self.com.card.get_rest() == 14
        # проверим, что когда зачеркнуты все 15 числе на карте, взводится флаг выигрыша
        self.hum.prepare()
        self.com.prepare()
        for i in range(3):
            for k in self.hum.card.rows[i]:
                self.hum.make_move(k, True)
            for k in self.com.card.rows[i]:
                self.com.make_move(k, True)
        assert self.hum.finished is True
        assert self.hum.card.get_rest() == 0
        assert self.com.finished is True
        assert self.com.card.get_rest() == 0
