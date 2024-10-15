import base64
import streamlit as sl
import requests
from streamlit_lottie import st_lottie as sl_loty
from streamlit.components.v1 import html

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load assets
lottie_wip = load_lottieurl('https://lottie.host/b8823d7e-cbee-41eb-a9fe-8aaab28b3275/hK41TFsgph.json')

# vertical spacing
def V_SPACE(lines):
    for _ in range(lines):
        sl.write('&nbsp;')

sl.markdown("<h1 style='text-align: left; color: #0078d7;'>About</h1>", unsafe_allow_html=True)

sl_loty(lottie_wip, height=333, key='wip')

V_SPACE(1)
sl.markdown("<p style='text-align: right; color: #0078d7;'>© All rights reserved.</p>", unsafe_allow_html=True)