#run locally in Terminal:  streamlit run streamlit-example\streamlit_app.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/
import streamlit as st

st.title("Fragebogen zur R-Angst1")

showResult = False

listOfAnswers = ['123Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu']
answer1 = st.radio('R stürzt immer ab, wenn ich es benutze.', listOfAnswers)
index1 = listOfAnswers.index(answer1)

answer2 = st.radio('Ich kann nicht schlafen, wenn ich an Eigenvektoren denke.', listOfAnswers)
index2 = listOfAnswers.index(answer2)

answer3 = st.radio('Standardabweichungen begeistern mich.', listOfAnswers)
index3 = listOfAnswers.index(answer3)

answer4 = st.radio('Ich habe wenig Erfahrung mit Computern.', listOfAnswers)
index4 = listOfAnswers.index(answer4)

answer5 = st.radio('Ich befürchte, dass ich irreparable Schäden verursachen werde wegen meiner Inkompetenz im Umgang mit Computern.', listOfAnswers)
index5 = listOfAnswers.index(answer5)

answer6 = st.radio('Ich wache unter meiner Bettdecke auf und denke, dass ich unter einer Normalverteilung gefangen bin.', listOfAnswers)
index6 = listOfAnswers.index(answer6)

answer7 = st.radio('Alle Computer hassen mich.', listOfAnswers)
index7 = listOfAnswers.index(answer7)


if st.button('Speichern'):
    st.write('Vielen Dank!')


st.title("Ergebnis: Welcher R-Angst-Typ sind Sie?")
password = st.text_input('Bitte geben Sie das Passwort ein.')

#typ ausrechnen

computerangst = (index4 + index1 + index5 + index7) / 4
statsangst = (index2 + (4-index3) + index6) / 3

if (computerangst >= 2) and (statsangst >= 2):
    answer = 'Sie haben sowohl Angst vor Computern, als auch vor Statistik! Therapievorschlag: Kommen Sie in meine Vorlesung und Übung!'
elif (computerangst >= 2) and (statsangst < 2):
    answer = 'Sie haben Angst vor Computern! Therapievorschlag: Kommen Sie in meine Übung!'
elif (computerangst < 2) and (statsangst >= 2):
    answer = 'Sie haben Angst vor Statistik! Therapievorschlag: Kommen Sie in meine Vorlesung!'
else:
    answer = 'Sie haben weder Angst vor Statistik, noch vor Computern! Wollen Sie eine Abschlussarbeit bei mir schreiben ;)?'



if password == "HFU":
    st.write(f"Ergebnis: {answer}")