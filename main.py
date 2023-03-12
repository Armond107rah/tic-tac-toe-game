# | X | O | X |
# | X | O | X |
# | X | O | O |


def display_board(board):
    """
    Function to display the board in console
    :param board: board of the game
    :return:
    """
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_winner(board, current_player):
    """
    Main logic of the game which decides if the game is won by a player
    :param board: board of the game
    :param current_player: current players turn
    :return: true if winner else false
    """
    return ((board[0] == current_player and board[1] == current_player and board[2] == current_player) or
            (board[3] == current_player and board[4] == current_player and board[5] == current_player) or
            (board[6] == current_player and board[7] == current_player and board[8] == current_player) or
            (board[0] == current_player and board[3] == current_player and board[6] == current_player) or
            (board[1] == current_player and board[4] == current_player and board[7] == current_player) or
            (board[2] == current_player and board[5] == current_player and board[8] == current_player) or
            (board[0] == current_player and board[4] == current_player and board[8] == current_player) or
            (board[2] == current_player and board[4] == current_player and board[6] == current_player))


def get_user_input(board):
    """
    Function to get the user's position and check if that is valid
    :param board: game board
    :return: the position from 1-9
    """
    while True:
        try:
            position = int(input("Enter position from [1-9]:"))
            if position < 1 or position > 9:
                print("Invalid position entered, Please try again.")
            else:
                if board[position - 1] != " ":
                    print("Position already taken, Please try again.")
                else:
                    return position - 1
        except ValueError:
            print("Invalid position entered, Please try again.")


def display_output(winner):
    """
    Function that displays the winner or tie for a game
    :param winner: winner of game
    :return:
    """
    if winner:
        print("")
        print("-------------------")
        print(f"Congratulations!, player {winner}. You won the game")
        print("Game over!")
        print("-------------------")
    else:
        print("")
        print("-------------------")
        print("Game ended in tie.")
        print("Game over!")
        print("-------------------")


def main():
    """
    The main logic of the game
    :return:
    """
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("Welcome to Tic Tac Toe Game!")
    current_player = "X"
    winner = None
    display_board(board)

    # looping until a winner is not selected
    while not winner:
        print(f"{current_player}'s turn !")
        position = get_user_input(board)
        board[position] = current_player
        display_board(board)
        # checking if current player is winner
        if check_winner(board, current_player):
            winner = current_player

        # check if there is empty space in board
        if " " not in board:
            break

        # swapping the values of player after each turn
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"

    # displaying winner
    display_output(winner)


if __name__ == '__main__':
    # starting the game
    main()
