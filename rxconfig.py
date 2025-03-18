import reflex as rx

config = rx.Config(
    app_name="link_bio",
    favicon="/assets/favicon.ico",
    backend_url="https://my-biography-links.up.railway.app/",
    cors_allow_origins=[
        "http://localhost:3000/",
        "https://sbh-links-web.vercel.app/"
        ],
    show_built_with_reflex=False,
)