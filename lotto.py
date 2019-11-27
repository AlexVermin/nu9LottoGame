"""
Основной модуль игры в лото
"""
from modules.console_game import LottoConsole


if '__main__' == __name__:
    m_game = LottoConsole()
    while True:
        m_game.show_main_menu()
        m_choice = input('>> Ваш выбор: ')
        if '1' == m_choice:
            m_game.setup_players()
        elif '2' == m_choice:
            m_game.show_rules()
        elif '3' == m_choice:
            m_game.start_new_game()
        elif '4' == m_choice:
            break
