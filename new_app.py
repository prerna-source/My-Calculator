
import streamlit as st

st.title("My Calculator")


if "display" not in st.session_state:
    st.session_state.display = "0"

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None


# Show the display
st.text_input("Display", value=st.session_state.display, disabled=True)


# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    cols = st.columns(4)

    for i, button in enumerate(row):
        if cols[i].button(button, use_container_width=True):

            if button.isdigit():
                if st.session_state.display == "0":
                    st.session_state.display = button
                else:
                    st.session_state.display += button

            elif button == "C":
                st.session_state.display = "0"
                st.session_state.first_number = None
                st.session_state.operator = None

            elif button in ["+", "-", "*", "/"]:
                st.session_state.first_number = float(st.session_state.display)
                st.session_state.operator = button
                st.session_state.display = "0"

            elif button == "=":
                if st.session_state.first_number is not None:
                    second_number = float(st.session_state.display)
                    op = st.session_state.operator

                    if op == "+":
                        result = st.session_state.first_number + second_number
                    elif op == "-":
                        result = st.session_state.first_number - second_number
                    elif op == "*":
                        result = st.session_state.first_number * second_number
                    elif op == "/":
                        if second_number == 0:
                            st.error("Cannot divide by zero")
                            result = None
                        else:
                            result = st.session_state.first_number / second_number
                    else:
                        result = None

                    if result is not None:
                        st.session_state.display = str(result)

                    st.session_state.first_number = None
                    st.session_state.operator = None

            st.rerun()

