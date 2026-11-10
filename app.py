import streamlit as st

st.title("Calculator")
a= st.number_input("Enter first number")
b= st.number_input("Enter second number")

if st.button("Add"):
    print(a+b)
    st.write("Answer =", a+b)

if st.button("Subtract"):
    st.write("Answer =", a-b)

if st.button("Multiply"):
    st.write("Answer =", a*b)

if st.button("Divide"):
    if b != 0:
        st.write("Answer =", a/b)

else:
    st.write("Cannot divide by zero")      
