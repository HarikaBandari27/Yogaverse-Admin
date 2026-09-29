import streamlit as st
import pandas as pd

st.title("Yogaverse Admin Console")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Users", "12,842")
col2.metric("New Signups This Week", "486")
col3.metric("Active Users", "8,259")
col4.metric("Pending Teacher Applications", "18")

st.subheader("Recent Users")

users_data = {
    "Name": ["Maya Patel", "Olivia Chen", "Sofia Martinez", "Amara Williams"],
    "Email": ["maya.patel@example.com", "olivia.chen@example.com", "sofia.martinez@example.com", "amara.williams@example.com"],
    "Signup Date": ["2024-05-12", "2024-05-11", "2024-05-09", "2024-05-08"],
    "Status": ["Active", "Active", "Inactive", "Active"]
}

users_df = pd.DataFrame(users_data)
st.dataframe(users_df)