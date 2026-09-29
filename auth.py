import streamlit as st

st.markdown("""
<style>
input { color: white !important; }
</style>
""", unsafe_allow_html=True)

def check_password():
    """I check whether the visitor has entered the correct password."""

    def password_entered():
        if st.session_state["password_input"] == st.secrets["app_password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password_input"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return

    st.text_input("Password", type="password", on_change=password_entered, key="password_input")

    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("Incorrect password")

    st.stop()