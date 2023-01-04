import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
# verificar si el usuario está autenticado


if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')