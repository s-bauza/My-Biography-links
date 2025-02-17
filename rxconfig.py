import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allow_origins=[
        "http://localhost:3000/",
        "https://sbh-links-web.vercel.app/"
        ],
)