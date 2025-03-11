import reflex as rx

config = rx.Config(
    app_name="link_bio",
    favicon="/assets/favicon.ico",
    cors_allow_origins=[
        "http://localhost:3000/",
        "https://sbh-links-web.vercel.app/"
        ],
    show_built_with_reflex=False,
)