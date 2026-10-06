import streamlit as st
import pandas as pd

st.set_page_config(page_title="Feature Usage", layout="wide", initial_sidebar_state="expanded")

from auth import check_password
check_password()

st.title("Feature Usage")

st.info("Feature reporting will connect once product analytics tracking has been added to the site. These engagement signals are placeholders for now.")

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

table_html = features_df.to_html(index=False, classes="scroll-table")

st.markdown(f"""
<div style="max-height: 350px; overflow-y: auto; border: 1px solid #e4e1da; border-radius: 6px;">
{table_html}
</div>
<style>
.scroll-table {{
    width: 100%;
    border-collapse: collapse;
}}
.scroll-table th {{
    position: sticky;
    top: 0;
    background-color: #1a2744;
    color: white;
    padding: 10px;
    text-align: left;
}}
.scroll-table td {{
    padding: 10px;
    border-bottom: 1px solid #e4e1da;
}}
</style>
""", unsafe_allow_html=True)