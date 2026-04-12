def create_grid():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return board

def display_grid(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            column = int(input(f"Player {player}, enter column (0-2): "))
            # checkin range
            if row not in [0,1,2] or column not in [0,1,2]:
                print("Invalid input. Please enter row and column.")
                continue
            # checking if empty
            if board[row][column] != " ":
                print("Cell is already taken. Try again.")
                continue
            return row, column
        except ValueError:
            print("Invalid input. Please enter row and column.")

def check_win(board, player):
    # check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # check columns
    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = create_grid()
    current_player = "X"

    while True:
        display_grid(board)
        row, column = player_input(board, current_player)
        board[row][column] = current_player

        # check win
        if check_win(board, current_player):
            display_grid(board)
            print(f"Player {current_player} wins!")
            break

        # check tie
        if check_tie(board):
            display_grid(board)
            print("It's a tie!")
            break

        # switch player:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

play()