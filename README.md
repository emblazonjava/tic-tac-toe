This package depends on the [retro-browser](https://github.com/allisonf/retro-browser) package.

It is a sample app for the RetroBrowser framework.

# Installation

This is a Python 3 application and requires version 3.2 or greater.

This package can be installed with pip, which comes along with Python 3.4 and above. If downloading from this 
repository, you will need to build the distribution and then install it locally:

`python3 setup.py sdist --formats=zip`

This will create a `dist` folder in the base directory and in it you will find a file called `TicTacToe-1.0.zip`.

Copy `TicTacToe-1.0.zip` to a temporary location where you can unzip it. The unzipped folder still needs
to be installed. To install, make sure you are in the directory containing `TicTacToe-1.0.zip` and execute:

`pip3 install -e TicTacToe-1.0`

# Game Play

* Start the framework, passing the application package name in as the first argument:

`retroBrowser tictactoe`

* The current "page" that you are out will be printed out

eg "at tictactoe/main/index"

* Start a new game by navigating:

`to gamePlay/newGame`

* Move in a space, 0 - 8 using a query string:

`to gamePlay/submit?space=2`

* There is no indication when a game has been won but when the board is filled up, you will be notified
that it is time for a new game

# Testing

doctest and unittest are used.

To run doctests, execute:

`python3 tests/doctests.py`

To run integration tests, execute:

`python3 tests/integrationtests.py`