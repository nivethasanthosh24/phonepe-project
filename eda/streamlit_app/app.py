import streamlit as st
import pandas as pd
import psycopg2

# -----------------------------
# Database connection
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="phonepe_db",
    user="postgres",
    password="Nivi@2003",
    port="5432"
)

st.set_page_config(
    page_title="PhonePe Transaction Insights",
    layout="wide"
)

st.title("📊 PhonePe Transaction Insights Dashboard")

# -----------------------------
# Load data
# -----------------------------
df = pd.read_sql("SELECT * FROM aggregated_transaction", conn)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", sorted(df["state"].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))
quarter = st.sidebar.selectbox("Select Quarter", sorted(df["quarter"].unique()))

filtered_df = df[
    (df["state"] == state) &
    (df["year"] == year) &
    (df["quarter"] == quarter)
]

# -----------------------------
# KPI cards
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Transaction Amount", f"₹ {filtered_df['amount'].sum():,.2f}")
col2.metric("Total Transaction Count", f"{filtered_df['count'].sum():,.0f}")
col3.metric("Transaction Categories", filtered_df["type"].nunique())

# -----------------------------
# Charts
# -----------------------------
st.subheader("Transaction Amount by Category")
category_amount = filtered_df.groupby("type")["amount"].sum()
st.bar_chart(category_amount)

st.subheader("Year-wise Transaction Trend")
year_trend = df.groupby("year")["amount"].sum()
st.line_chart(year_trend)

st.subheader("Top 10 States by Transaction Amount")
top_states = df.groupby("state")["amount"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_states)

# -----------------------------
# Data preview
# -----------------------------
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)

conn.close()