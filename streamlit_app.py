import streamlit as st

st.write("i'm a professor bitches")

answer = st.selectbox('Pick one', ['cats', 'dogs'])


password = st.text_input('Password')

if password == "bitches":
    st.write(f"you're type is: {answer}")