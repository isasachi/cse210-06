from turtle import position
from constants import *
from game.elements.point import Point
from game.scripting.action import Action

class MoveRacketAction(Action):

    def __ini__(self):
        pass

    def execute(self, collection, script, callback):
        racket = collection.get_first_entity(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()

        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            positioN = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())

        body.set_position(position)