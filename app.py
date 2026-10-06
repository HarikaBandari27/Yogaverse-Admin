import streamlit as st
from auth import check_password

st.set_page_config(page_title="Yogaverse Admin Console", layout="wide", initial_sidebar_state="expanded")
check_password()

overview = st.Page("views/overview.py", title="Dashboard", default=True)
users = st.Page("views/users.py", title="Users")
teachers = st.Page("views/teachers.py", title="Teachers")
revenue = st.Page("views/revenue.py", title="Plans & Revenue")
traffic = st.Page("views/traffic.py", title="Traffic")
feature_usage = st.Page("views/feature_usage.py", title="Feature Usage")


pg = st.navigation({
    "Core Structure": [overview, users, teachers],
    "Not Tracked Yet": [revenue, traffic, feature_usage],
})

pg.run()