# ---------------------------1---------------------------


# def draw_field():
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
#     output += "---------"
#     print(output)
#
#
# def check_input(coordinates):
#     for coordinate in coordinates:
#         if not coordinate.isnumeric():
#             print("You should enter numbers!")
#             return False
#     coordinates = [int(x) for x in coordinates]
#     for coordinate in coordinates:
#         if coordinate < 0 or coordinate > 3:
#             print("Coordinates should be from 1 to 3!")
#             return False
#     if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
#         print("This cell is occupied! Choose another one!")
#         return False
#     return True
#
#
# def make_turn(x, coordinates):
#     field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x
#     global moves
#     moves += 1
#
#
# def print_status():
#
#     # check whether 'X' wins
#     result = [field[0][0] == field[1][1] == field[2][2] == 'X', field[2][0] == field[1][1] == field[0][2] == 'X']
#     result.extend([field[j][0] == field[j][1] == field[j][2] == 'X' for j in range(0, 3)])
#     result.extend([field[0][j] == field[1][j] == field[2][j] == 'X' for j in range(0, 3)])
#     if any(result):
#         print("X wins")
#         return
#
#     # check whether 'O' wins
#     result = [field[0][0] == field[1][1] == field[2][2] == 'O', field[2][0] == field[1][1] == field[0][2] == 'O']
#     result.extend([field[j][0] == field[j][1] == field[j][2] == 'O' for j in range(0, 3)])
#     result.extend([field[0][j] == field[1][j] == field[2][j] == 'O' for j in range(0, 3)])
#     if any(result):
#         print("O wins")
#         return
#
#     # check if game not finished
#     if moves < 9:
#         print("Game not finished")
#         return
#
#     print("Draw")
#     return
#
#
# global field
# global moves
# instructions = input("Enter cells: ")
# instructions = instructions.replace('_', ' ')
# field = [[instructions[i * 3], instructions[i * 3 + 1], instructions[i * 3 + 2]] for i in range(0, 3)]
#
# draw_field()
# x_coordinates = input("Enter the coordinates: ").split()
#
# moves = instructions.count('X') + instructions.count('O')
# move = 'O' if moves % 2 else 'X'
#
# while True:
#     if check_input(x_coordinates):
#         make_turn(move, x_coordinates)
#         break
#     x_coordinates = input("Enter the coordinates: ").split()
#
# draw_field()
# print_status()

# ---------------------------2---------------------------
# import random
#
#
# def draw_field():
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
#     output += "---------"
#     print(output)
#
# def check_input(coordinates):
#     for coordinate in coordinates:
#         if not coordinate.isnumeric():
#             print("You should enter numbers!")
#             return False
#     coordinates = [int(x) for x in coordinates]
#     for coordinate in coordinates:
#         if coordinate < 0 or coordinate > 3:
#             print("Coordinates should be from 1 to 3!")
#             return False
#     if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
#         print("This cell is occupied! Choose another one!")
#         return False
#     return True
#
#
# def finished(x):
#     result = [field[0][0] == field[1][1] == field[2][2] == x, field[2][0] == field[1][1] == field[0][2] == x]
#     result.extend([field[j][0] == field[j][1] == field[j][2] == x for j in range(0, 3)])
#     result.extend([field[0][j] == field[1][j] == field[2][j] == x for j in range(0, 3)])
#     return any(result)
#
#
# def make_turn(x, coordinates):
#     field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x
#     possible_moves.remove([int(coordinates[0]), int(coordinates[1])])
#
#
# def generate_move_easy():
#     move = random.choice(possible_moves)
#     return move
#
#
# global field
# # initializing field
# field = [[' ' for x in range(3)] for y in range(3)]
# global possible_moves
# # initializing possible moves for easy AI
# possible_moves = [[i, j] for i in range(1, 4) for j in range (1, 4)]
#
# # starting main cycle
# draw_field()
# for i in range(1, 10):
#     if i % 2:
#         x_coordinates = input("Enter the coordinates: ").split()
#         while True:
#             if check_input(x_coordinates):
#                 break
#             x_coordinates = input("Enter the coordinates: ").split()
#         make_turn('X', x_coordinates)
#         draw_field()
#         if finished('X'):
#             print(f"{'X'} wins")
#             break
#     else:
#         print('Making move level "easy"')
#         y_coordinates = generate_move_easy()
#         make_turn('O', y_coordinates)
#         draw_field()
#         if finished('O'):
#             print(f"{'O'} wins")
#             break
# else:
#     draw_field()
#     print("Draw")

