import reflex as rx
from link_bio.components.setup_part import setup_part
from link_bio.routes import Route
from link_bio.styles import styles
from link_bio.styles.styles import Size

def setup_links() -> rx.Component:
    return rx.vstack(
        rx.text('This is my workspace and the setup I use daily.', color=styles.TextColor.BODY.value),
        rx.image(
                src='/setup.jpeg',
                width='100%'
        ),
        setup_part(
            'sofa',
            'Furniture',
            ['DESK: STANDING DESK FLEXISPOT E7','CHAIR: GTPLAYER EMERGONOMISCHER GAMING STUHL'],
        ),
        setup_part(
            'computer',
            'PC (2016)',
            ['CHASSIS: NOX HUMMER MC WHITE','MAINBOARD: ASUS H170 PRO GAMING','CPU: INTEL CORE I5 6500','GPU: RADEON RX 590 SERIES', 'MEMORY: 32 GB', 'STORAGE: 500 GB SSD M2 + 1 TB HDD + 2 TB HDD','OS: WINDOWS 10 ENTERPRISE' ],
        ),
        setup_part(
            'monitor',
            'Screens',
            ['DISPLAY 1:LG IPS FULLHD','DISPLAY 2: ACER CB242Y','DUAL MONITOR MOUNT: MARS GAMING MMS2']
        ),
        setup_part(
            'keyboard',
            'Keyboard & Mouse',
            ['LOGITECH MK220','G502 HERO SE','AJAZZ AK820 PRO 75%','MOUSEPAD: REALKY GMS-X6' ],
        ),
        setup_part(
            'headphones',
            'Sound',
            ['SOUNDCORE ANKER Q30','ONEODIO PRO C'],
        ),
        setup_part(
            'mic',
            'Microphone',
            ['FURINE MICROPHONE PC'],
        ),
        setup_part(
            'webcam',
            'Camera',
            ['WEBCAMTRUST TRINO HD 720P'],
        ),
        setup_part(
            'lightbulb',
            'Lights',
            ['QUNTIS SCREENLINEAR'],
        ),
        setup_part(
            'network',
            'Network & Connections',
            ['ROUTER: ORANGE LIVEBOX 1 GB','TP-LINK TL-SG1005S','PRIMEWIRE CAT 8'],
        ),
        setup_part(
            'boxes',
            'Others',
            ['ECHO DOT 3','SAMSUNG S6 LITE','SAMSUNG S24 ULTRA'],
        ),
        width='100%',
        margin_top=Size.DEFAULT.value
    )
