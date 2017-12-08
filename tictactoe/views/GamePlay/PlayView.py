import retrobrowser.framework.view as view

class PlayView(view.View):
    """
    View to render a tic-tac-toe board
    """

    # Overriding the abstract method
    def get_content(self):
        return """
               {0}|{1}|{2}
               {3}|{4}|{5}
               {6}|{7}|{8}
               """.format(self.board[0],
                          self.board[1],
                          self.board[2],
                          self.board[3],
                          self.board[4],
                          self.board[5],
                          self.board[6],
                          self.board[7],
                          self.board[8])
