import random

def play_connect_four_1():
    response = "yes"
    while response == "yes":
        empty_cells = 42 
        board = [ [ " ", " ", " ", " ", " ", " ", " ", " "],
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "],
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "]]
        users_turn = True 
        
        while not winner(board) and (empty_cells > 0):
            if users_turn:
                print_board(board)
                make_move(board)
                users_turn = False
            else:
                computer_move(board)
                users_turn = True
            empty_cells -= 1
        
        print_board(board)
        if winner(board) and not(users_turn): 
            print("Congrats! You won!\n")\
            
        if winner(board) and (users_turn):
            print("You lost!\n")
            
        if empty_cells == 0: 
            print("It's a tie!\n")
            
        response = input("Do you want to play again? yes or no \n")

def play_connect_four_2():
    response = "yes"
    while response == "yes":
        empty_cells = 42 
        board = [ [ " ", " ", " ", " ", " ", " ", " ", " "],
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "],
                  [ " ", " ", " ", " ", " ", " ", " ", " "], 
                  [ " ", " ", " ", " ", " ", " ", " ", " "]]
        player_1 = True 
        
        while not winner(board) and (empty_cells > 0):
            if player_1:
                print("Player 1's turn. ")
                print_board(board)
                make_move(board)
                player_1 = False
            else:
                print("Player 2's turn. ")
                print_board(board)
                make_move_2(board)
                player_1 = True
            empty_cells -= 1
        
        print_board(board)
        if winner(board) and not(player_1): 
            print("Congrats Player 2! You won!\n")\
            
        if winner(board) and (player_1): 
            print("Congrats Player 1! You won!\n")\
            
        if empty_cells == 0: 
            print("It's a tie!\n")
            
        response = input("Do you want to play again? yes or no \n")
        
def print_board(board):
    print("   1   2   3   4    5   6   7")
    print("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7])
    print("  ---+---+---+---+---+---+---")
    print("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board[1][6] + " | " + board[1][7])
    print("  ---+---+---+---+---+---+---")
    print("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board[2][4] + " | " + board[2][5] + " | " + board[2][6] + " | " + board[2][7])
    print("  ---+---+---+---+---+---+---")
    print("4: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board[3][4] + " | " + board[3][5] + " | " + board[3][6] + " | " + board[3][7])
    print("  ---+---+---+---+---+---+---")
    print("5: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | " + board [4][7])
    print("  ---+---+---+---+---+---+---+")
    print("6: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | " + board [5][7])
    print("\n")
    
def winner(board):
    ##horizontal win
    for row in range(6):
        for col in range(4):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]) and (board[row][col] != " "):
                return board[row][col]
                
    ##vertical win 
    for row in range(3): 
        for col in range(6): 
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] != " "):
                return board[row][col]
    
    ##horizontal win (bottom left to top right)
    for row in range(5, 2, -1): 
        for col in range(3): 
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] and board[row][col] != " "):
                return board[row][col]
                
    ##horizontal win (right to left)
    for row in range(3): 
        for col in range(4): 
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] != " "):
                return board[row][col]

    return ""
    
def make_move(board):
    try:
        valid_move = False
        while not valid_move:
            col = int(input("What col would you like to move to (1-7):"))
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
                    board[row-1][col-1] = 'X'
                    valid_move = True
                    break
            else:
                print("Sorry, invalid square. Please try again!\n")

    ##catch for all errors 
    except NameError:
        print("Only numbers are allowed.")

    except IndexError:
        print("You can only select columns from (1-7), and rows from (1-6).")
        
    except ValueError:
        print("Only numbers are allowed.")
        
def make_move_2(board):
    try:
        valid_move = False
        while not valid_move:
            col = int(input("What col would you like to move to (1-7):"))
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
                    board[row-1][col-1] = 'O'
                    valid_move = True
                    break
            else:
                print("Sorry, invalid square. Please try again!\n")

    ##catch for all errors 
    except NameError:
        print("Only numbers are allowed.")

    except IndexError:
        print("You can only select columns from (1-7), and rows from (1-6).")
        
    except ValueError:
        print("Only numbers are allowed.")
        
def computer_move(board):
    valid_move = False
    while not valid_move:
        row = random.randint(0,5)
        col = random.randint(0,6)
        for row in range (5,0,-1):
            if board[row][col] == " ":
                board[row][col] = "O"
                valid_move = True
                break

def word_guess(): 
    print("Welcome to Word Guesser! You have 5 attempts to guess what word I'm thinking of. You have two hints to help you. Good Luck!\n")
    response = 'yes'
    
    while response == "yes": 
        words = ['dog', 'cat', 'apple', 'tree']
        
        index = random.randint(0,3)
        word = words[index]
        guesses = 5
        hint_num = 2
        hints = [["I am man's best friend.", "I bark at things."],
                 ["I meow.","I lay around the house all day."],
                 ["Doctors reccomend you eat me.", "I can be red, green, or yellow."], 
                 ["I am green and brown", "Many creatures live in and on me."]]
        
        while (guesses > 0):
            print(guesses)
            guess = input("\nWhat is your guess?\n")
            if (guess == word): 
                print("Congrats! You got the word!") 
                break
            if (guess != word): 
                print("Wrong. Try again. You have %d hints remaining\n" % hint_num)
                if hint_num == 0: 
                    continue
                hint_request = input("Do you want a hint?\n")
                if hint_request == "yes":
                    print("\n")
                    print(hints[index][hint_num-1])
                    hint_num -= 1
            guesses -= 1
            
        if guesses == 0: 
            print("You lost! The word was %s." %word)
        
        response = input("Do you want to play again?\n")
    
if __name__ == '__main__': 
    print("Welcome Player! \n")
    print("a) Connect 4 (1 Player)\nb) Connect 4 (2 Player)\nc) Word Guesser")
    game = input("What game do you want to play?\n")
    if game == "a":
        play_connect_four_1() 
    if game == "b": 
        play_connect_four_2()
        
    if game == "c":
        word_guess()
    else: 
        print("Goodbye!")
