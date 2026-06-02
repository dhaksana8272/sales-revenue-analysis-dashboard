# def calculate_kpis(df):

#     total_sales = df["Sales"].sum()

#     total_profit = df["Profit"].sum()

#     total_quantity = df["Quantity"].sum()

#     total_orders = len(df)

#     profit_margin = (
#         total_profit / total_sales
#     ) * 100

#     return {
#         "sales": total_sales,
#         "profit": total_profit,
#         "quantity": total_quantity,
#         "orders": total_orders,
#         "margin": profit_margin
#     }


def calculate_kpis(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_quantity = df["Quantity"].sum()

    total_orders = len(df)

    profit_margin = (
        total_profit /
        total_sales
    ) * 100

    return {
        "sales": total_sales,
        "profit": total_profit,
        "quantity": total_quantity,
        "orders": total_orders,
        "margin": profit_margin
    }