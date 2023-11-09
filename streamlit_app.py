#run locally in Terminal:  streamlit run streamlit-example\streamlit_app.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/

import streamlit as st

st.title("Datenerhebung")

showResult = False

listOfAnswers = ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu']
#answer1 = st.radio('Ich bin ein Detektiv, der die Geheimnisse des menschlichen Verhaltens lüftet, wenn ich eine Vorlesung über Human Factors besuche.', listOfAnswers)
#index1 = listOfAnswers.index(answer1)

#answer2 = st.radio('Meine Freunde würden mir ein ‚High Five‘ dafür geben, dass ich regelmäßig an Human Factors-Vorlesungen teilnehme.', listOfAnswers)
#index2 = listOfAnswers.index(answer2)

#answer3 = st.radio('Ich kann einen engen Zeitplan überwinden, um Zeit für den Besuch von Human Factors-Vorlesungen zu finden.', listOfAnswers)
#index3 = listOfAnswers.index(answer3)

answer4 = st.radio('Gäbe es Schokolade, würde ich sie mir nehmen.', listOfAnswers)
index4 = listOfAnswers.index(answer4)


if st.button('Speichern'):
    st.write('Vielen Dank!')


#st.title("Ergebnis: Wie gut passt die Theorie des geplanten Verhaltens auf Sie?")
#password = st.text_input('Bitte geben Sie das Passwort ein.')

#typ ausrechnen

#collectingchance = index4

#if (collectingchance > 2):
#    answer = 'Sie werden die Smarties einsammeln!'
#else:
#    answer = 'Sie werden die Smarties nicht einsammeln!'



#if password == "HKA":
#    st.write(f"Ergebnis: {answer}")