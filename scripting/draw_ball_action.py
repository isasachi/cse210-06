from curses.textpad import rectangle
from turtle import position
from constants import *
from game.scripting.action import Action

class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        ball = collection.get_first_entity(BALL_GROUP)
        body = ball.get_body()
        #adds a puple box to see what is the space the image is filling
        if ball.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)

        image = ball.get_image()
        position = body.get_position()
        self._video_service.draw_action(image, position)