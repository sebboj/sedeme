import streamlit as sl
import requests
from streamlit_lottie import st_lottie as sl_loty
from PIL import Image
from streamlit.components.v1 import html

sl.set_page_config(page_title='I Am SEDE', page_icon=':male_mage:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')

#vertical spacing
def V_SPACE(lines):
    for _ in range(lines):
        sl.write('&nbsp;')

#load assets
lottie_blob = load_lottieurl('https://lottie.host/33118df1-fd23-404e-84f7-60afb603811e/h9LzOU2qa6.json')
w_open = 'https://i.imgur.com/Gj4Q7aq.png'
w_shut = 'https://i.imgur.com/saTyGe0.png'
w_peek = 'https://i.imgur.com/jitxniN.png'

#landing screen
with sl.container():
    V_SPACE(7)
    sl.markdown("<h1 style='text-align: center; color: #0078d7;'>LET THERE BE DATA</h1>", unsafe_allow_html=True)
    V_SPACE(7)
    sl.write('Please  \nScroll All The Way:arrow_double_down:')

#who am I
with sl.container():
    left_col, right_col = sl.columns(2)
    with left_col:
        V_SPACE(3)
        sl.subheader('Are you looking for an engineer that is:')
        sl.subheader('&nbsp;&nbsp;&nbsp;>Adept')
        sl.subheader('&nbsp;&nbsp;&nbsp;>Honest')
        sl.subheader('&nbsp;&nbsp;&nbsp;>Aplomb')
        sl.subheader('&nbsp;&nbsp;&nbsp;>Proactive')
        sl.subheader('&nbsp;&nbsp;&nbsp;>Coachable')
        sl.subheader('Seek no further...')
        V_SPACE(1)
        sl.header('Greetings, I am :blue[Sebastian Dolan El]')
        sl.subheader('Allow me to add value to your business using statistics and programming')
    with right_col:
        V_SPACE(1)
        sl_loty(lottie_blob, height=666, key='blob')

#my projects
with sl.container():
    V_SPACE(2)
    sl.header('My Projects')
    image_col, text_col = sl.columns((1,4))
    with image_col:
        html(
            f"""
            <div id="image-container" class="image-container">
                <img alt="" src="{w_shut}" style="height: 250px; width: 300px" id="door" onmouseover="handleMouseOver()" onmouseout="handleMouseOut()"onclick="handleClick()"/>
            </div>
            <script>
            function handleMouseOver() {{
                console.log('over');
                document.getElementById('door').src = '{w_peek}';
            }}
            function handleMouseOut() {{
                console.log('out');
                document.getElementById('door').src = '{w_shut}';
            }}
            function handleClick() {{
                console.log('click');
                document.getElementById('door').src = '{w_open}';
                window.location.href = 'https://www.themangoplace.com/'; //replace w desired page
            }}
            </script>
            
            <style>
            .image-container{{
                //border: 4px solid white;
                width: 300px;
                min-height: 250px;
                overflow: hidden;
                background-size: 100% 100%;
                cursor: grab;
            }}
            .image-container:active{{
                cursor: grabbing;
            }}
            </style>
            """, height=300)
    with text_col:
        sl.subheader('Project 1')
        sl.write(
            '''
            - g
            - u
            - h
            - h
            - h
            - h
            - h
            '''
        )
        V_SPACE(1)
    with image_col:
        html(
            f"""
            <div id="image-container" class="image-container">
                <img alt="" src="{w_shut}" style="height: 250px; width: 300px" id="door" onmouseover="handleMouseOver()" onmouseout="handleMouseOut()"onclick="handleClick()"/>
            </div>
            <script>
            function handleMouseOver() {{
                console.log('over');
                document.getElementById('door').src = '{w_peek}';
            }}
            function handleMouseOut() {{
                console.log('out');
                document.getElementById('door').src = '{w_shut}';
            }}
            function handleClick() {{
                console.log('click');
                document.getElementById('door').src = '{w_open}';
                window.location.href = 'https://www.themangoplace.com/'; //replace w desired page
            }}
            </script>

            <style>
            .image-container{{
                //border: 4px solid white;
                width: 300px;
                min-height: 250px;
                overflow: hidden;
                background-size: 100% 100%;
                cursor: grab;
            }}
            .image-container:active{{
                cursor: grabbing;
            }}
            </style>
            """, height=300)
    with text_col:
        sl.subheader('Project 2')
        sl.write(
            '''
            - g
            - u
            - h
            - h
            - h
            - h
            - h
            '''
        )
        V_SPACE(1)
#contact me
with sl.container():
    sl.write('---')
    sl.header('Kindly connect with me')
    # sl.header('I am open to further discussion')
    contact_form = '''
    <form action="https://formsubmit.co/eff8967734373b429d782e941b162b2c" method="POST">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message" required></textarea>
         <button type="submit">Send</button>
    </form>
    '''
    left_col, right_col = sl.columns(2)
    with left_col:
        sl.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        sl.empty()
