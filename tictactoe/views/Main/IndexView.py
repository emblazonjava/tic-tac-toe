import retrobrowser.framework.view as view

class IndexView(view.View):
    # Overriding the abstract method
    def get_content(self):
        return "Welcome to TicTacToe! navigate to gamePlay/newGame to play a new game"