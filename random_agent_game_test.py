# -*- coding: utf-8 -*-

# Othello AI Project
# University Of California, Irvine
# Authors: Akshat Patel, Teja Kolli, Prakul Agarwal

# Game testing code for random agents.
# Measure wins, loses and other stats.

# Imports
from othello import Othello
from random_agent import RandomAgent
import time

# Global Variables
board_size = 8
number_of_games = 100

player_1_wins = 0
player_2_wins = 0
draw_games = 0

total_start_time = time.time()

for i in range(number_of_games):
    othello = Othello(board_size)
    player = 1
    start_time = time.time()
    while True:
        move = RandomAgent.pick_move(othello, player)
        if move != -1:
            othello.put(move, player)
        game_over = othello.is_game_over(player)
        player *= -1
        if game_over != None:
            if game_over == 0:
                draw_games += 1
            else:
                if game_over == 1:
                    player_1_wins += 1
                else:
                    player_2_wins += 1
            break
    end_time = time.time()
    # print 'Time taken for game ' + str(i) + ' is %.2f seconds.' % (end_time - start_time)

total_end_time = time.time()
print 'Total time taken for ' + str(number_of_games) + ' games is %.2f seconds.' % (total_end_time - total_start_time)
print '================\nFinal scores: '
print 'Player 1 won ' + str(player_1_wins) + ' times. '
print 'Player 2 won ' + str(player_2_wins) + ' times. '
print 'Game draw ' + str(draw_games) + ' times. '
