import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size


def link_button(tag: str, text: str, sub_text: str, url: str) -> rx.Component:

    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=tag,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(sub_text, style=styles.button_body_style),
                    align_items='start',
                    spacing='1',
                ),
                width='100%',
            ), 
            width='100%',
        ),
        href=url,
        is_external=True,
        width='100%'
    )
