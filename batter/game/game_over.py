from game.actor import Actor
from game import constants
class GameOver(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.GAME_OVER_WIDTH
        self._height = constants.GAME_OVER_HEIGHT
        self._image = " "