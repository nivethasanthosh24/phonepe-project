import os
import matplotlib.pyplot as plt

OUTPUT_PATH = "../eda_outputs"

os.makedirs(OUTPUT_PATH, exist_ok=True)


def save_top_states_chart(df):
    top_states = df.groupby("state")["amount"].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    top_states.plot(kind="bar")
    plt.title("Top 10 States by Transaction Amount")
    plt.xlabel("State")
    plt.ylabel("Transaction Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_PATH}/top_10_states.png")
    plt.close()


def save_transaction_type_chart(df):
    type_dist = df.groupby("type")["amount"].sum()

    plt.figure(figsize=(8, 8))
    type_dist.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Transaction Type Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_PATH}/transaction_type_distribution.png")
    plt.close()


def save_year_trend_chart(df):
    year_trend = df.groupby("year")["amount"].sum()

    plt.figure(figsize=(8, 5))
    year_trend.plot(kind="line", marker="o")
    plt.title("Year-wise Transaction Trend")
    plt.xlabel("Year")
    plt.ylabel("Transaction Amount")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_PATH}/year_wise_trend.png")
    plt.close()


def save_quarter_trend_chart(df):
    quarter_trend = df.groupby(["year", "quarter"])["amount"].sum()

    plt.figure(figsize=(10, 5))
    quarter_trend.plot(kind="line", marker="o")
    plt.title("Quarter-wise Transaction Trend")
    plt.xlabel("Year, Quarter")
    plt.ylabel("Transaction Amount")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_PATH}/quarter_wise_trend.png")
    plt.close()


def generate_all_charts(df):
    save_top_states_chart(df)
    save_transaction_type_chart(df)
    save_year_trend_chart(df)
    save_quarter_trend_chart(df)

    print("✅ All EDA charts saved in eda_outputs folder")