# # ---------------------------3---------------------------
# import random
#
#
# def draw_field():
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
#     output += "---------"
#     print(output)
#
#
# def check_input(coordinates):
#     for coordinate in coordinates:
#         if not coordinate.isnumeric():
#             print("You should enter numbers!")
#             return False
#     coordinates = [int(x) for x in coordinates]
#     for coordinate in coordinates:
#         if coordinate <= 0 or coordinate > 3:
#             print("Coordinates should be from 1 to 3!")
#             return False
#     if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
#         print("This cell is occupied! Choose another one!")
#         return False
#     return True
#
#
# def finished(x):
#     result = [field[0][0] == field[1][1] == field[2][2] == x, field[2][0] == field[1][1] == field[0][2] == x]
#     result.extend([field[j][0] == field[j][1] == field[j][2] == x for j in range(0, 3)])
#     result.extend([field[0][j] == field[1][j] == field[2][j] == x for j in range(0, 3)])
#     return any(result)
#
#
# def make_turn(x, coordinates):
#     field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x
#     possible_moves.remove([int(coordinates[0]), int(coordinates[1])])
#
#
# def generate_move_easy():
#     move = random.choice(possible_moves)
#     return move
#
#
# global field
# # initializing field
# # field = [[' ' for x in range(3)] for y in range(3)]
# global possible_moves
# # initializing possible moves for easy AI
# # possible_moves = [[i, j] for i in range(1, 4) for j in range (1, 4)]
#
#
# def play(player_1, player_2):
#     draw_field()
#     for i in range(1, 10):
#         if i % 2:
#             if player_1 == 'user':
#                 x_coordinates = input("Enter the coordinates: ").split()
#                 while True:
#                     if check_input(x_coordinates):
#                         break
#                     x_coordinates = input("Enter the coordinates: ").split()
#                 make_turn('X', x_coordinates)
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#             else:
#                 print('Making move level "easy"')
#                 x_coordinates = generate_move_easy()
#                 make_turn('X', x_coordinates)
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#         else:
#             if player_2 == 'user':
#                 y_coordinates = input("Enter the coordinates: ").split()
#                 while True:
#                     if check_input(y_coordinates):
#                         break
#                     y_coordinates = input("Enter the coordinates: ").split()
#                 make_turn('O', y_coordinates)
#                 draw_field()
#                 if finished('O'):
#                     print(f"{'O'} wins")
#                     break
#             else:
#                 print('Making move level "easy"')
#                 y_coordinates = generate_move_easy()
#                 make_turn('O', y_coordinates)
#                 draw_field()
#                 if finished('O'):
#                     print(f"{'O'} wins")
#                     break
#     else:
#         draw_field()
#         print("Draw")
#
#
# while True:
#     command = input("Input command:").split()
#     possible_players = ['easy', 'user']
#     if len(command) == 0:
#         print("Bad parameters!")
#         break
#     if len(command) == 1 and command[0] == 'exit':
#         break
#     if (len(command) != 3 or command[0] != 'start' or command[1] not in possible_players
#             or command[2] not in possible_players):
#         print("Bad parameters!")
#     else:
#         # initializing field
#         field = [[' ' for x in range(3)] for y in range(3)]
#         # initializing possible moves for easy AI
#         possible_moves = [[i, j] for i in range(1, 4) for j in range(1, 4)]
#         play(command[1], command[2])

