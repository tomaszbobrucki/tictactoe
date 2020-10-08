# write your code here
# print("""X O X
# O X O
# X X O""")


def win(game, letter):
    new_g = [[game[j], game[j + 1], game[j + 2]] for j in range(0, len(game), 3)]
    # print(new_g)

    for h in range(3):
        if new_g[h][0] == new_g[h][1] == new_g[h][2] == letter:
            return True
    for h1 in range(3):
        if new_g[0][h1] == new_g[1][h1] == new_g[2][h1] == letter:
            return True
    if new_g[0][0] == new_g[1][1] == new_g[2][2] == letter or new_g[0][2] == new_g[1][1] == new_g[2][0] == letter:
        return True
    return False


def matrix_printing(matrix):
    print("---------")
    i = 0
    while i < len(matrix):
        print("|", matrix[i], matrix[i + 1], matrix[i + 2], "|")
        i += 3
    print("---------")


def putting_value(matrix1, a, b, sign1):
    list_matrix = [[matrix1[j], matrix1[j + 1], matrix1[j + 2]] for j in range(0, len(matrix1), 3)]
    if int(b) == 1:
        list_matrix[2][int(a) - 1] = sign1
    elif int(b) == 2:
        list_matrix[1][int(a) - 1] = sign1
    elif int(b) == 3:
        list_matrix[0][int(a) - 1] = sign1
    list_matrix_2 = [cc for aa in list_matrix for cc in aa]
    # print(list_matrix)
    # print(list_matrix_2)
    return list_matrix_2


def checking_value(matrix2, a, b):
    val = ["X", "O"]
    list_matrix = [[matrix2[j], matrix2[j + 1], matrix2[j + 2]] for j in range(0, len(matrix2), 3)]
    if (int(b) == 1 and list_matrix[2][int(a) - 1] in val) or (int(b) == 2 and list_matrix[1][int(a) - 1] in val) or (int(b) == 3 and list_matrix[0][int(a) - 1] in val):
        return True
    else:
        return False


third_stage = """
if abs(list_in.count("X") - list_in.count("O")) >= 2:
    print("Impossible")
elif win(list_in, "X") and win(list_in, "O"):
    print("Impossible")
elif win(list_in, "X"):
    print("X wins")
elif win(list_in, "O"):
    print("O wins")
elif list_in.count("X") + list_in.count("O") == 9:
    print("Draw")
else:
    print("Game not finished")"""

numbers = [1, 2, 3]


list_in = list(" " * 9)
matrix_printing(list_in)
sign = "X"

while True:
    x, y = input("Enter the coordinates: ").split()
    if not(x.isdigit() or y.isdigit()):
        print("You should enter numbers!")
    elif int(x) not in numbers or int(y) not in numbers:
        print("Coordinates should be from 1 to 3!")
    elif checking_value(list_in, x, y):
        print("This cell is occupied! Choose another one!")
    else:
        list_in = putting_value(list_in, x, y, sign)
        matrix_printing(list_in)

    if win(list_in, "X"):
        print("X wins")
        break
    elif win(list_in, "O"):
        print("O wins")
        break
    elif list_in.count("X") + list_in.count("O") == 9:
        print("Draw")
        break

    if sign == "X":
        sign = "O"
    else:
        sign = "X"
