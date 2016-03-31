class Game(object):
    """
    The primary domain object for the tic-tac-toe game. Holds game state.
    """

    def __init__(self):
        self.board = ['_'] * 9 # Holds the moves, 0s and 1s
        self.turn = 0 # Values: 0 to 8, keeps track of which turn we are on
        self.player = 0 # Values: 0 or 1, keeps track of whose turn it is
