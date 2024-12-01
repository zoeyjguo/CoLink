import streamlit as st
from modules.nav import get_nav_config
from streamlit_navigation_bar import st_navbar

pages, styles, logo, options = get_nav_config(show_home=False)
page = st_navbar(pages, selected="Reports", styles=styles, logo_path=logo, options=options)

if page == "Delete Group Chat":
  st.switch_page('pages/23_Delete_GroupChat.py')

if page == "Flag Message":
  st.switch_page('pages/25_Flag_Message.py')

if page == "Logout":
  del st.session_state["role"]
  del st.session_state["authenticated"]
  st.switch_page("Home.py")