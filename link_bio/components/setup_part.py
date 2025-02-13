import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.title import title
from link_bio.styles.styles import Size
from link_bio.styles.styles import TextColor as TextColor


def setup_part(tag: str, text: str, components: list[str] ) -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(
                    tag=tag,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    color=TextColor.HEADER.value
                ),
                title(text),
                width='100%',
                justify_content='start',
                align_items='center',
            ), 
            *[rx.hstack(
                rx.icon(
                    tag='circle',
                    size=6,
                ),
                rx.text(component,color=TextColor.BODY.value),
                justify_content='start',
                align_items='center',
                width='100%',
                padding_x=Size.BIG.value,
            ) for component in components], 
        ),
        width='100%'
    )