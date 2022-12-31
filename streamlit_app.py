#run locally:  streamlit run .\streamlit_app.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/
import streamlit as st

st.write("R-Angst Fragebogen")

answer1 = st.select_slider('R stürzt immer ab, wenn ich es benutze', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer2 = st.select_slider('Ich kann nicht schlafen, wenn ich an Eigenvektoren denke', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer3 = st.select_slider('Standardabweichungen begeistern mich', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer4 = st.select_slider('Ich habe wenig Erfahrung mit Computern', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer5 = st.select_slider('Ich befürchte, dass ich irreparable Schäden verursachen werde wegen meiner Inkompetenz im Umgang mit Computern', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer6 = st.select_slider('Ich wache unter meiner Bettdecke auf und denke, dass ich unter einer Normalverteilung gefangen bin', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])

answer7 = st.select_slider('Alle Computer hassen mich', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])


password = st.text_input('efa')

if password == "efa":
    st.write(f"your type is: {answer}")