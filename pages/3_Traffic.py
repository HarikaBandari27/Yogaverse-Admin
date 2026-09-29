import streamlit as st
import pandas as pd

st.set_page_config(page_title="Traffic", layout="wide", initial_sidebar_state="expanded")

from auth import check_password
check_password()
st.title("Traffic")

st.info("Traffic reporting will connect to Google Analytics once site tracking has been added. Until then, the figures below are sample data.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Unique Visitors", "4,820")
col2.metric("Sessions", "6,957")
col3.metric("Avg. Engagement", "2m 36s")
col4.metric("Member Conversion", "7.0%")

st.subheader("Acquisition Channels")

channels_data = {
    "Channel": ["Organic Search", "Direct", "Instagram", "Newsletter"],
    "Sessions": [2412, 1648, 982, 741],
    "Visitors": [1876, 1312, 791, 573],
    "Engagement": ["2m 18s", "3m 05s", "1m 52s", "3m 42s"],
    "Conversion": ["8.2%", "7.8%", "5.6%", "11.3%"]
}

channels_df = pd.DataFrame(channels_data)
st.dataframe(channels_df)