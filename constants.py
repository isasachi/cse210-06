from game.elements.color import Color
#----------------------------------------------
# GENERAL GAME CONSTANTS
#----------------------------------------------

#SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680

#FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#FONT
FONT_FILE = "ping_pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

#SOUND
BOUNCE_SOUND = 'ping_pong/assests/sounds/boing.wav'
OVER_SOUND = 'ping_pong/assests/sounds/over.wav'

#TEXT
ALIGN_LEFT = 1

#COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

#KEYS
ENTER = "enter"

#SCENES
TRY_AGAIN = 1
GAME_OVER = 4

#-------------------------------------------------
# CASTING CONSTANTS
#-------------------------------------------------

#STATS
STATS_GROUP = 'stats'
DEFAULT_LIVES = 3

#HUD 
LIVES_GROUP = 'lives'
SCORE_GROUP = 'score'
LIVES_FORMAT = 'LIVES: {}'
SCORE_FORMAT = 'SCORE: {}'

#BALL
BALL_GROUP = 'balls'
BALL_WIDTH = 28
BALL_VELOCITY = 6

#RACKET
RACKET_GROUP = "rackets"
RACKET_VELOCITY = 7

#YARD_LINES
YARD_LINES_GROUP = 'lines'
YARD_LINES = 'ping_pong/assets/images/white.gif'

#DIALOG
DIALOG_GROUP = 'dialogs'