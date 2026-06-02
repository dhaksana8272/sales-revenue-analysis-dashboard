import plotly.express as px
import pandas as pd
import plotly.express as px
def category_sales_chart(df):

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    return fig


def region_sales_chart(df):

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Sales by Region"
    )

    return fig


def top_subcategory_chart(df):

    top_products = (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Sub-Category",
        y="Sales",
        title="Top 10 Sub-Categories"
    )

    return fig


def profit_chart(df):

    profit_data = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        profit_data,
        x="Sub-Category",
        y="Profit",
        title="Top Profitable Products"
    )

    return fig


def state_sales_chart(df):

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig = px.bar(
        state_sales,
        x="State",
        y="Sales",
        title="Top States by Sales"
    )

    return fig
def revenue_trend_chart(df):

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    trend = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="M"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="Order Date",
        y="Sales",
        title="Monthly Revenue Trend",
        markers=True
    )

    return fig