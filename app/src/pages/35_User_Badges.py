import streamlit as st
from modules.nav import get_nav_config
from streamlit_navigation_bar import st_navbar

pages, styles, logo, options = get_nav_config(show_home=False)
page = st_navbar(pages, selected="Badges", styles=styles, logo_path=logo, options=options)

if page == "Interests":
  st.switch_page('pages/32_User_Interests.py')

if page == "User Rank":
  st.switch_page('pages/36_Specific_User_Rank.py')

if page == "Logout":
  del st.session_state["role"]
  del st.session_state["authenticated"]
  st.switch_page("Home.py")