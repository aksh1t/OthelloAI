# -*- coding: utf-8 -*-

# Othello AI Project
# University Of California, Irvine
# Authors: Akshat Patel, Teja Kolli, Prakul Agarwal

# Global Variables
board_size = 8

class Board:
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
        """ Places the disc at co-ordinates given by move. Assumes move to be valid
        :param move: tuple having x and y co-ordinates where you want to put the disc
        :param player: value should be 1 for player 1 and -1 for player 2
        :return: 0 for draw, player value if any player won, None otherwise
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

        return None

    def valid_moves(self, player):
        """ Returns a list of valid moves for the player, -1 if an error
        :param player:
        :return:
        """
        if not (player == 1 or player == -1):
            return -1

        opp = player * -1
        moves = []

        # Looping through each spot on the board
        for i in self.__rsize:
            for j in self.__rsize:

                # Skip if the spot is not empty
                if not self.__board[i][j] == 0:
                    continue

                # Looking in all the directions
                for d in self.__dir:

                    # Generates the next move in direction
                    md = self.__move_in_dir((i, j), d)

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
                        moves.append((i, j))
                        break

        # Returning list of moves
        return moves

    def draw(self):
        s = ''
        for i in self.__board:
            for j in i:
                if j == 0:
                    s += '. '
                else:
                    s += '● ' if j == 1 else '○ '
            s += '\n'
        print(s)

    def draw_with_valid_moves(self, player):
        v_m = self.valid_moves(player)
        s = ''
        for a, i in enumerate(self.__board):
            for b, j in enumerate(i):
                if (a, b) in v_m:
                    s += '▵ '
                elif j == 0:
                    s += '. '
                else:
                    s += '● ' if j == 1 else '○ '
            s += '\n'
        print(s)


class Othello:
    def __init__(self):
        self.board = Board(board_size)


import random

o = Othello()
p = 1
o.board.draw_with_valid_moves(p)

while True:
    v_m = o.board.valid_moves(p)
    a = None
    if len(v_m) > 0:
        a = o.board.put(random.choice(v_m), p)
    p *= -1
    o.board.draw_with_valid_moves(p)

    if a:
        if a == 0:
            print 'Game draw!'
        else:
            print 'Player ' + str(a) + ' won!'
        break
