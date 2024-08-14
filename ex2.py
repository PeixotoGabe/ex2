#ex 2

import streamlit as st
import speech_recognition as sr

st.title("Transcrição de Áudio")

audio_file = st.file_uploader("Envie um arquivo de áudio", type=["wav"])

if audio_file is not None:
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        st.write("Transcrição:")
        st.write(text)
    except:
        st.write("Não foi possível transcrever o áudio.")


