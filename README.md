This package depends on the [retro-browser](https://github.com/allisonf/retro-browser) package'

It is a sample app for the RetroBrowser framework.

#Installation

This package can be distributed with distutils

`python3 setup.py sdist`

Unzip the resultant file (found in the newly created dist folder) and, from within, execute:

`python3 setup.py install`

#Game Play

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

#Testing

doctest and unittest are used.

To run doctests, execute:

`python3 tests/doctests.py`

To run integration tests, execute:

`python3 tests/integrationtests.py`