import streamlit as st
import pandas as pd

st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")

st.title("📊 PhonePe Transaction Insights Dashboard")
st.markdown("### Digital Payment Analysis using PhonePe Pulse Data")

df = pd.read_csv("outputs/aggregated_transaction.csv")

st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", sorted(df["State"].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))
quarter = st.sidebar.selectbox("Select Quarter", sorted(df["Quarter"].unique()))

filtered_df = df[
    (df["State"] == state) &
    (df["Year"] == year) &
    (df["Quarter"] == quarter)
]

col1, col2, col3 = st.columns(3)

col1.metric("Total Transaction Amount", f"₹ {filtered_df['Amount'].sum():,.2f}")
col2.metric("Total Transaction Count", f"{filtered_df['Count'].sum():,.0f}")
col3.metric("Transaction Categories", filtered_df["Type"].nunique())

st.subheader("Transaction Amount by Category")
category_amount = filtered_df.groupby("Type")["Amount"].sum()
st.bar_chart(category_amount)

st.subheader("Year-wise Transaction Trend")
year_trend = df.groupby("Year")["Amount"].sum()
st.line_chart(year_trend)

st.subheader("Top 10 States by Transaction Amount")
top_states = df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_states)

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)