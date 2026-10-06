import streamlit as st
import pandas as pd

st.title("Dashboard")

def sparkline(points, color="#c9a227"):
    width, height = 120, 36
    max_val = max(points)
    min_val = min(points)
    range_val = max_val - min_val if max_val != min_val else 1
    step = width / (len(points) - 1)
    coords = []
    for i, val in enumerate(points):
        x = i * step
        y = height - ((val - min_val) / range_val * (height - 4)) - 2
        coords.append(f"{x:.1f},{y:.1f}")
    polyline = " ".join(coords)
    return f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}"><polyline fill="none" stroke="{color}" stroke-width="2" points="{polyline}" /></svg>'

def check_for_drop(points, threshold=0.3):
    latest = points[-1]
    baseline = sum(points[:-1]) / len(points[:-1])
    if baseline == 0:
        return False, 0
    drop_pct = (latest - baseline) / baseline
    return drop_pct <= -threshold, drop_pct

kpi_data = {
    "Total Users": [180, 210, 205, 230, 260, 255, 280],
    "New Signups This Week": [60, 72, 55, 80, 90, 85, 95],
    "Active Users": [140, 150, 148, 160, 155, 170, 165],
    "Pending Teacher Applications": [4, 6, 5, 9, 7, 12, 18]
}
kpi_values = {
    "Total Users": "12,842",
    "New Signups This Week": "486",
    "Active Users": "8,259",
    "Pending Teacher Applications": "18"
}

alerts = []
for name, points in kpi_data.items():
    is_dropping, pct = check_for_drop(points)
    if is_dropping:
        alerts.append(f"{name} is down {abs(pct) * 100:.0f}% compared to its recent average.")
if alerts:
    for alert_text in alerts:
        st.warning(f"⚠ {alert_text}")

cols = st.columns(4)
for col, (name, points) in zip(cols, kpi_data.items()):
    with col:
        st.metric(name, kpi_values[name])
        st.markdown(sparkline(points), unsafe_allow_html=True)

st.subheader("Recent Users")
users_data = {
    "Name": ["Maya Patel", "Olivia Chen", "Sofia Martinez", "Amara Williams"],
    "Email": ["maya.patel@example.com", "olivia.chen@example.com", "sofia.martinez@example.com", "amara.williams@example.com"],
    "Signup Date": ["2024-05-12", "2024-05-11", "2024-05-09", "2024-05-08"],
    "Status": ["Active", "Active", "Inactive", "Active"]
}
users_df = pd.DataFrame(users_data)
table_html = users_df.to_html(index=False, classes="scroll-table")
st.markdown(f'<div style="max-height: 350px; overflow-y: auto; border: 1px solid #e4e1da; border-radius: 6px;">{table_html}</div><style>.scroll-table {{width: 100%; border-collapse: collapse;}} .scroll-table th {{position: sticky; top: 0; background-color: #1a2744; color: white; padding: 10px; text-align: left;}} .scroll-table td {{padding: 10px; border-bottom: 1px solid #e4e1da;}}</style>', unsafe_allow_html=True)