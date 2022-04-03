from turtle import position
from constants import *
from game.scripting.action import Action

class DrawLinesYardAction(Action):
    def __init__(self,video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        lines_yard = collection.get_entities(YARD_LINES_GROUP)

        for line in lines_yard:
            body = line.get_body()

            if line.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle()

            image = lines_yard.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)




        