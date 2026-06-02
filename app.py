import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_csv,
    load_excel,
    load_database
)

from utils.kpi_calculator import calculate_kpis
from utils.insights import generate_insights

from utils.charts import (
    category_sales_chart,
    region_sales_chart,
    top_subcategory_chart,
    profit_chart,
    state_sales_chart,
    revenue_trend_chart
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Sales & Revenue Analysis Dashboard")
st.markdown(
    "Analyze sales performance, revenue trends, profit insights, and business performance."
)

# --------------------------------------------------
# DATA SOURCE SELECTION
# --------------------------------------------------

st.sidebar.header("Data Source")

source = st.sidebar.radio(
    "Choose Source",
    [
        "CSV",
        "Excel",
        "Database"
    ]
)

df = None

# --------------------------------------------------
# CSV
# --------------------------------------------------

if source == "CSV":

    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file:
        df = load_csv(uploaded_file)

# --------------------------------------------------
# EXCEL
# --------------------------------------------------

elif source == "Excel":

    uploaded_file = st.sidebar.file_uploader(
        "Upload Excel File",
        type=["xlsx"]
    )

    if uploaded_file:
        df = load_excel(uploaded_file)

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

elif source == "Database":

    try:
        df = load_database()
    except Exception as e:
        st.error(f"Database Error: {e}")

# --------------------------------------------------
# PROCESS DATA
# --------------------------------------------------

if df is not None:

    df.columns = df.columns.str.strip()

    required_columns = [
        "Sales",
        "Profit",
        "Quantity",
        "Category",
        "Sub-Category",
        "Region",
        "Segment",
        "State",
        "Order Date"
    ]

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:

        st.error(
            f"Missing Required Columns: {missing_columns}"
        )

        st.stop()

    # ----------------------------------------------
    # FILTERS
    # ----------------------------------------------

    st.sidebar.header("Filters")

    region_filter = st.sidebar.multiselect(
        "Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    category_filter = st.sidebar.multiselect(
        "Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    segment_filter = st.sidebar.multiselect(
        "Segment",
        options=sorted(df["Segment"].unique()),
        default=sorted(df["Segment"].unique())
    )

    filtered_df = df[
        (df["Region"].isin(region_filter))
        &
        (df["Category"].isin(category_filter))
        &
        (df["Segment"].isin(segment_filter))
    ]

    # ----------------------------------------------
    # KPIs
    # ----------------------------------------------

    kpis = calculate_kpis(filtered_df)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Sales",
        f"${kpis['sales']:,.2f}"
    )

    col2.metric(
        "Total Profit",
        f"${kpis['profit']:,.2f}"
    )

    col3.metric(
        "Total Quantity",
        f"{kpis['quantity']:,}"
    )

    col4.metric(
        "Total Orders",
        f"{kpis['orders']:,}"
    )

    col5.metric(
        "Profit Margin",
        f"{kpis['margin']:.2f}%"
    )

    st.divider()

    # ----------------------------------------------
    # REVENUE TREND
    # ----------------------------------------------

    st.subheader("📈 Revenue Trend")

    st.plotly_chart(
        revenue_trend_chart(filtered_df),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # CHART ROW 1
    # ----------------------------------------------

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.plotly_chart(
            category_sales_chart(filtered_df),
            use_container_width=True
        )

    with chart_col2:

        st.plotly_chart(
            region_sales_chart(filtered_df),
            use_container_width=True
        )

    st.divider()

    # ----------------------------------------------
    # CHART ROW 2
    # ----------------------------------------------

    chart_col3, chart_col4 = st.columns(2)

    with chart_col3:

        st.plotly_chart(
            top_subcategory_chart(filtered_df),
            use_container_width=True
        )

    with chart_col4:

        st.plotly_chart(
            profit_chart(filtered_df),
            use_container_width=True
        )

    st.divider()

    # ----------------------------------------------
    # STATE ANALYSIS
    # ----------------------------------------------

    st.subheader("🏛 State Analysis")

    st.plotly_chart(
        state_sales_chart(filtered_df),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # BUSINESS INSIGHTS
    # ----------------------------------------------

    st.subheader("💡 Business Insights")

    insights = generate_insights(
        filtered_df
    )

    for insight in insights:
        st.success(insight)

    st.divider()

    # ----------------------------------------------
    # DATA PREVIEW
    # ----------------------------------------------

    st.subheader("📄 Filtered Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

else:

    st.info(
        "Select a data source and load data to begin analysis."
    )