# # ---------------------------4---------------------------
# import random
#
#
# class Player:
#     def __init__(self, mark):
#         self.mark = mark
#
#     def make_turn(self, coordinates):
#         field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = self.mark
#         possible_moves.remove([int(coordinates[0]), int(coordinates[1])])
#
#
# class User(Player):
#     pass
#
#
# class AI(Player):
#     def make_random_move(self):
#         move = random.choice(possible_moves)
#         self.make_turn(move)
#
#
# class EasyAI(AI):
#     pass
#
#
# class MediumAI(AI):
#     # check rule 1 - if can win in 1 move
#     def check_rule_1(self):
#         # check diagonal from left upper to right bottom
#         if field[0][0] == field[1][1] == self.mark:
#             self.make_turn([3, 1])
#             return True
#         if field[0][0] == field[2][2] == self.mark:
#             self.make_turn([2, 2])
#             return True
#         if field[1][1] == field[2][2] == self.mark:
#             self.make_turn([1, 3])
#             return True
#         # check diagonal from left bottom to right upper
#         if field[2][0] == field[1][1] == self.mark:
#             self.make_turn([3, 3])
#             return True
#         if field[1][1] == field[0][2] == self.mark:
#             self.make_turn([1, 1])
#             return True
#         if field[2][0] == field[0][2] == self.mark:
#             self.make_turn([2, 2])
#             return True
#         # check rows
#         for i in range(3):
#             if field[i][0] == field[i][2] == self.mark:
#                 self.make_turn([2, 3 - i])
#                 return True
#             if field[i][0] == field[i][1] == self.mark:
#                 self.make_turn([3, 3 - i])
#                 return True
#             if field[i][1] == field[i][2] == self.mark:
#                 self.make_turn([1, 3 - i])
#                 return True
#         # check columns
#         for i in range(3):
#             if field[0][i] == field[2][i] == self.mark:
#                 self.make_turn([i + 1, 2])
#                 return True
#             if field[0][i] == field[1][i] == self.mark:
#                 self.make_turn([i + 1, 1])
#                 return True
#             if field[1][i] == field[2][i] == self.mark:
#                 self.make_turn([i + 1, 3])
#                 return True
#         return False
#
#     # check rule 2 - if can lose in 1 move
#     def check_rule_2(self):
#         if self.mark == 'X':
#             opposite_mark = 'O'
#         else:
#             opposite_mark = 'X'
#         # check diagonal from left upper to right bottom
#         if field[0][0] == field[1][1] == opposite_mark:
#             self.make_turn([3, 1])
#             return True
#         if field[0][0] == field[2][2] == opposite_mark:
#             self.make_turn([2, 2])
#             return True
#         if field[1][1] == field[2][2] == opposite_mark:
#             self.make_turn([1, 3])
#             return True
#         # check diagonal from left bottom to right upper
#         if field[2][0] == field[1][1] == opposite_mark:
#             self.make_turn([3, 3])
#             return True
#         if field[1][1] == field[0][2] == opposite_mark:
#             self.make_turn([1, 1])
#             return True
#         if field[2][0] == field[0][2] == opposite_mark:
#             self.make_turn([2, 2])
#             return True
#         # check rows
#         for i in range(3):
#             if field[i][0] == field[i][2] == opposite_mark:
#                 self.make_turn([2, 3 - i])
#                 return True
#             if field[i][0] == field[i][1] == opposite_mark:
#                 self.make_turn([3, 3 - i])
#                 return True
#             if field[i][1] == field[i][2] == opposite_mark:
#                 self.make_turn([1, 3 - i])
#                 return True
#         # check columns
#         for i in range(3):
#             if field[0][i] == field[2][i] == opposite_mark:
#                 self.make_turn([i + 1, 2])
#                 return True
#             if field[0][i] == field[1][i] == opposite_mark:
#                 self.make_turn([i + 1, 1])
#                 return True
#             if field[1][i] == field[2][i] == opposite_mark:
#                 self.make_turn([i + 1, 3])
#                 return True
#         return False
#
#
# def draw_field():
#     output = "---------\n"
#     for i in range(0, 3):
#         output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
#     output += "---------"
#     print(output)
#
#
# def check_input(coordinates):
#     for coordinate in coordinates:
#         if not coordinate.isnumeric():
#             print("You should enter numbers!")
#             return False
#     coordinates = [int(x) for x in coordinates]
#     for coordinate in coordinates:
#         if coordinate <= 0 or coordinate > 3:
#             print("Coordinates should be from 1 to 3!")
#             return False
#     if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
#         print("This cell is occupied! Choose another one!")
#         return False
#     return True
#
#
# def finished(x):
#     result = [field[0][0] == field[1][1] == field[2][2] == x, field[2][0] == field[1][1] == field[0][2] == x]
#     result.extend([field[j][0] == field[j][1] == field[j][2] == x for j in range(0, 3)])
#     result.extend([field[0][j] == field[1][j] == field[2][j] == x for j in range(0, 3)])
#     return any(result)
#
#
# def play(player_1, player_2):
#     draw_field()
#     if player_1 == 'user':
#         player1 = User('X')
#     elif player_1 == 'easy':
#         player1 = EasyAI('X')
#     else:
#         player1 = MediumAI('X')
#     if player_2 == 'user':
#         player2 = User('O')
#     elif player_2 == 'easy':
#         player2 = EasyAI('O')
#     else:
#         player2 = MediumAI('O')
#     for i in range(1, 10):
#         if i % 2:
#             if player_1 == 'user':
#                 x_coordinates = input("Enter the coordinates: ").split()
#                 while True:
#                     if check_input(x_coordinates):
#                         break
#                     x_coordinates = input("Enter the coordinates: ").split()
#                 player1.make_turn(x_coordinates)
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#             elif player1 == 'medium':
#                 print('Making move level "medium"')
#                 if not player1.check_rule_1() and not player1.check_rule_2():
#                     player1.make_random_move()
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#             else:
#                 print('Making move level "easy"')
#                 player1.make_random_move()
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#         else:
#             if player_2 == 'user':
#                 y_coordinates = input("Enter the coordinates: ").split()
#                 while True:
#                     if check_input(y_coordinates):
#                         break
#                     y_coordinates = input("Enter the coordinates: ").split()
#                 player2.make_turn(y_coordinates)
#                 draw_field()
#                 if finished('O'):
#                     print(f"{'O'} wins")
#                     break
#             elif player2 == 'medium':
#                 print('Making move level "medium"')
#                 if not player2.check_rule_1() and not player2.check_rule_2():
#                     player2.make_random_move()
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#             else:
#                 print('Making move level "easy"')
#                 player2.make_random_move()
#                 draw_field()
#                 if finished('X'):
#                     print(f"{'X'} wins")
#                     break
#     else:
#         print("Draw")
#
#
# global field
# global possible_moves
#
# while True:
#     command = input("Input command:").split()
#     possible_players = ['easy', 'medium', 'user']
#     if len(command) == 0:
#         print("Bad parameters!")
#         break
#     if len(command) == 1 and command[0] == 'exit':
#         break
#     if (len(command) != 3 or command[0] != 'start' or command[1] not in possible_players
#             or command[2] not in possible_players):
#         print("Bad parameters!")
#     else:
#         # initializing field
#         field = [[' ' for x in range(3)] for y in range(3)]
#         # initializing possible moves for AI
#         possible_moves = [[i, j] for i in range(1, 4) for j in range(1, 4)]
#         play(command[1], command[2])

