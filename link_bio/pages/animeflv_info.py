import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.animeflv_box_info import animeflv_box_info_page
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import link_bio.utils as utils
from link_bio.routes import Route
        
@rx.page(
    route=Route.ANIMEFLV.value,
    title=utils.animeflv_info_title,
    description=utils.animeflv_info_description,
    image=utils.preview_image,
    meta=utils.meta,
)
def animeflv_info() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                animeflv_box_info_page(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.DEFAULT.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )