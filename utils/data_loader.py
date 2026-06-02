# import pandas as pd

# def load_data(path):
#     df = pd.read_csv(path)

#     df.columns = df.columns.str.strip()

#     return df



import pandas as pd
import sqlite3

def load_csv(file):
    return pd.read_csv(file)

def load_excel(file):
    return pd.read_excel(file)

def load_database():

    conn = sqlite3.connect("sales.db")

    df = pd.read_sql_query(
        "SELECT * FROM sales_data",
        conn
    )

    conn.close()

    return df