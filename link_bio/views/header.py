import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size, Spacing
import link_bio.constants as constants
from link_bio.styles.styles import TextColor, color


def header(details=True,twitch_live=False) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback='SBH',
                src='/llamas.png',
                size='7',
            ),
            
            rx.vstack(
                rx.heading(
                    'Santiago Bauzá Hirschler',
                    color=TextColor.HEADER.value,
                    size='6',

                ),
                rx.hstack(
                    link_icon(
                        'linkedin',
                        constants.LINKEDIN_URL
                    ),
                    link_icon(
                        'github',
                        constants.GITHUB_URL,
                    ),
                    link_icon(
                        'youtube',
                        constants.YOUTUBE_URL
                    ),
                    link_icon(
                        'x',
                        constants.X_URL
                    ),
                    rx.box(  
                        link_icon(
                            'twitch',
                            constants.TWITCH_URL
                        ),
                        rx.box(  
                            width=Size.SMALL.value,  
                            height=Size.SMALL.value,
                            background_color=rx.cond(twitch_live, "green", "red"), 
                            border_radius="50%",  
                            position="absolute",  
                            top="65%",  
                            left="20px",   
                            class_name=rx.cond(twitch_live, "blink", ""),
                        ),
                        position="relative",  
                    ),
                    padding_top=Size.DEFAULT.value,
                    spacing=Spacing.SMALL.value,
                ),
            ),
        ),
        rx.cond(
            details,
                rx.text(
                    "Hi! I'm Santiago, a technology and video game enthusiast. I'm currently working on completing my degree in Technologies for the Information Society while learning new technologies and improving my English to enhance my skills in the industry. My hobbies include playing video games like Genshin Impact, watching anime, doing judo, exploring the mountains with friends and family, and some times sharing content as a creator on Twitch and YouTube. Here, you can find my projects, social media, and more about what I do. Thanks for stopping by!",
                    color=TextColor.BODY.value,
                    padding_top=Size.DEFAULT.value,
                ),
        ),
    )
