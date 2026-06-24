import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Database-Backed AI Application",
    page_icon="🗄️",
    layout="wide"
)

st.title("Final Project Starter App")

st.write(
    """
    This Streamlit application will eventually allow users to inspect,
    query, or interact with a database-backed AI feature.
    """
)

sample_data = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Example A", "Example B", "Example C"],
        "status": ["New", "In Progress", "Complete"]
    }
)

st.subheader("Sample Data Display")
st.dataframe(sample_data)