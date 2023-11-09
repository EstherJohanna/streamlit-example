#run locally in Terminal:  streamlit run streamlit-example\MentalArithmetic.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/
import streamlit as st
import sqlite3

# Database setup
conn = sqlite3.connect('survey_results.db')
c = conn.cursor()

# Create table - this should be done once
c.execute('''
          CREATE TABLE IF NOT EXISTS responses 
          (id INTEGER PRIMARY KEY AUTOINCREMENT, answer1 INTEGER, answer2 INTEGER, 
           answer3 INTEGER, answer4 INTEGER)
          ''')
conn.commit()

# Streamlit app
st.title("Fragebogen zur Vorlesungsteilnahme")

showResult = False

listOfAnswers = ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu']
answer1 = st.radio('Ich mag Schokolade.', listOfAnswers)
index1 = listOfAnswers.index(answer1)

answer2 = st.radio('Meine Freunde finden bunte Kreise toll.', listOfAnswers)
index2 = listOfAnswers.index(answer2)

answer3 = st.radio('Es gibt Schokolade in meiner Nähe.', listOfAnswers)
index3 = listOfAnswers.index(answer3)

answer4 = st.radio('Gäbe es für die Teilnahme an Human Factors-Vorlesungen „Smarty-Punkte" würde ich möglichst alle davon einsammeln.', listOfAnswers)
index4 = listOfAnswers.index(answer4)


if st.button('Speichern'):
    # Insert a row of data
    c.execute("INSERT INTO responses (answer1, answer2, answer3, answer4) VALUES (?, ?, ?, ?)",
              (index1, index2, index3, index4))
    conn.commit()

    st.write('Vielen Dank!')

# Don't forget to close the connection
conn.close()

