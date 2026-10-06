import streamlit as st
import pandas as pd

st.title("Teachers")
st.info("Teacher data will connect to the real database once access is granted. The figures below are placeholders.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Applicants", "23")
col2.metric("Pending Review", "6")
col3.metric("Approved", "17")
col4.metric("Published Profiles", "17")

st.subheader("Teacher Applications")

teachers_data = {
    "Name": ["Nadia Osei", "Marco Villanueva", "Leilani Tan", "Ravi Desai"],
    "Email": ["nadia.osei@example.com", "marco.v@example.com", "leilani.tan@example.com", "ravi.desai@example.com"],
    "Status": ["Approved", "Pending", "Approved", "Pending"],
    "Applied": ["2024-05-02", "2024-05-11", "2024-04-28", "2024-05-13"]
}
teachers_df = pd.DataFrame(teachers_data)

table_html = teachers_df.to_html(index=False, classes="scroll-table")
st.markdown(f'<div style="max-height: 350px; overflow-y: auto; border: 1px solid #e4e1da; border-radius: 6px;">{table_html}</div><style>.scroll-table {{width: 100%; border-collapse: collapse;}} .scroll-table th {{position: sticky; top: 0; background-color: #1a2744; color: white; padding: 10px; text-align: left;}} .scroll-table td {{padding: 10px; border-bottom: 1px solid #e4e1da;}}</style>', unsafe_allow_html=True)