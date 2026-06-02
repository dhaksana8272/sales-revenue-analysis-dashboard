def generate_insights(df):

    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    most_profitable = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .idxmax()
    )

    highest_discount = (
        df.groupby("Sub-Category")["Discount"]
        .mean()
        .idxmax()
    )

    insights = [
        f"Top Revenue Category: {top_category}",
        f"Best Performing Region: {top_region}",
        f"Most Profitable Sub-Category: {most_profitable}",
        f"Highest Discount Sub-Category: {highest_discount}"
    ]

    return insights