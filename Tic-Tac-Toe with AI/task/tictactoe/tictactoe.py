# ---------------------------1---------------------------


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
        if coordinate < 0 or coordinate > 3:
            print("Coordinates should be from 1 to 3!")
            return False
    if field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def make_turn(x, coordinates):
    field[3 - int(coordinates[1])][int(coordinates[0]) - 1] = x
    global moves
    moves += 1


def print_status():

    # check whether 'X' wins
    result = [field[0][0] == field[1][1] == field[2][2] == 'X', field[2][0] == field[1][1] == field[0][2] == 'X']
    result.extend([field[j][0] == field[j][1] == field[j][2] == 'X' for j in range(0, 3)])
    result.extend([field[0][j] == field[1][j] == field[2][j] == 'X' for j in range(0, 3)])
    if any(result):
        print("X wins")
        return

    # check whether 'O' wins
    result = [field[0][0] == field[1][1] == field[2][2] == 'O', field[2][0] == field[1][1] == field[0][2] == 'O']
    result.extend([field[j][0] == field[j][1] == field[j][2] == 'O' for j in range(0, 3)])
    result.extend([field[0][j] == field[1][j] == field[2][j] == 'O' for j in range(0, 3)])
    if any(result):
        print("O wins")
        return

    # check if game not finished
    if moves < 9:
        print("Game not finished")
        return

    print("Draw")
    return


global field
global moves
instructions = input("Enter cells: ")
instructions = instructions.replace('_', ' ')
field = [[instructions[i * 3], instructions[i * 3 + 1], instructions[i * 3 + 2]] for i in range(0, 3)]

draw_field()
x_coordinates = input("Enter the coordinates: ").split()

moves = instructions.count('X') + instructions.count('O')
move = 'O' if moves % 2 else 'X'

while True:
    if check_input(x_coordinates):
        make_turn(move, x_coordinates)
        break
    x_coordinates = input("Enter the coordinates: ").split()

draw_field()
print_status()
