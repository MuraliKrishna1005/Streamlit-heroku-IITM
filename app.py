import streamlit as st

st.write("""
# To Find if the given Number is odd or even
""")

#Get Input
st.header('User Input Parameter')

def user_input_features():
    num = st.number_input("Number ",step=1)

    if num%2 == 0:
        return f'The given Number {num} is Even.'
    else:
        return f'The given Number {num} is Odd.'

result = user_input_features()

st.subheader('Result')
st.write(result)