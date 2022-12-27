import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Hello world',
    page_icon=Image.open('/Users/brianmoore/githib.com/datastx/PropTech/app/favicon.ico'),
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com/datastx/PropTech/issues/new',
        'About': 'About your application: **Hello world**'
        }
)

st.sidebar.title('Hello world')
st.title('Hello world')
