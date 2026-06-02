import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/SampleSuperstore.csv"
)

conn = sqlite3.connect(
    "sales.db"
)

df.to_sql(
    "sales_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created")