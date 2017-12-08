import doctest
import importlib

doctest.testmod(importlib.import_module('tictactoe.controllers.GamePlayController'))
doctest.testmod(importlib.import_module('tictactoe.services.GamePlayService'))