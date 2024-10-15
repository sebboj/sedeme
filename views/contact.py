import streamlit as sl

# vertical spacing
def V_SPACE(lines):
    for _ in range(lines):
        sl.write('&nbsp;')

# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')

sl.markdown("<h1 style='text-align: left; color: #0078d7;'>Contact</h1>", unsafe_allow_html=True)

# contact form
with sl.container():
    sl.subheader('Kindly connect with me')
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

# links
sl.write('---')
sl.subheader('Other ways to reach me')
sl.markdown(f"<a style='display: inline; text-align: left;' href={'https://www.youtube.com/@se2boj'}>youtube.com/@se2boj</a>"
            f"<span> to watch me speak.</span>",unsafe_allow_html=True)
sl.markdown(f"<a style='display: inline; text-align: left;' href={'https://github.com/sebboj'}>github.com/sebboj</a>"
            f"<span> to catch a glimpse of my work.</span>",unsafe_allow_html=True)
sl.markdown(f"<a style='display: inline; text-align: left;' href={'https://www.linkedin.com/in/sebastian-dolan-el/'}"
            f">linkedin.com/in/sebastian-dolan-el</a><span> everybody has one these days.</span>",unsafe_allow_html=True)

V_SPACE(1)
sl.markdown("<p style='text-align: right; color: #0078d7;'>© All rights reserved.</p>", unsafe_allow_html=True)