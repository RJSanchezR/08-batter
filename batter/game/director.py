from os import remove
from time import sleep
from game.audio_service import AudioService
from game.output_service import OutputService
import raylibpy
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            # TODO: Add some logic like the following to handle game over conditions
            if len(self._cast["bricks"]) == 0:
                # Game over
                audio_service = AudioService()
                audio_service.play_sound(constants.SOUND_OVER)
                # self._keep_playing = False
            
            if len(self._cast["lives"]) == 0:
                # Game over
                audio_service = AudioService()
                output_service = OutputService()
                audio_service.play_sound(constants.SOUND_OVER)
                # self._keep_playing = False
                
                output_service.remove_everything()

            if raylibpy.window_should_close():
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)