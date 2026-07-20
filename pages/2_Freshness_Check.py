import streamlit as st

from utils.loader import load_pipeline

from utils.metrics import freshness

df = load_pipeline()

latest = freshness(df)

st.title("Pipeline Freshness")

st.metric("Latest Refresh",latest)

st.dataframe(df) 