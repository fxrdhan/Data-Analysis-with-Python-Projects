import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime("%B")

    # Order the months
    months_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    df_bar["Month"] = pd.Categorical(
        df_bar["Month"], categories=months_order, ordered=True
    )

    # Group by Year and Month and calculate the mean
    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean().reset_index()

    # Pivot the data for plotting
    df_pivot = df_bar.pivot(index="Year", columns="Month", values="value")

    # Ensure the columns (Months) are in the correct order
    df_pivot = df_pivot[months_order]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 8))
    df_pivot.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    plt.xticks(rotation=0)

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["Year"] = df_box["date"].dt.year
    df_box["Month"] = df_box["date"].dt.strftime("%b")

    # Order the months
    months_order = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    df_box["Month"] = pd.Categorical(
        df_box["Month"], categories=months_order, ordered=True
    )

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x="Year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x="Month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
