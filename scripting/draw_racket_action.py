from curses.textpad import rectangle
from email.mime import image
from turtle import position
from constants import *
from game.scripting.action import Action

class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        racket = collection.get_first_entity(RACKET_GROUP)
        body = racket.get_body()

        if racket.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)

        image = racket.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)


    