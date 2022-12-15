import streamlit as st

st.write("i'm a professor bitches")

answer = st.selectbox('Pick one', ['cat', 'dog'])


password = st.text_input('Password')

if password == "bitches":
    st.write(f"you're type is: {answer}")