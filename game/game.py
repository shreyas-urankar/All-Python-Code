def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    for _ in range(9):
        row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)
            if check_winner(board):
                print(f"Player {player} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")
    
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
