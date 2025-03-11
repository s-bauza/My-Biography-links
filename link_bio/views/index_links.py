import reflex as rx
import link_bio.constants as constants
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
from link_bio.state.page_state import PasgeState


def index_links() -> rx.Component:
    return rx.vstack(
        title('DEV'),
        link_button(
            'github', 
            'GitHub',
            's-bauza',
            constants.GITHUB_URL
        ),
        #TODO: Future feature projects
        # link_button(
        #     'anvil',
        #     'Projects',
        #     'My projects 🛠',
        #     Route.PROYECTS.value,
        #     is_external=False
        # ),
        title('Social Media'),
        link_button(
            'linkedin',
            'Linkedin',
            'Santiago Bauzá Hirschler',
            constants.LINKEDIN_URL
        ),
        link_button(
            'x',
            'X',
            'Cordic0',
            constants.X_URL
        ),
        link_button(
            'instagram',
            'Instagram',
            'santibauza',
            constants.INSTAGRAM_URL
        ),
        link_button(
            'instagram',
            'Instagram',
            'cordicoomg',
            constants.INSTAGRAM2_URL
        ),
        link_button(
            'youtube',
            'Youtube',
            '@cordico9070',
            constants.YOUTUBE_URL
        ),
        rx.box(
            link_button(
                'twitch',
                'Twitch',
                'cordico',
                constants.TWITCH_URL
            ),
            rx.box(  
                width=Size.SMALL.value,  
                height=Size.SMALL.value,
                background_color=rx.cond(PasgeState.live_status.live, "green", "red"), 
                border_radius="50%",  
                position="absolute",  
                top="57%",  
                left="41px",
                class_name=rx.cond(PasgeState.live_status.live, "blink", ""),   
                on_mount=PasgeState.twitch_live
            ),
            position="relative",
            width='100%',
        ),
        title('Games'),
        link_button(
            'gamepad-2',
            'Genshin impact',
            'Europe Server UID: 712814271',
            constants.GENSHIN_IMPACT_URL
        ),
        title('Resources'),
        link_button(
            'computer',
            'Setup',
            'My setup',
            Route.MYSETUP.value,
            False
        ),
        title('Contact'),
        link_button(
            'mail',
            'Email',
            constants.EMAIL,
            f'mailto:{constants.EMAIL}'
        ),
        width='100%',
        spacing='3',
        margin_top=Size.DEFAULT.value
    )
