import streamlit as st
import pandas as pd
import plotly.express as px

# Configure page
st.set_page_config(layout="wide")
st.title("Student Performance Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_students.csv")

df = load_data()

# Interactive widgets
subject = st.selectbox("Select Subject", ['math_score', 'science_score'])
threshold = st.slider("Passing Grade", 0, 100, 60)

# Visualization
fig = px.scatter(
    df,
    x='attendance',
    y=subject,
    color=df[subject] > threshold,
    title=f"Attendance vs {subject.replace('_', ' ').title()}"
)
st.plotly_chart(fig, use_container_width=True)
