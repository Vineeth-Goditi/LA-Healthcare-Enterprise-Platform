
import streamlit as st
from healthcare_engine import process_healthcare_query

st.set_page_config(
    page_title="LA Healthcare Enterprise AI Platform",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 LA Healthcare Enterprise AI Platform")

st.caption(
    "AI-powered healthcare operations assistant for claims, PBM, prior authorization, "
    "member eligibility, and pharmacy workflows."
)

with st.sidebar:
    st.header("Healthcare Modules")

    st.markdown("""
    ### Core Workflows
    - Claims Adjudication
    - Prior Authorization
    - PBM Operations
    - RxClaim Processing
    - Member Eligibility
    - Pharmacy Claims
    - Provider Assistance
    - Healthcare Policy Guidance
    """)

    st.info(
        "This project simulates enterprise healthcare AI workflows commonly "
        "used in payer and PBM environments."
    )

sample_queries = [
    "Explain claims adjudication workflow",
    "What documents are required for prior authorization?",
    "Explain member eligibility validation",
    "How does PBM support pharmacy claims?",
    "Explain RxClaim processing",
    "What are the fraud detection checks in claims processing?"
]

query = st.selectbox(
    "Choose a healthcare workflow query",
    sample_queries
)

custom_query = st.text_area(
    "Ask a healthcare operations question",
    value=query,
    height=120
)

if st.button("Generate AI Response"):

    response = process_healthcare_query(custom_query)

    st.subheader("AI Response")

    st.success(response)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Claims Processed", "2.1M+")

with col2:
    st.metric("Authorization Accuracy", "98.2%")

with col3:
    st.metric("PBM Workflow Automation", "87%")

st.warning(
    "This platform is for educational and demonstration purposes only. "
    "It does not provide real medical or insurance decisions."
)
