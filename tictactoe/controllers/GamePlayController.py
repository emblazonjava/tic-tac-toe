import tictactoe.domain.Game as g
import tictactoe.services.GamePlayService as gameplayservice

class GamePlayController(object):
    """
    The primary controller handling all the Game play actions
    """

    def __init__(self):
        self.game = g.Game()
        self.game_play_service = gameplayservice.GamePlayService()

    def index(self):
        return self.redirect(**{'action': 'new_game'})

    def play(self):
        """
        Prints the tic-tac-toe board
        :return: The board

        >>> import retrobrowser.framework.builder as b
        >>> builder = b.Builder()
        >>> builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'play')
        >>> game_play_controller = builder.get_controller()
        >>> print (game_play_controller.play())
        {'board': ['_', '_', '_', '_', '_', '_', '_', '_', '_']}
        """

        if not self.game:
            return self.new_game()

        if self.game.turn < 9:
            self.flash.message = 'Player {0} turn...'.format(self.game.player)
        else:
            self.flash.message = 'Board full'

        return {'board': self.game.board}

    def submit(self):
        """
        Handles the user input about what space to play
        :param space: The space to put the token on
        :return: redirects to play

        >>> import retrobrowser.framework.builder as b
        >>> builder = b.Builder()
        >>> builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'submit')
        >>> game_play_controller = builder.get_controller()
        >>> print (game_play_controller.new_game())
        new game created
        {'board': ['_', '_', '_', '_', '_', '_', '_', '_', '_']}
        >>> print (game_play_controller.game.player)
        0
        >>> print (game_play_controller.game.turn)
        0
        >>> game_play_controller.params = {'space': '4'}
        >>> print (game_play_controller.submit())
        {'board': ['_', '_', '_', '_', 0, '_', '_', '_', '_']}
        >>> print (game_play_controller.game.player)
        1
        >>> print (game_play_controller.game.turn)
        1
        """

        if not self.game:
            return self.new_game()

        space = None

        if self.game_play_service.validate_params_for_submit(self.params):
            space = int(self.params['space'])
        else:
            self.flash.error = 'Must enter an integer 0-8 as the space'
            return self.redirect(**{'action': 'play'})

        if self.game.turn >= 0 and self.game.turn < 9:
            int_space = int(self.params['space'])
            if self.game.board[int_space] == '_':
                self.game_play_service.move(self.game, int_space)
            else:
                self.flash.error = 'Cannot move there, that space is occupied'
        else:
            self.flash.error = 'Time for a new game'

        return self.redirect(**{'action': 'play'})

    def new_game(self):
        """
        Initalizes a Game
        :return: redirects to play

        >>> import retrobrowser.framework.builder as b
        >>> builder = b.Builder()
        >>> builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'newGame')
        >>> game_play_controller = builder.get_controller()
        >>> print (game_play_controller.new_game())
        new game created
        {'board': ['_', '_', '_', '_', '_', '_', '_', '_', '_']}
        >>> print (game_play_controller.game.player)
        0
        >>> print (game_play_controller.game.turn)
        0
        >>> game_play_controller.params = {'space': '4'}
        >>> print (game_play_controller.submit())
        {'board': ['_', '_', '_', '_', 0, '_', '_', '_', '_']}
        >>> print (game_play_controller.game.player)
        1
        >>> print (game_play_controller.game.turn)
        1
        >>> print (game_play_controller.new_game())
        new game created
        {'board': ['_', '_', '_', '_', '_', '_', '_', '_', '_']}
        >>> print (game_play_controller.game.player)
        0
        >>> print (game_play_controller.game.turn)
        0
        """

        self.game = g.Game()
        print ('new game created')
        return self.redirect(**{'action': 'play'})