import streamlit as st


def check_password():
    """I check whether the visitor has entered the correct password."""

    # I load my custom CSS here so it applies on every page
    st.markdown("""
    <style>
    /* I give the sidebar a thin border instead of a heavy colour */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #E5E7EB;
    }

    /* I turn each KPI into a clean white card */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 16px 20px;
    }

    [data-testid="stMetricLabel"] p {
        color: #6B7280 !important;
        font-size: 0.85rem !important;
    }

    [data-testid="stMetricValue"] {
        font-weight: 600;
    }

    /* I make the page titles bold and tight, like a SaaS dashboard */
    h1 {
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }

    /* I keep the password box readable */
    div[data-testid="stTextInput"] input {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        border: 1px solid #D1D5DB !important;
    }

    /* I fade and slide each element in as it scrolls into view */
    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @supports (animation-timeline: view()) {
        [data-testid="stMain"] [data-testid="stElementContainer"],
        [data-testid="stMain"] .element-container {
            animation: fadeUp linear both;
            animation-timeline: view();
            animation-range: entry 0% entry 40%;
        }
    }

    /* I turn the animation off for people who prefer less motion */
    @media (prefers-reduced-motion: reduce) {
        [data-testid="stMain"] [data-testid="stElementContainer"],
        [data-testid="stMain"] .element-container {
            animation: none !important;
        }
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