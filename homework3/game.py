class CrossesZeroes:
    # Класс для представления игры "Крестики-нолики

    def __init__(self) -> None:
        # Инициализация игровой доски и текущего игрока
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def draw_board(self) -> None:
        # Отображение игровой доски в терминале
        print('    A   B   C')
        print('  -------------')
        nom_row = 0
        for row in self.board:
            nom_row += 1
            print(f'{nom_row} |', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print('\n  -------------')

    def make_move(self, row: int, col: int) -> bool:
        """Проверка валидности хода и установка символа игрока на доску.
        Args:
        * row: номер строки.
        * col: номер столбца.

        return:
        True, если ход выполнен успешно,
        False в противном случае"""
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            # self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self, player: str) -> bool:
        """Проверка условий победы для заданного игрока.
        Args:
        * player: символ игрока ('X' или 'O').

        return:
        True, если игрок победил,
        False в противном случае"""
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
                    self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
                return True

        return False

    def input_validation(self, st) -> str:
        """ Проверка валидности введенных координат.
               Args:
               * st: введенная строка игроком.
               return:
               "0", если игрок ввел не валидную строку,
               row+col, координаты очередного хода, если ввод валиден"""
        row = ''
        col = ''
        st = st.replace(' ', '')
        if len(st) != 2:
            return "0"
        symbols = list(st)
        st_row = '123'  # допустимые символы координаты строки
        st_col = 'АаAaВвBbСсCc'  # допустимые символы координаты столбца (учитываем кириллицу и латиницу)
        for i in range(2):
            if symbols[i] in st_row:
                row = symbols[i]
            if symbols[i] in st_col:
                col = "ABC"[st_col.index(symbols[i]) // 4] 
        if col == '' or row == '':
            return "0"
        return row + col

    def play(self) -> None:
        """Начало игры.

        Игроки по очереди делают ходы до достижения условия победы одним из игроков
        или объявления ничьи.
        """
        while True:
            self.draw_board()
            pl = "ноликов" if self.current_player == "O" else "крестиков"
            print(f'Ход {pl}')
            string_coordinates = input('Введите координаты (2 символа): ')
            valid_coordinates = self.input_validation(string_coordinates)
            if valid_coordinates == '0':
                print('Введенные координаты некорректны. Повторите ввод!')
                continue
            print(f'{valid_coordinates=}')
            row = int(valid_coordinates[0]) - 1
            col = int(ord(valid_coordinates[1])) - 65  # Перевод "буквенной координаты" в числовую

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.draw_board()
                    print('Игрок', pl, 'победил!')
                    break

                if all(cell != ' ' for row in self.board for cell in row):
                    self.draw_board()
                    print('Ничья.')
                    break

            else:
                print('В эту клетку уже сделан ход. Повторите ввод.')
                continue
            self.current_player = "OX"[("OX".index(self.current_player) + 1) % 2]  # переход хода на другого игрока