# ---------------------------5---------------------------
import random


class Player:
    def __init__(self, mark):
        self.mark = mark

    def make_turn(self, coordinates):
        field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = self.mark
        possible_moves.remove([int(coordinates[0]), int(coordinates[1])])


class User(Player):
    pass


class AI(Player):
    def make_random_move(self):
        move = random.choice(possible_moves)
        self.make_turn(move)


class EasyAI(AI):
    pass


class MediumAI(AI):
    # check rule 1 - if can win in 1 move
    def check_rule_1(self):
        # check diagonal from left upper to right bottom
        if field[0][0] == field[1][1] == self.mark:
            self.make_turn([3, 1])
            return True
        if field[0][0] == field[2][2] == self.mark:
            self.make_turn([2, 2])
            return True
        if field[1][1] == field[2][2] == self.mark:
            self.make_turn([1, 3])
            return True
        # check diagonal from left bottom to right upper
        if field[2][0] == field[1][1] == self.mark:
            self.make_turn([3, 3])
            return True
        if field[1][1] == field[0][2] == self.mark:
            self.make_turn([1, 1])
            return True
        if field[2][0] == field[0][2] == self.mark:
            self.make_turn([2, 2])
            return True
        # check rows
        for i in range(3):
            if field[i][0] == field[i][2] == self.mark:
                self.make_turn([2, 3 - i])
                return True
            if field[i][0] == field[i][1] == self.mark:
                self.make_turn([3, 3 - i])
                return True
            if field[i][1] == field[i][2] == self.mark:
                self.make_turn([1, 3 - i])
                return True
        # check columns
        for i in range(3):
            if field[0][i] == field[2][i] == self.mark:
                self.make_turn([i + 1, 2])
                return True
            if field[0][i] == field[1][i] == self.mark:
                self.make_turn([i + 1, 1])
                return True
            if field[1][i] == field[2][i] == self.mark:
                self.make_turn([i + 1, 3])
                return True
        return False

    # check rule 2 - if can lose in 1 move
    def check_rule_2(self):
        if self.mark == 'X':
            opposite_mark = 'O'
        else:
            opposite_mark = 'X'
        # check diagonal from left upper to right bottom
        if field[0][0] == field[1][1] == opposite_mark:
            self.make_turn([3, 1])
            return True
        if field[0][0] == field[2][2] == opposite_mark:
            self.make_turn([2, 2])
            return True
        if field[1][1] == field[2][2] == opposite_mark:
            self.make_turn([1, 3])
            return True
        # check diagonal from left bottom to right upper
        if field[2][0] == field[1][1] == opposite_mark:
            self.make_turn([3, 3])
            return True
        if field[1][1] == field[0][2] == opposite_mark:
            self.make_turn([1, 1])
            return True
        if field[2][0] == field[0][2] == opposite_mark:
            self.make_turn([2, 2])
            return True
        # check rows
        for i in range(3):
            if field[i][0] == field[i][2] == opposite_mark:
                self.make_turn([2, 3 - i])
                return True
            if field[i][0] == field[i][1] == opposite_mark:
                self.make_turn([3, 3 - i])
                return True
            if field[i][1] == field[i][2] == opposite_mark:
                self.make_turn([1, 3 - i])
                return True
        # check columns
        for i in range(3):
            if field[0][i] == field[2][i] == opposite_mark:
                self.make_turn([i + 1, 2])
                return True
            if field[0][i] == field[1][i] == opposite_mark:
                self.make_turn([i + 1, 1])
                return True
            if field[1][i] == field[2][i] == opposite_mark:
                self.make_turn([i + 1, 3])
                return True
        return False


