#run locally:  streamlit run .\streamlit_app.py
#run on website: commit and push: https://estherjohanna-streamlit-example-streamlit-app-egl5jh.streamlit.app/
import streamlit as st

st.write("R stürzt immer ab, wenn ich es benutze")

answer = st.select_slider('R stürzt immer ab, wenn ich es benutze', ['Ich stimme gar nicht zu', 'Ich stimme nicht zu', 'Weder - noch', 'Ich stimme zu','Ich stimme voll und ganz zu'])


password = st.text_input('Password')

if password == "bitches":
    st.write(f"you're type is: {answer}")