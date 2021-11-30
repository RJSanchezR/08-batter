import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.lives import Lives
from game.game_over import GameOver
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    
    cast["bricks"] = []
    for x in range(55, 700, 55):
        for y in range(60, 180, 30):
            brick = Brick()
            brick.set_image(constants.IMAGE_BRICK)
            brick.set_position(Point(x, y))
            brick.set_velocity(Point(2, 0))
            brick.set_width(constants.BRICK_WIDTH)
            brick.set_height(constants.BRICK_HEIGHT)
            cast["bricks"].append(brick)

    cast["balls"] = []
    ball = Ball()
    ball.set_position(Point(constants.MAX_X / 2, constants.MAX_Y / 2))
    ball.set_velocity(Point(3, -3))
    cast["balls"].append(ball)

    cast["paddle"] = []
    paddle = Paddle()
    paddle.set_position(Point(constants.MAX_X / 2, constants.MAX_Y - 40))
    cast["paddle"].append(paddle)

    cast["lives"] = []
    space = 90

    for x in range(1):
        for y in range(3):
            life = Lives()
            life.set_image(constants.IMAGE_BALL)
            life.set_position(Point(1, (constants.MAX_Y - space)))
            life.set_width(constants.BALL_WIDTH)
            life.set_height(constants.BALL_HEIGHT)
            cast["lives"].append(life)
            space = space - 30
    
    cast["game_over"] = []
    game_over = GameOver()
    game_over.set_position(Point(282, 182))
    cast["game_over"].append(game_over)

    # Create the script {key: tag, value: list}aaz
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game(cast)

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
