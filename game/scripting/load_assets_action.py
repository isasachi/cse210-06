from game.scripting.action import Action

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, collection, script, callback):
        # self._audio_service.load_sounds(ASSETS_SOUND)
        # self._video_service.load_fonts(ASSETS_FONT)
        # self._video_service.load_images(ASSETS_IMAGES)
        self._audio_service.load_sounds(r'D:\Apps\byui-winter-2022\cse210-projects\cse210-06\assets\sounds')
        self._video_service.load_fonts(r'D:\Apps\byui-winter-2022\cse210-projects\cse210-06\assets\fonts')
        self._video_service.load_images(r'D:\Apps\byui-winter-2022\cse210-projects\cse210-06\assets\images')