import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.pages.index import index
from link_bio.pages.my_setup import my_setup
from link_bio.pages.animeflv_info import animeflv_info
from link_bio.api.api import live

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=(
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-FYMYC5EJCN"),
        rx.script('''window.dataLayer = window.dataLayer || [];
                     function gtag(){dataLayer.push(arguments);}
                     gtag('js', new Date());
                    gtag('config', 'G-FYMYC5EJCN');''')
    )
)

app.api.add_api_route('/api/live/{user_name}', live, methods=['GET'])