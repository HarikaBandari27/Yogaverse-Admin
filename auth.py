import streamlit as st


def check_password():
    """I check whether the visitor has entered the correct password."""

    # I load my custom CSS here so it applies on every page
    st.markdown("""
    <style>
    input[type="password"],
    div[data-testid="stTextInput"] input {
        background-color: white !important;
        color: #1f3d2f !important;
        caret-color: #1f3d2f !important;
        -webkit-text-fill-color: #1f3d2f !important;
    }

    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] span {
        color: #ffffff !important;
    }

    [data-testid="stSidebarCollapseButton"] button,
    [data-testid="stSidebarCollapseButton"] svg {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

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