import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import TextColor, color

def link_icon(tag: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=tag,
        ),
        href=url,
        is_external=True,
        color=TextColor.BODY.value,
        alt=str(tag),
    )