def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append([i, j])
    return moves


def minimax(board, mark, state):

    # check for terminal states
    if mark == 'X':
        opposite_mark = 'O'
    else:
        opposite_mark = 'X'

    if state:
        if finished(mark):
            return 10
        elif finished(opposite_mark):
            return -10
        elif len(available_moves(board)) == 0:
            return 0
    else:
        if finished(mark):
            return -10
        elif finished(opposite_mark):
            return 10
        elif len(available_moves(board)) == 0:
            return 0

    moves = []
    i = 0
    for move in available_moves(board):
        board[move[0]][move[1]] = mark
        moves.append([move, minimax(board, opposite_mark, not state)])
        # moves[i][1] = minimax(board, opposite_mark, not state)
        board[move[0]][move[1]] = ' '
        i += 1

    bestMove = [[0, 0], -10000]
    for move in moves:
        if move[1] > bestMove[1]:
            bestMove = move

    return bestMove[0]


class HardAI(AI):
    def make_move(self):
        self.make_turn(minimax(field, self.mark, True))


def draw_field():
    output = "---------\n"
    for i in range(0, 3):
        output += f"| {field[i][0]} {field[i][1]} {field[i][2]} |\n"
    output += "---------"
    print(output)


def check_input(coordinates):
    for coordinate in coordinates:
        if not coordinate.isnumeric():
            print("You should enter numbers!")
            return False
    coordinates = [int(x) for x in coordinates]
    for coordinate in coordinates:
        if coordinate <= 0 or coordinate > 3:
            print("Coordinates should be from 1 to 3!")
            return False
    if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def finished(x):
    result = [field[0][0] == field[1][1] == field[2][2] == x, field[2][0] == field[1][1] == field[0][2] == x]
    result.extend([field[j][0] == field[j][1] == field[j][2] == x for j in range(0, 3)])
    result.extend([field[0][j] == field[1][j] == field[2][j] == x for j in range(0, 3)])
    return any(result)


