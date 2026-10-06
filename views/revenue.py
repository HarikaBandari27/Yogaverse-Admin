import streamlit as st
import pandas as pd

st.set_page_config(page_title="Revenue", layout="wide", initial_sidebar_state="expanded")

from auth import check_password
check_password()

st.title("Revenue")

st.info("Payments are not live yet. These are planning estimates based on the sample member mix and placeholder pricing.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Estimated MRR", "$18,460")
col2.metric("Projected ARR", "$221,520")
col3.metric("Paid Members", "462")
col4.metric("Trial Conversion", "4.1%")

st.subheader("Subscription Mix")

plans_data = {
    "Plan": ["Monthly Membership", "Annual Membership", "Teacher Membership"],
    "Members": [286, 144, 32],
    "Share": ["61.9%", "31.2%", "6.9%"],
    "Estimated MRR": ["$8,294", "$8,640", "$1,526"]
}

plans_df = pd.DataFrame(plans_data)

table_html = plans_df.to_html(index=False, classes="scroll-table")

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