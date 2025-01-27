import reflex as rx
from enum import Enum
from .colors import Color as color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = '560px'


STYLESHEETS = [
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap',
    'https://fonts.googleapis.com/css2?family=Great+Vibes:wght@400&display=swap'
    
]

# Sizes


class Size(Enum):
    SMALL = '0.5em' # 8px = 1
    MEDIUM = '0.8em' # 12px = aprox 2
    DEFAULT = '1em' # 16px = 3
    LARGE = '1.5em' # 24px = 4
    BIG = '2em' # 32px = 6
    
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"
    
    
# Styles


BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'font_weight': FontWeight.LIGHT.value,
    'background_color': color.BACKGROUND.value,
    rx.heading: {
        'font_family':Font.TITLE.value,
        'font_weight': FontWeight.BOLD.value,
    },
    rx.icon: {
        '_hover': {
            'color': color.SECONDARY.value
        }
    },
    rx.button: {
        'width': '100%',
        'height': '100%',
        'padding': Size.SMALL,
        'border_radius': Size.DEFAULT,
        'color': TextColor.HEADER.value,
        'background_color': color.CONTENT.value,
        'white_space': 'nowrap',
        'justify_content': 'start',
        'align_items': 'center',
        '_hover': {
            'background_color': color.SECONDARY.value
        }
    },
    rx.link: {
       'text_decoration': 'none',
       '_hover': {}
    }
}

navar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.BOLD.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width='100%',
    pading=Size.DEFAULT,
    color=TextColor.HEADER.value,
    
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.BODY.value
)
