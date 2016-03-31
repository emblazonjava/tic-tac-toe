#!/usr/bin/env python

from distutils.core import setup

setup(name='TicTacToe',
      version='0.1',
      description='A tic-tac-toe game playable by RetroBrowser',
      author='Allison F',
      author_email='yetanotherallisonf@yahoo.com',
      url='https://github.com/allisonf/tic-tac-toe',
      packages=['tictactoe',
                'tictactoe.controllers',
                'tictactoe.domain',
                'tictactoe.services',
                'tictactoe.views.GamePlay',
                'tictactoe.views.Main']
     )