def play(player_1, player_2):
    draw_field()
    if player_1 == 'user':
        player1 = User('X')
    elif player_1 == 'easy':
        player1 = EasyAI('X')
    elif player_1 == 'medium':
        player1 = MediumAI('X')
    else:
        player1 = HardAI('X')
    if player_2 == 'user':
        player2 = User('O')
    elif player_2 == 'easy':
        player2 = EasyAI('O')
    elif player_2 == 'medium':
        player2 = MediumAI('O')
    else:
        player2 = HardAI('O')
    for i in range(1, 10):
        if i % 2:
            if player_1 == 'user':
                x_coordinates = input("Enter the coordinates: ").split()
                while True:
                    if check_input(x_coordinates):
                        break
                    x_coordinates = input("Enter the coordinates: ").split()
                player1.make_turn(x_coordinates)
                draw_field()
                if finished('X'):
                    print(f"{'X'} wins")
                    break
            elif player_1 == 'medium':
                print('Making move level "medium"')
                if not player1.check_rule_1() and not player1.check_rule_2():
                    player1.make_random_move()
                draw_field()
                if finished('X'):
                    print(f"{'X'} wins")
                    break
            elif player_1 == 'hard':
                print('Making move level "hard"')
                player1.make_move()
                draw_field()
                if finished('X'):
                    print(f"{'X'} wins")
                    break
            else:
                print('Making move level "easy"')
                player1.make_random_move()
                draw_field()
                if finished('X'):
                    print(f"{'X'} wins")
                    break
        else:
            if player_2 == 'user':
                y_coordinates = input("Enter the coordinates: ").split()
                while True:
                    if check_input(y_coordinates):
                        break
                    y_coordinates = input("Enter the coordinates: ").split()
                player2.make_turn(y_coordinates)
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
            elif player_2 == 'medium':
                print('Making move level "medium"')
                if not player2.check_rule_1() and not player2.check_rule_2():
                    player2.make_random_move()
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
            elif player_2 == 'hard':
                print('Making move level "hard"')
                player2.make_move()
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
            else:
                print('Making move level "easy"')
                player2.make_random_move()
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
    else:
        print("Draw")


global field
global possible_moves

while True:
    command = input("Input command:").split()
    possible_players = ['easy', 'medium', 'user', 'hard']
    if len(command) == 0:
        print("Bad parameters!")
        break
    if len(command) == 1 and command[0] == 'exit':
        break
    if (len(command) != 3 or command[0] != 'start' or command[1] not in possible_players
            or command[2] not in possible_players):
        print("Bad parameters!")
    else:
        # initializing field
        field = [[' ' for x in range(3)] for y in range(3)]
        # initializing possible moves for AI
        possible_moves = [[i, j] for i in range(1, 4) for j in range(1, 4)]
        play(command[1], command[2])