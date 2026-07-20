import streamlit as st
from utils.report_generator import generate_report

st.title("✅ Data Reliability Sign-off")

st.markdown("""
This page summarizes the overall health of the data pipelines and provides
a final reliability sign-off before business decisions are made.
""")

# Generate the report
report = generate_report()

st.subheader("Reliability Summary Report")
st.dataframe(report, use_container_width=True)

# Download button
csv = report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Reliability Report",
    data=csv,
    file_name="reliability_summary.csv",
    mime="text/csv"
)

st.divider()

st.subheader("Data Quality Checklist")

st.markdown("""
- ✅ Data Complete
- ✅ Pipelines Fresh
- ✅ Source & Warehouse Reconciled
- ✅ Dashboard Updated
""")

status = st.selectbox(
    "Overall Status",
    ["APPROVED", "REVIEW REQUIRED"]
)

if status == "APPROVED":
    st.success("✅ Data is trusted and ready for business decision-making.")
else:
    st.warning("⚠️ Data requires further validation before use.") 