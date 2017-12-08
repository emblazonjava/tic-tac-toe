class GamePlayService(object):
    """
    The service for helping the GamePlayController
    """

    def move(self, game, space):
        """
        Record the player's move on the board.
        Error checking is done by controller before calling this method

        :param game: The game to record the move in
        :param space: The space that the player wants to mark
        :return:
        """

        game.board[space] = game.player

        game.player = (game.player + 1) % 2

        game.turn += 1

    def validate_params_for_submit(self, params):
        return params and \
               'space' in params and \
               params['space'].isdigit() and \
               int(params['space']) >= 0 and \
               int(params['space']) < 9