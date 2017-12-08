import unittest
import retrobrowser.framework.builder as b

class IntegrationTests(unittest.TestCase):

    def test_get_controller(self):
        builder = b.Builder()
        builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'play')
        controller = builder.get_controller()

        self.assertEqual('tictactoe.controllers.GamePlayController', controller.__module__)
        self.assertEqual('GamePlayController', controller.__class__.__name__)

    def test_get_view(self):
        builder = b.Builder()
        builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'play')
        view = builder.get_view({'hello': 'world'})

        self.assertEqual('tictactoe.views.GamePlay.PlayView', view.__module__)
        self.assertEqual('PlayView', view.__class__.__name__)
        self.assertEqual('world', view.hello)

    def test_get_action(self):
        builder = b.Builder()
        builder.set_package_controller_and_action('tictactoe', 'gamePlay', 'play')
        action = builder.get_action()
        self.assertEqual('play', action.__name__)


if __name__ == '__main__':
    unittest.main()