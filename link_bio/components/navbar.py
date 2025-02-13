import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.styles import color as color
from link_bio.routes import Route
import link_bio.styles.styles as styles


def navbar() -> rx.Component: 
    return rx.hstack(
        rx.link(
            rx.text(
                "SBH",
                color=color.PRIMARY.value,
                style=styles.navar_title_style
            ),
            href=Route.INDEX.value,
        ),
        position='sticky',
        bg=color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index='999',
        top='0'
    )