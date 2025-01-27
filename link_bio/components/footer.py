import reflex as rx
import datetime
from link_bio.styles.styles import Size
from link_bio.styles.styles import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='campana.jpg',
            alt='Campana de fuego'
        ),
        rx.vstack(
            rx.text(
                f"© {str(datetime.datetime.now().year)} Santiago Bauzá Hirschler",
                font_size=Size.MEDIUM.value
            ),
            rx.text(
                'Nobody has greater satisfaction than overcoming themselves.',
                font_size=Size.MEDIUM.value
            ),
            spacing='0',
            align_items='center',
            justify='center'
        ),
        padding_y=Size.SMALL.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        align_items='center',
        color=TextColor.FOOTER.value
    )