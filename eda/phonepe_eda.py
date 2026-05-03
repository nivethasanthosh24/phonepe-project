import pandas as pd
import psycopg2
from charts import generate_all_charts   # 👈 NEW IMPORT

# DB connection
conn = psycopg2.connect(
    host="localhost",
    database="phonepe_db",
    user="postgres",
    password="Nivi@2003",
    port="5432"
)

# Load data
query = "SELECT * FROM aggregated_transaction"
df = pd.read_sql(query, conn)

# Basic EDA (optional but good for report)
print(df.head())
print(df.info())
print(df.describe())

# 👇 THIS LINE IS IMPORTANT
generate_all_charts(df)

conn.close()