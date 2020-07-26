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

# ---------------------------3---------------------------
# ---------------------------2---------------------------
import random


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


def make_turn(x, coordinates):
    field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x
    possible_moves.remove([int(coordinates[0]), int(coordinates[1])])


def generate_move_easy():
    move = random.choice(possible_moves)
    return move


global field
# initializing field
# field = [[' ' for x in range(3)] for y in range(3)]
global possible_moves
# initializing possible moves for easy AI
# possible_moves = [[i, j] for i in range(1, 4) for j in range (1, 4)]


def play(player_1, player_2):
    draw_field()
    for i in range(1, 10):
        if i % 2:
            if player_1 == 'user':
                x_coordinates = input("Enter the coordinates: ").split()
                while True:
                    if check_input(x_coordinates):
                        break
                    x_coordinates = input("Enter the coordinates: ").split()
                make_turn('X', x_coordinates)
                draw_field()
                if finished('X'):
                    print(f"{'X'} wins")
                    break
            else:
                print('Making move level "easy"')
                x_coordinates = generate_move_easy()
                make_turn('X', x_coordinates)
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
                make_turn('O', y_coordinates)
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
            else:
                print('Making move level "easy"')
                y_coordinates = generate_move_easy()
                make_turn('O', y_coordinates)
                draw_field()
                if finished('O'):
                    print(f"{'O'} wins")
                    break
    else:
        draw_field()
        print("Draw")


while True:
    command = input("Input command:").split()
    possible_players = ['easy', 'user']
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
        # initializing possible moves for easy AI
        possible_moves = [[i, j] for i in range(1, 4) for j in range(1, 4)]
        play(command[1], command[2])
