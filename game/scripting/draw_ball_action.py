# from curses.textpad import rectangle
# from turtle import position
from constants import *
from game.scripting.action import Action

class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()

        image = ball.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)