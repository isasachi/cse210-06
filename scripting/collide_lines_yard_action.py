from constants import *
from game.elements.sound import Sound
from game.scripting.action import Action

class CollideLinesYardAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, collection, script, callback):
        ball = collection.get_first_entity(BALL_GROUP)
        yard_lines = collection.get_entities(YARD_LINES_GROUP)
        ball_body = ball.get_body()
        yard_lines_body = yard_lines.get_body()

        if self._physics_service.has_coolided(ball_body, yard_lines_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
