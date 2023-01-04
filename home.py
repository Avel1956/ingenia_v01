import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader
from streamlit_authenticator import Authenticate
from functions import *
import logging
import datetime

page_config = st.set_page_config(page_title="IngenIA", 
    page_icon=":robot:", layout="wide", initial_sidebar_state="collapsed")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
st.session_state['authentication_status'] = authentication_status
if st.session_state["authentication_status"]:
    st.title('IngenIA')
       
        

        
    authenticator.logout('Logout', 'main')
    
    st.write(f'Hola *{st.session_state["name"]}*')
    #divide screen in tree columns, one narrowest and two wider
    col1, col2, col3 = st.columns([2, 1, 2])
        
    #col1
    col1.header('Entrada')
    
    #save text in a variable
    text_ini = col1.text_area('Texto inicial', height=400)
    # Save the text in the session state
    st.session_state["text_ini"] = text_ini

    #calculate nuymber of tokens
    tokens = len(text_ini.split())
    col1.write(f'Número de tokens: {tokens}')
    # change middle column color
    col2.markdown(f'<style>div.row-widget.stRadio > div{{background-color: #F5F5F5;}}</style>', unsafe_allow_html=True)
    
    #col2
    col2.header('Operaciones')
    
    #save radio selection in a variable
    radio_sel = col2.radio('Método', ('Extracción de relaciones', 'Resumir', 'Extracción de entidades',
    'Análisis de sentimiento', 'Extracción de conceptos', 'Extracción de preguntas', 'Extracción de respuestas'),
    help='Seleccione el método que desea ejecutar')
    if radio_sel == 'Extracción de relaciones':
        metodo = extraccion_relaciones
    elif radio_sel == 'Resumir':
        metodo = resumen
    elif radio_sel == 'Extracción de entidades':
        metodo = extraccion_entidades
    elif radio_sel == 'Análisis de sentimiento':
        metodo = extraccion_sentimientos
    elif radio_sel == 'Extracción de conceptos':
        metodo = extraccion_conceptos
    elif radio_sel == 'Extracción de preguntas':
        metodo = extraccion_preguntas
    elif radio_sel == 'Extracción de respuestas':
        metodo = extraccion_respuestas
    # Save the method in the session state
    st.session_state["metodo"] = metodo
    # a button to call the function
    respuesta=''
    if col2.button('Ejecutar', help='Ejecuta el método seleccionado'):
        respuesta= get_answer(text_ini, metodo)
        # Save the response in the session state
        st.session_state["respuesta"] = respuesta
        # Set the log file and log level
        logging.basicConfig(filename='log.txt', level=logging.INFO)

        # Get the current session timestamp
        session_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Get the user name from the session state
        user = st.session_state["name"]

        # Get the input text from the session state
        text_ini = st.session_state["text_ini"]

        # Get the method from the session state
        metodo = st.session_state["metodo"]

        # Get the response from the session state
        respuesta = st.session_state["respuesta"]

        # Format the log message
        log_message = f'{session_timestamp}, {user}, {text_ini}, {metodo}, {respuesta}'

        # Log the message
        logging.info(log_message)

    #col2.image('resources\Arrows_blue.png', width=100)
    #col3
    col3.header('Salida')
    
    #write variable to text area
    col3.text_area('Texto final', respuesta, height=400)
    #put a copy button
    col3.button('Copiar', help='Copia el texto final al portapapeles')
    
    st.write('---')
    st.write('---')
    col1, col2, col3 = st.columns([2, 1, 2])
    
    col1.write('VERSION 0.01')
    col1.write('Jaime Vélez, 2023')
    if col3.button('Download log', help='descaargar el log'):
        st.download_button(label='Download log', data='log.txt', file_name='log.txt', mime='text/plain')


elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

# create a log with timestamp and username
import datetime
now = datetime.datetime.now()
with open('log.txt', 'a') as f:
    f.write(f'{now} {st.session_state["name"]} {st.session_state["authentication_status"]}')






