import streamlit as st
import pandas as pd

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
st.dataframe(members_df)