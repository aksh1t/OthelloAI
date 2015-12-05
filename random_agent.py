# -*- coding: utf-8 -*-

# Othello AI Project
# University Of California, Irvine
# Authors: Akshat Patel, Teja Kolli, Prakul Agarwal

# Agent which plays a random valid move

# Imports
from othello import Othello
import random


class RandomAgent:

    @staticmethod
    def pick_move(othello, player):
        """ Picks a valid move at random. Returns -1 if no valid move possible.
        :type othello: Othello
        :param othello: An instance of the othello game skeleton
        :param player: The current player
        :return: A valid move if possible, -1 otherwise
        """
        valid_move_list = othello.valid_moves(player)
        if len(valid_move_list) > 0:
            return random.choice(valid_move_list)
        else:
            return -1

