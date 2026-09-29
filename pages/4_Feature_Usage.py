import streamlit as st
import pandas as pd

st.set_page_config(page_title="Feature Usage", layout="wide", initial_sidebar_state="expanded")

from auth import check_password
check_password()

st.title("Feature Usage")

st.info("Feature reporting will connect to PostHog once product tracking has been added to the site. These engagement signals are placeholders for now.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Weekly Active Members", "3,782")
col2.metric("Practices Started", "6,904")
col3.metric("Avg. Session Length", "24 min")
col4.metric("Saved Practices", "1,864")

st.subheader("Feature Engagement")

features_data = {
    "Feature": ["Practice Library", "Saved Practices", "Teacher Profiles", "Daily Intention"],
    "Count": [3418, 1864, 1203, 927],
    "Change": ["+14.6%", "+9.2%", "+18.4%", "+7.8%"]
}

features_df = pd.DataFrame(features_data)
st.dataframe(features_df)