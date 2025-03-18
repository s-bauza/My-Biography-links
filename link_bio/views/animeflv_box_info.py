import reflex as rx
from link_bio.state.page_state import PasgeState
from link_bio.styles.styles import Spacing
from link_bio.styles.colors import Color, TextColor
from link_bio.components.anime_block import anime_block


def animeflv_box_info_page():

    return rx.vstack(
        rx.heading('Animelfv Info', color=TextColor.HEADER.value),
        rx.form(
            rx.hstack(
                rx.input(
                    placeholder="User name",
                    on_change=PasgeState.set_name,
                    size=Spacing.MEDIUM_SMALL.value,
                    required=True,
                    min_length=1,
                    width='100%',
                    color=TextColor.BODY.value,
                ),
                rx.select.root(
                    rx.select.trigger(
                        name='anime_type',
                        variant='soft',
                        background_color=Color.CONTENT.value,
                        color=TextColor.HEADER.value,),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item("Favorites", value="favoritos"),
                            rx.select.item("Following", value="siguiendo"),
                            rx.select.item("Watchlist", value="lista_espera"),
                        ),
                        color=TextColor.BODY.value,
                        color_scheme='yellow',
                        variant='soft',

                    ),
                    default_value='favoritos',
                    name='anime_type',
                    required=True,
                    size=Spacing.MEDIUM_SMALL.value,
                    on_change=PasgeState.set_anime_type,
                ),
                rx.box(
                    rx.button(
                        'Search',
                        on_click=PasgeState.get_animes,
                        disabled=PasgeState.name == "",
                    ),
                ),
                rx.cond(
                    PasgeState.loading,
                    rx.spinner(),
                    rx.text(''),

                ),
            ),
            on_submit=PasgeState.get_animes,
            enter_key_submit=True,
        ),
        rx.vstack(
            anime_block(),
            width='100%',
        ),
        width='100%',
        margin_top='20px',
    )
