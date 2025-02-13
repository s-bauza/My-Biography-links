import reflex as rx

def lang()->rx.Component:
    return rx.script("document.dispatchEvent.lang='en'"),

# Index page

index_title = 'LINKS_BIO_SBH'
index_description = 'LINKS_BIO_SBH_DESCRIPTION'
preview_image = '/favicon-16x16.png'
meta=[
         {'name': 'og:preview_image'}
    ]

# Proyects page

# proyects_title = 'Proyects'
# proyects_description = 'Proyects_DESCRIPTION'
# proyects_image = '/favicon-16x16.png'

#My setup page

my_setup_title = 'My SetUp'
my_setup_description = 'My SetUp DESCRIPTION'
my_setup_image = '/favicon-16x16.png'
