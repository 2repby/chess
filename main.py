WHITE = 1
BLACK = 2

class Pawn:

    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))

class Rook:

    def __init__(self, color):
        self.color = color

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку,
        # которая не лежит в том же ряду или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

class Knight:

    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        row1, col1 = self.row + 2, self.col + 1
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row + 2, self.col - 1
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row - 2, self.col + 1
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row - 2, self.col - 1
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row + 1, self.col + 2
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row + 1, self.col - 2
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row - 1, self.col + 2
        if row == row1 and col == col1:
            return True
        row1, col1 = self.row - 1, self.col - 2
        if row == row1 and col == col1:
            return True

        return False

class Bishop:

    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if row > self.row and col > self.col:
            if row - self.row == col - self.col:
                return True
        if row > self.row and col < self.col:
            if row - self.row == self.col - col:
                return True
        if row < self.row and col < self.col:
            if self.row - row == self.col - col:
                return True
        if row < self.row and col > self.col:
            if self.row - row == col - self.col:
                return True
        return False


class Queen:
    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move_old(self, board, row, col, row1, col1):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        rook = Rook(self.row, self.col, self.color)
        bishop = Bishop(self.row, self.col, self.color)
        if rook.can_move(row, col) or bishop.can_move(row, col):
            return True
        return False
    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку,
        # которая не лежит в том же ряду или столбце клеток.
        if row != row1 and col != col1:
            return False

        step_y = 1 if (row1 >= row) else -1
        step_x = 1 if (col1 >= col) else -1
        for r in range(row + step_y, row1, step_y):
            for c in range(col + step_x, col1, step_x):
            # Если на пути по вертикали есть фигура
                if not (board.get_piece(r, c) is None):
                    return False
        #
        # step = 1 if (col1 >= col) else -1
        # for c in range(col + step, col1, step):
        #     # Если на пути по горизонтали есть фигура
        #     if not (board.get_piece(row, c) is None):
        #         return False
        return True


class King:
    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        rook = Rook(self.row, self.col, self.color)
        bishop = Bishop(self.row, self.col, self.color)
        if rook.can_move(row, col) or bishop.can_move(row, col):
            return True
        return False
    def can_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        rook = Rook(self.row, self.col, self.color)
        bishop = Bishop(self.row, self.col, self.color)
        for x in range(self.col, col):
            for y in range(self.row, row):
                if rook.can_move(y, x) or bishop.can_move(y, x):
                    return True
        return False


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None
# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE

def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8

def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()

def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


# main()

WHITE=1
BLACK=2

board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
board.field[2][3] = Bishop(WHITE)
board.field[0][5] = Rook(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()