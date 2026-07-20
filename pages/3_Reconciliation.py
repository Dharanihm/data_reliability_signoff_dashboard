import streamlit as st

from utils.loader import load_source,load_warehouse

from utils.metrics import reconciliation

source = load_source()

warehouse = load_warehouse()

diff = reconciliation(source,warehouse)

st.title("Source vs Warehouse")

col1,col2 = st.columns(2)

col1.metric("Source Rows",len(source))

col2.metric("Warehouse Rows",len(warehouse))

if diff == 0:

    st.success("Reconciliation Successful")

else:

    st.error(f"Difference = {diff}") 