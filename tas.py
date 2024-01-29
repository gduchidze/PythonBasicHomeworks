board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

player = 'X'

def print_board():
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print()

while True:
    print_board()

    try:
        move = int(input(f"{player}, enter the number: "))

        if not (1 <= move <= 9):
            print("Enter a number between 1 and 9.")
            continue

        found = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    if board[i][j] == 'X' or board[i][j] == 'O':
                        print("Already occupied. Try again.")
                    else:
                        board[i][j] = player
                        found = True
                        break

        if not found:
            print("Enter a valid square number.")
            continue

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
                print_board()
                print("Player", player, "wins!")
                exit()

        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            print_board()
            print("Player", player, "wins!")
            exit()

        player = 'O' if player == 'X' else 'X'

    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid move. Please enter a valid square number.")

    if all(isinstance(cell, str) for row in board for cell in row):
        print_board()
        print("It's a tie!")
        break
