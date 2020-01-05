"""
Консольная версия игры
"""
from modules.player import LottoPlayer
from modules.bag import LottoBag


class LottoConsole:

    def __init__(self):
        self.players = []
        self.bag = LottoBag()
        self.round_no = 0

    @staticmethod
    def show_main_menu():
        m_str = """************************************
**           ЛОТО                 **
************************************
** 1. Настройка участников игры   **
** 2. Посмотреть правила игры     **
** 3. Начать новую игру           **
** 4. Выход                       **
************************************"""
        print(m_str)

    @staticmethod
    def show_rules():
        m_str = """
***************************************************************************************************************
**                                           Правила игры                                                    **
***************************************************************************************************************
**                                                                                                           **
**   Игра состоит из специальных карточек, на которых отмечены числа, и бочонков с цифрами.                  **
** В игре используются числа от 1 до 90.                                                                     **
**                                                                                                           **
**   Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,                     **
** расположенных в столбце, соответствующем десятку числа. Например, числа от 1 до 9 находятся               **
** в первом столбце, от 10 до 19 - во втором и т.д. В девятом столбце находяся числа от 80 до 90.            **
** Все цифры в карточке уникальны.                                                                           **
**                                                                                                           **
**   Каждый ход выбирается случайный бочонок. Ваша задача: посмотрев на свою карточку, определить,           **
** нужно ли Вам зачеркнуть выпашее число или нет.                                                            **
**   В случае, если выпашее число есть в Вашей карточке:                                                     **
**     -- если Вы выбрали "зачеркнуть", то число зачеркивается, и Вы продолжаете игру                        **
**     -- если Вы выбрали "пропустить", то Вы проигрываете и выбываете из дальнейшей игры                    **
**   В случае, если выпашее число отсутствует в Вашей карточке:                                              **
**     -- если Вы выбрали "зачеркнуть", то Вы проигрываете и выбываете из дальнейшей игры                    **
**     -- если Вы выбрали "пропустить", то Вы продолжаете игру дальше.                                       **
**                                                                                                           **
**  Победителем считается тот, кто первым вычеркнет все числа на своей карточке,                             **
** или останется последним игроком.                                                                          **
**                                                                                                           **
** Вы можете задать любое количество соперников, указав, кто будет Вам противостоять:                        **
** человек или компьютер, но учтите, компьютер никогда не ошибается в зачеркивании чисел на своей карточке.  **
**                                                                                                           **
**        Удачной игры!                                                                                      **
**                                                                                                           **
***************************************************************************************************************
        """
        print(m_str)

    @staticmethod
    def show_player_card(p_player):
        print('\n')
        print('+' * 48)
        print(f'++ {p_player.name:^42} ++')
        print('+' * 48)
        for i in range(3):
            nums = []
            keys = list(p_player.card.rows[i].keys())
            keys.sort()
            j = 0
            for k in range(0, 81, 10):
                if j < 5 and keys[j] < (k + 10 if keys[j] < 90 else k + 20):
                    nums.append('--' if p_player.card.rows[i][keys[j]] else f'0{keys[j]}' if keys[j] < 10 else str(keys[j]))
                    j += 1
                else:
                    nums.append('  ')
            print(f'++ {" + ".join(nums)} ++')
            print('+' * 48)

    def check_round_results(self):
        m_rest_players = []
        m_win = []
        for player in self.players:
            if not player.failed:
                m_rest_players.append(player.name)
            if player.finished:
                m_win.append(player.name)
        if 1 == len(m_rest_players):
            m_return = m_rest_players[0]
        elif m_win:
            m_return = ', '.join(m_win)
        else:
            m_return = ''
        return m_return

    def start_new_game(self):
        if len(self.players) < 2:
            print('Ошибка! Количество участников меньше двух.')
            print('         Запустите настройку участников и заполните хотя бы двух игроков.')
            return None
        self.round_no = 0
        self.bag.shuffle()
        for player in self.players:
            player.prepare()
        while True:
            self.round_no += 1
            m_current = self.bag.get_number()
            if m_current > 0:
                print(f'\n\n>> Раунд: {self.round_no}. Выпало: {m_current}. Осталось чисел: {self.bag.get_rest()}')
                for player in self.players:
                    self.show_player_card(player)
                    if 'c' == player.kind:
                        print(f'>>  Игрок "{player.name}" сделал свой ход. ')
                        plr_act = True
                    else:
                        while True:
                            plr_act = input(f'>>  Ваш выбор ( [m] - зачеркнуть / [p] - продолжить): ')
                            if plr_act in 'mp':
                                plr_act = 'm' == plr_act
                                break
                            else:
                                print('>>    Пожалуйста, укажите допустимое значение!')
                    player.make_move(m_current, plr_act)
                    if player.failed:
                        print('!!! Вы допустили ошибку и выбываете из дальнейшей борьбы.')
                winner = self.check_round_results()
                if winner:
                    print('\n')
                    print(f'    На {self.round_no}-м ходу у нас определился победитель!!!')
                    print(f'    Это: {winner} !!!')
                    print('       ПОЗДРАВЛЯЕМ!!!')
                    print('\n')
                    break
            if not self.bag.get_rest():
                print('\n')
                print(f'    Все бочонки закончились...')
                print(f'    Боевая НИЧЬЯ!')
                print('\n')
                break

    def clear_players(self):
        self.players.clear()

    def add_player(self, p_kind):
        while 1:
            m_name = input('Задайте псевдоним: ')
            m_new = True
            for player in self.players:
                if player.name == m_name:
                    print('  !!! Ошибка: игрок с таким именем уже существует. попробуйте ещё раз.')
                    m_new = False
                    break
            if m_new:
                self.players.append(LottoPlayer(p_kind, m_name))
                break

    def show_setup_menu(self):
        print("""***************************************************
**                    Участники игры             **
***************************************************""")
        i = 1
        for player in self.players:
            print(f'   {i}. {player.name} ({"компьютер" if "c" == player.kind else "человек"})')
            i += 1
        if not self.players:
            print(f'   Нет зарегистрированных участников.')
        print("""***************************************************
** 1. Очистить список                            **
** 2. Добавить игрока под управлением компьютера **
** 3. Добавить игрока под управлением человека   **
** 4. Вернуться в основное меню                  **
***************************************************""")

    def setup_players(self):
        while 1:
            self.show_setup_menu()
            m_action = input('>>  Укажите действие: ')
            if '1' == m_action:
                self.clear_players()
            elif '2' == m_action:
                self.add_player('c')
            elif '3' == m_action:
                self.add_player('h')
            elif '4' == m_action:
                break
            else:
                print('    Неверная команда!')

    def __str__(self):
        return f'Класс "Консольная версия игры в лото". Сыграно раундов: {self.round_no}. Количество участников: {len(self.players)}.'

    def __eq__(self, other):
        is_equal = self.round_no == other.round_no and len(self.players) == len(other.players)
        if is_equal and len(self.players) > 0:
            for player in self.players:
                has_eq_player = False
                for other_player in other.players:
                    has_eq_player |= player == other_player
                is_equal &= has_eq_player
                if not is_equal:
                    break
        return is_equal


if '__main__' == __name__:
    m_game = LottoConsole()
    print(m_game)
    m_test = LottoConsole()
    print(m_test)
    print(m_game == m_test)
    print(m_game != m_test)
    m_game.setup_players()
    m_test.setup_players()
    print('After reg 1player for each game...')
    print(m_game)
    print(m_test)
    print(m_game == m_test)
    print(m_game != m_test)
    print('Cause of different cards players have...')
