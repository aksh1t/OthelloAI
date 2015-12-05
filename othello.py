# -*- coding: utf-8 -*-

# Othello AI Project
# University Of California, Irvine
# Authors: Akshat Patel, Teja Kolli, Prakul Agarwal

# Imports
import random

# Global Variables
board_size = 8


class Othello:
    def __init__(self, size):
        # Setting up size of the board
        self.__size = size if size > 3 else 4

        # Convenience variables to use in other functions
        self.__dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.__move_in_dir = lambda m, d: (m[0] + d[0], m[1] + d[1])
        self.__valid_move = lambda m: (self.__size > m[0] >= 0 and self.__size > m[1] >= 0)
        self.__rsize = range(self.__size)

        # Setting up empty board
        self.__board = [[0 for _ in self.__rsize] for _ in self.__rsize]

        # Setting up initial discs in the board
        s = self.__size // 2
        self.__board[s - 1][s - 1] = self.__board[s][s] = 1
        self.__board[s][s - 1] = self.__board[s - 1][s] = -1

        # Scores
        self.__score = {1: 2, -1: 2}

    def put(self, move, player):
        """ Places the disc at co-ordinates given by move. Assumes the move to be valid.
        :param move: tuple having x and y co-ordinates where you want to put the disc
        :param player: value should be 1 for player 1 and -1 for player 2
        :return: Nothing
        """
        # Optional Validations
        # --------------------
        # if move[0] < 0:
        #     return -1
        # if move[0] >= self.__size:
        #     return -1
        # if move[1] < 0:
        #     return -1
        # if move[1] >= self.__size:
        #     return -1
        # if not (player == 1 or player == -1):
        #     return -1
        #
        # # Generating all valid moves and checking if the given move is among those
        # if move not in self.valid_moves(player):
        #     return -1

        # Making the move
        self.__board[move[0]][move[1]] = player
        opp = player * -1

        # Increasing player's count
        self.__score[player] += 1

        # Check to see if discs need to be flipped
        for d in self.__dir:

            # Generates the next move in direction
            md = self.__move_in_dir(move, d)

            # Checks for validity of generated move
            if not self.__valid_move(md):
                continue

            # Checks if the generated move is not an opponent disc
            if self.__board[md[0]][md[1]] != opp:
                continue

            # Temporary variables
            needs_flipping = False
            next_move = md

            # We have found the next disc to be the opponent's disc, so going further
            while True:

                # Generate the next disc in line
                next_move = self.__move_in_dir(next_move, d)

                # We hit the end without finding our disc, so no flipping required
                if not self.__valid_move(next_move):
                    break

                # Found empty space in between, so no flipping required
                if self.__board[next_move[0]][next_move[1]] == 0:
                    break

                # We found our disc, so will need to flip the middle discs
                if self.__board[next_move[0]][next_move[1]] == player:
                    needs_flipping = True
                    break

            # Doing the actual flipping
            if needs_flipping:
                while True:

                    # Flip!
                    self.__board[md[0]][md[1]] = player

                    # Update scores
                    self.__score[player] += 1
                    self.__score[opp] -= 1

                    # Generate next move
                    md = self.__move_in_dir(md, d)

                    # Will flip till we find our own disc
                    if self.__board[md[0]][md[1]] == player:
                        break

    def is_game_over(self, player):
        """ Function to check if the game is over.
        :param player: The current player
        :return: 1 for player 1 win, -1 for player 2 win, 0 for draw, None otherwise
        """
        opp = player * -1

        # Check for opponent win!
        if self.__score[player] == 0:
            return opp

        # Check for player win!
        if self.__score[opp] == 0:
            return player

        # No space left for any move. Game Over!
        if self.__score[player] + self.__score[opp] == self.__size ** 2:
            if self.__score[player] > self.__score[opp]:
                return player
            elif self.__score[player] < self.__score[opp]:
                return opp
            else:
                return 0

        # No player can make a valid move
        if len(self.valid_moves(player)) == 0:
            if len(self.valid_moves(opp)) == 0:
                if self.__score[player] > self.__score[opp]:
                    return player
                elif self.__score[player] < self.__score[opp]:
                    return opp
                else:
                    return 0

    def valid_moves(self, player):
        """ Returns a list of valid moves for the player, -1 if an error.
        :param player: The current player
        :return: Returns a list of valid moves for the player or -1 if player is invalid
        """
        if not (player == 1 or player == -1):
            return -1

        opp = player * -1
        moves = []

        # Looping through each spot on the board
        for row in self.__rsize:
            for col in self.__rsize:

                # Skip if the spot is not empty
                if not self.__board[row][col] == 0:
                    continue

                # Looking in all the directions
                for d in self.__dir:

                    # Generates the next move in direction
                    md = self.__move_in_dir((row, col), d)

                    # Checks for validity of generated move
                    if not self.__valid_move(md):
                        continue

                    # Checks if the generated move is not an opponent disc
                    if self.__board[md[0]][md[1]] != opp:
                        continue

                    # Temporary variables
                    found_valid_position = False
                    next_move = md

                    # We have found the next disc to be the opponent's disc, so going further
                    while True:

                        # Generate the next disc in line
                        next_move = self.__move_in_dir(next_move, d)

                        # We hit the end without finding our disc, so no flipping required
                        if not self.__valid_move(next_move):
                            break

                        # Found empty space in between, so no flipping required
                        if self.__board[next_move[0]][next_move[1]] == 0:
                            break

                        # We found our disc, so will need to flip the middle discs
                        if self.__board[next_move[0]][next_move[1]] == player:
                            found_valid_position = True
                            break

                    # Found a valid position, so append this position to the list of valid moves
                    if found_valid_position:
                        moves.append((row, col))
                        break

        # Returning list of moves
        return moves

    def draw(self):
        """ Prints the board.
        :return: Nothing
        """
        valid_move_list = ''
        for row in self.__board:
            for disc in row:
                if disc == 0:
                    valid_move_list += '. '
                else:
                    valid_move_list += '● ' if disc == 1 else '○ '
            valid_move_list += '\n'
        print(valid_move_list)

    def draw_with_valid_moves(self, player):
        """ Prints the board and also shows the valid moves for one player.
        :param player: Player for whom we need to show the valid moves
        :return: Nothing
        """
        valid_move_list = self.valid_moves(player)
        string = ''
        for row, row_element in enumerate(self.__board):
            for col, disc in enumerate(row_element):
                if (row, col) in valid_move_list:
                    string += '▵ '
                elif disc == 0:
                    string += '. '
                else:
                    string += '● ' if disc == 1 else '○ '
            string += '\n'
        print(string)

#
#
# GAME TESTING CODE
#
#

p1w = 0
p2w = 0
dr = 0

for i in range(100):
    o = Othello(board_size)
    p = 1
    while True:
        v_m = o.valid_moves(p)
        if len(v_m) > 0:
            o.put(random.choice(v_m), p)
        # o.board.draw_with_valid_moves(p)
        a = o.is_game_over(p)
        p *= -1
        if a != None:
            if a == 0:
                dr += 1
                # print 'Game draw!'
            else:
                if a == 1:
                    p1w += 1
                else:
                    p2w += 1
                    # print 'Player ' + str(a) + ' won! ' + str(i)
            break

print '\n\n================\nFinal scores: '
print 'Player 1 won ' + str(p1w) + ' times. '
print 'Player 2 won ' + str(p2w) + ' times. '
print 'Game draw ' + str(dr) + ' times. '
