import pandas as pd
import numpy as np

df = pd.read_csv("data/SampleSuperstore.csv")

start_date = pd.Timestamp("2023-01-01")
end_date = pd.Timestamp("2025-12-31")

df["Order Date"] = pd.to_datetime(
    np.random.randint(
        start_date.value // 10**9,
        end_date.value // 10**9,
        len(df)
    ),
    unit="s"
)

df.to_csv(
    "SampleSuperstore_Updated.csv",
    index=False
)