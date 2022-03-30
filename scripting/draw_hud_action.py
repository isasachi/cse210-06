from turtle import position
from constants import *
from game.scripting.action import Action

class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, collection, script, callback):
        stats = collection.get_first_entity(STATS_GROUP)
        self._draw_label(collection, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_label(collection, SCORE_GROUP, SCORE_FORMAT, stats.get_score())

    def _draw_label(self, collection, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = collection.get_first_entity(group)
        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)