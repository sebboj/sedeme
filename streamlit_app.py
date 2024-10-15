import streamlit as sl

sl.set_page_config(page_title='I Am SEDE', page_icon=':male_mage:', layout='wide')

# page setup
home = sl.Page(
    page='views/home.py',
    title='Home',
    icon=':material/explosion:',
    default=True
)
about = sl.Page(
    page='views/about.py',
    title='About',
    icon=':material/account_circle:'
)
projects = sl.Page(
    page='views/projects.py',
    title='Projects',
    icon=':material/mountain_flag:'
)
contact = sl.Page(
    page='views/contact.py',
    title='Contact',
    icon=':material/emoji_people:'
)

# navigation menu
pg = sl.navigation([home,about, projects, contact])

sl.sidebar.text('Made with ❤.')


# run nav
pg.run()
