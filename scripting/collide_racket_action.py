from constants import *
from game.elements.sound import Sound
from game.scripting.action import Action

class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service =  physics_service
        self._audio_service = audio_service

    def execute(self, collection, script, callback):
        ball = collection.get_first_entity(BALL_GROUP)
        racket = collection.get_first_entity(RACKET_GROUP)

        ball_body = ball.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_colloded(ball_body, racket_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)