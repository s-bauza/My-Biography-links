import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
import link_bio.constants as constants

def links() -> rx.Component:
    return rx.vstack(
        title('DEV'),
        link_button(
            'github',
            'GitHub',
            's-bauza',
            constants.GITHUB_URL
        ),
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
        link_button(
            'twitch',
            'Twitch',
            'cordico',
            constants.TWITCH_URL
        ),
        title('Games'),
        link_button(
            'gamepad-2',
            'Genshin impact',
            'Europe Server UID: 712814271',
            constants.GENSHIN_IMPACT_URL
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
