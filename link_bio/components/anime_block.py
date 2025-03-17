import reflex as rx
from link_bio.state.page_state import PasgeState
from link_bio.styles.colors import TextColor, Color


def anime_block():
    return rx.box(
        rx.hstack(
            rx.text(f'{PasgeState.name} anime list ',
                    rx.match(
                        PasgeState.anime_type,
                        ("favoritos", "Favorites"),
                        ("siguiendo", "Following"),
                        ("lista_espera", "Watchlist"),
                        "Unknown"  # valor por defecto
                    ),
                    color=TextColor.HEADER.value,
            ),
            rx.box(
                rx.text(f"Total: {PasgeState.count_animes}",
                        color=TextColor.HEADER.value
                ),
                text_align="right",
                flex="1",
            ),
            width="100%",
        ),
        rx.table.root(
            # rx.table.header(
            #     rx.table.row(
            #         rx.table.column_header_cell("Título"),
            #     ),
            #     position="sticky",
            #     top="0",
            #     background=Color.BACKGROUND.value,
            #     z_index="1",
            #     width="100%",
            # ),
            rx.table.body(
                rx.foreach(
                    PasgeState.animes,
                    lambda anime: rx.table.row(
                        rx.table.cell(anime["title"],
                                      white_space="nowrap",
                                      text_wrap="nowrap",
                                      color=TextColor.BODY.value,
                                      ),
                    )
                ),
            ),
            width="100%",
            height="calc(100% - 40px)",
        ),
        rx.hstack(
            rx.cond(
                PasgeState.has_animes,
                rx.hstack(
                    rx.button(
                        'Copy',
                        on_click=PasgeState.copy_data_table,
                        width="30%",
                        margin_top="10px",
                    ),
                    rx.button(
                        "Download CSV",
                        on_click=PasgeState.download_csv_data,
                        width="65%",
                        margin_top="10px",

                    ),
                ),
                rx.text("Load animes first to download",
                        color=TextColor.BODY.value,
                ),
            ),
            width="100%",
            justify="end",
        ),
        width="100%",
        height="400px",
        margin_top="20px",
    )
