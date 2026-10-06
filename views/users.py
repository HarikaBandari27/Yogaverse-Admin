import streamlit as st
import pandas as pd

st.set_page_config(page_title="Users", layout="wide", initial_sidebar_state="expanded")

from auth import check_password
check_password()

st.title("Users")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Members", "12,842")
col2.metric("Active This Month", "8,259")
col3.metric("New This Week", "486")
col4.metric("Avg. Member Tenure", "7.4 mo")

st.subheader("Member Directory")

members_data = {
    "Member": ["Elena Rossi", "Jonah Green", "Priya Shah", "Nina Campbell"],
    "Joined": ["2024-05-14", "2024-05-13", "2024-05-12", "2024-05-10"],
    "Plan": ["Annual", "Monthly", "Trial", "Free"],
    "Status": ["Active", "Active", "Active", "Inactive"]
}

members_df = pd.DataFrame(members_data)

search_name = st.text_input("Search by member name")

if search_name:
    filtered_df = members_df[members_df["Member"].str.contains(search_name, case=False, na=False)]
else:
    filtered_df = members_df

table_html = filtered_df.to_html(index=False, classes="scroll-table")

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