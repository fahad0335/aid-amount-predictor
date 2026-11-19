# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: made 3 charts from the analysis data.
import matplotlib
matplotlib.use("Agg")  # without seeing the chart, save it to a file
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

REPORTS = "outputs/reports/"
FIGURES = "outputs/figures/"


def chart_total_by_year():
    df = pd.read_csv(REPORTS + "summary_by_year.csv", index_col="fiscal_year")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(df.index, df["sum"] / 1e6, marker="o")
    ax.set_title("Total US aid to Pakistan by fiscal year")
    ax.set_xlabel("Fiscal year")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylabel("Total amount (million US dollars)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURES + "chart1_total_by_year.png", dpi=150)
    plt.close(fig)


def chart_economic_vs_military():
    df = pd.read_csv(REPORTS + "pivot_year_by_assistance.csv", index_col="fiscal_year")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for col in df.columns:
        ax.plot(df.index, df[col] / 1e6, marker="o", label=col)
    ax.set_title("Economic vs military aid by fiscal year")
    ax.set_xlabel("Fiscal year")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylabel("Total amount (million US dollars)")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURES + "chart2_economic_vs_military.png", dpi=150)
    plt.close(fig)


def chart_top_agencies():
    s = pd.read_csv(REPORTS + "top10_agencies.csv", index_col=0).iloc[:, 0]
    s = s.sort_values()  # chhota neeche, bara upar
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(s.index, s / 1e6)
    ax.set_title("Top 10 implementing agencies by total aid (2001-2021)")
    ax.set_xlabel("Total amount (million US dollars)")
    ax.set_ylabel("Implementing agency")
    fig.tight_layout()
    fig.savefig(FIGURES + "chart3_top_agencies.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    chart_total_by_year()
    chart_economic_vs_military()
    chart_top_agencies()
    print("3 charts saved in outputs/figures/")