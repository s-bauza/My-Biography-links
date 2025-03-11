import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import link_bio.utils as utils
from link_bio.routes import Route


        
@rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview_image,
    meta=utils.meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(True),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.DEFAULT.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
