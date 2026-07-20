import streamlit as st

from utils.loader import load_source

from utils.metrics import completeness

df = load_source()

st.title("Data Completeness")

score = completeness(df)

st.metric("Completeness Score",f"{score}%")

st.dataframe(df)

if score > 98:

    st.success("Pipeline Complete")

else:

    st.error("Data Missing") 