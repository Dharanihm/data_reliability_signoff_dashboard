import streamlit as st

st.set_page_config(
    page_title="Data Reliability Sign-off Dashboard",
    page_icon="✅",
    layout="wide"
)

st.title("✅ Data Reliability Sign-off Dashboard")

st.markdown("""
This dashboard validates the trustworthiness of business data by monitoring:

- Data Completeness
- Pipeline Freshness
- Source vs Warehouse Reconciliation
- Data Reliability Sign-off

Use the sidebar to navigate.
""")

st.success("System Status : HEALTHY") 