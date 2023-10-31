#run locally in Terminal:  streamlit run streamlit-example\streamlit_app.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/
import streamlit as st

st.title("Fragebogen zur R-Angst")

showResult = False

listOfAnswers = ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu']
answer1 = st.radio('R stürzt immer ab, wenn ich es benutze.', listOfAnswers)
index1 = listOfAnswers.index(answer1)

answer2 = st.radio('Ich kann nicht schlafen, wenn ich an Eigenvektoren denke.', listOfAnswers)
index2 = listOfAnswers.index(answer2)

answer3 = st.radio('Standardabweichungen begeistern mich.', listOfAnswers)
index3 = listOfAnswers.index(answer3)
