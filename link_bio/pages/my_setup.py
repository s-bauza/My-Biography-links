import reflex as rx
import link_bio.state.page_state as page_state
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.my_setup_links import setup_links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route
import link_bio.utils as utils

@rx.page(
    route=Route.MYSETUP.value,
    title=utils.my_setup_title,
    description=utils.my_setup_description,
    image=utils.preview_image,
    meta=utils.meta,
    on_load=page_state.PasgeState.twitch_live
)
def my_setup() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False,page_state.PasgeState.is_alive),
                setup_links(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.DEFAULT.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )