import math
player_score = 0
ai_score = 0
games = 0
def print_board(board):
    print(" 0 1 2 \n 3 4 5 \n 6 7 8")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)
def is_draw(board):
    return " " not in board and not is_winner(board, "X") and not is_winner(board, "O")
def minimax(board, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0
    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(board, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(board, True))
                board[i] = " "
        return best
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def play():
    global player_score, ai_score, games
    board = [" "] * 9
    print("\nYou are X, AI is O")
    print_board(board)
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move.")
                continue
        except (ValueError, IndexError):
            print("Enter a number from 0–8.")
            continue
        board[move] = "X"
        if is_winner(board, "X"):
            print_board(board)
            player_score += 1
            ai_score -= 1
            games += 1
            print(f"You win! You: {player_score} AI: {ai_score} \n Game: {games}")
            return
        if is_draw(board):
            print_board(board)
            games += 1
            print(f"It's a draw! You: {player_score} AI: {ai_score} \n Game: {games}")
            return
        ai = best_move(board)
        board[ai] = "O"
        print(f"AI plays {ai}")
        print_board(board)
        if is_winner(board, "O"):
            ai_score += 1
            games += 1
            print(f"AI wins! You: {player_score} AI: {ai_score} \n Game: {games}")
            return
        if is_draw(board):
            games += 1
            print(f"It's a draw! You: {player_score} AI: {ai_score} \n Game: {games}")
            return
while True:
    play()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break