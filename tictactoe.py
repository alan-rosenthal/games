import random

class Board(object):
    game = []

    ##########################################################################
    #   Initialize the board for a new game
    ##########################################################################
    def __init__(self):

        self.game = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]
        return

    ##########################################################################
    #   Print the Board
    ##########################################################################
    def print(self):

        def display_cell(cell_num, whats_in_it):
            if whats_in_it == "X" or whats_in_it == "O":
                answer = " "
            else:
                answer = str(cell_num)

            return answer

        print("")
        print(" " + self.game[0][0] + " | " + self.game[0][1] + " | " + self.game[0][2] + "          " +
              display_cell(1, self.game[0][0]) + " | " + display_cell(2, self.game[0][1]) + " | " + display_cell(3, self.game[0][2]))
        print("-----------        ----------")
        print(" " + self.game[1][0] + " | " + self.game[1][1] + " | " + self.game[1][2] + "          " +
              display_cell(4, self.game[1][0]) + " | " + display_cell(5, self.game[1][1]) + " | " + display_cell(6, self.game[1][2]))
        print("-----------        ----------")
        print(" " + self.game[2][0] + " | " + self.game[2][1] + " | " + self.game[2][2] + "          " +
              display_cell(7, self.game[2][0]) + " | " + display_cell(8, self.game[2][1]) + " | " + display_cell(9, self.game[2][2]))
        return

    ##########################################################################
    #   Test to see if a cell on the board is empty or not
    ##########################################################################
    def is_cell_empty(self, r, c):

        return self.game[r][c] == " "

    ###########################################################################
    #   Is the game a tie (if the board is full and nobody has won)
    ###########################################################################
    def is_it_a_tie(self):

        number_of_moves = 0
        for r in range(0, 3):
            for c in range(0, 3):
                if not self.is_cell_empty(r, c):
                    number_of_moves += 1

        if number_of_moves == 9:
            print("")
            print("The game is a tie")
            answer = True
        else:
            answer = False

        return answer

    ##########################################################################
    #   See if anybody has 3 in a row
    ##########################################################################
    def did_someone_win(self):

        answer = False
        for who in ["X", "O"]:
            if ((self.game[0][0] == who and self.game[0][1] == who and self.game[0][2] == who) or
                (self.game[1][0] == who and self.game[1][1] == who and self.game[1][2] == who) or
                (self.game[2][0] == who and self.game[2][1] == who and self.game[2][2] == who) or
                (self.game[0][0] == who and self.game[1][0] == who and self.game[2][0] == who) or
                (self.game[0][1] == who and self.game[1][1] == who and self.game[2][1] == who) or
                (self.game[0][2] == who and self.game[1][2] == who and self.game[2][2] == who) or
                (self.game[0][0] == who and self.game[1][1] == who and self.game[2][2] == who) or
                (self.game[0][2] == who and self.game[1][1] == who and self.game[2][0] == who)):
                    print("")
                    print(who + " is the winner")
                    answer = True

        return answer


    ##########################################################################
    #   Let the player make a move
    ##########################################################################
    def player_makes_move(self):
        print("")
        print("Now it is the player's turn.  Pick a number that is shown above:")

        print("")
        while True:
            the_move = int(input("what is your (O) move --> "))
            r = int((the_move - 1) / 3)
            c = (the_move - 1) % 3

            if self.is_cell_empty(r, c):
                self.game[r][c] = "O"
                break

        return

    ##########################################################################
    #   Let the computer make a move
    ##########################################################################

    def computer_makes_move(self):
        if not self.is_it_a_tie():
            print("")
            print("The computer (X) makes a move.  And the new board is:")
            while True:
                r = random.randrange(0, 3)
                c = random.randrange(0, 3)
                if self.is_cell_empty(r, c):
                    self.game[r][c] = "X"
                    break
        else:
            print("It is a tie")

        return


####################################################################
###   Main
####################################################################

x = Board()
whose_turn = "COMPUTER"

while not x.is_it_a_tie():
    if whose_turn == "COMPUTER":
        x.computer_makes_move()
        x.print()
        if x.did_someone_win():
            print("")
            print("The computer is the winner")
            break
        else:
            whose_turn = "PLAYER"
    else:
        x.player_makes_move()
        x.print()
        if x.did_someone_win():
            print("")
            print("The player is the winner")
            break
        else:
            whose_turn = "COMPUTER"

print("")
print("Good bye")

