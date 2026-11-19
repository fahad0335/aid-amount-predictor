# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: raw data -> clean -> validate -> save cleaned data + metrics.
import matplotlib
matplotlib.use("Agg")  # without seeing the chart, save it to a file
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd

REPORTS = "outputs/reports/"
FIGURES = "outputs/figures/"

BLUE = "#2563EB"
ORANGE = "#F97316"
GREY = "#CBD5E1"
TEXT = "#1E293B"

plt.rcParams.update({
    "font.size": 11,
    "axes.edgecolor": GREY,
    "axes.labelcolor": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def clean_axes(ax):
    """Halka grid, sirf horizontal lines (parhne mein aasaan)."""
    ax.grid(axis="y", color="#E2E8F0", linewidth=1)
    ax.set_axisbelow(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))


def chart_total_by_year():
    df = pd.read_csv(REPORTS + "summary_by_year.csv", index_col="fiscal_year")
    total = df["sum"] / 1e6
    peak_year = total.idxmax()

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.fill_between(total.index, total, color=BLUE, alpha=0.12)
    ax.plot(total.index, total, color=BLUE, linewidth=2.5)
    ax.scatter([peak_year], [total[peak_year]], color=BLUE, s=60, zorder=3)
    ax.annotate(f"Peak: {peak_year}\n{total[peak_year]:,.0f} million",
                xy=(peak_year, total[peak_year]),
                xytext=(peak_year + 1.5, total[peak_year] * 0.95),
                arrowprops={"arrowstyle": "-", "color": GREY}, color=TEXT)
    ax.set_title("US aid to Pakistan peaked in " + str(peak_year),
                 loc="left", fontsize=14, fontweight="bold", color=TEXT)
    ax.set_xlabel("Fiscal year")
    ax.set_ylabel("Total aid (million US dollars)")
    ax.set_ylim(bottom=0)
    clean_axes(ax)
    fig.tight_layout()
    fig.savefig(FIGURES + "chart1_total_by_year.png", dpi=150)
    plt.close(fig)


def chart_economic_vs_military():
    df = pd.read_csv(REPORTS + "pivot_year_by_assistance.csv", index_col="fiscal_year")
    colors = {"Economic": BLUE, "Military": ORANGE}

    fig, ax = plt.subplots(figsize=(9, 5))
    for col in df.columns:
        series = (df[col] / 1e6).dropna()
        ax.plot(series.index, series, color=colors.get(col, GREY),
                linewidth=2.5, label=col)
    ax.set_title("Economic and military aid over time",
                 loc="left", fontsize=14, fontweight="bold", color=TEXT)
    ax.set_xlabel("Fiscal year")
    ax.set_ylabel("Total aid (million US dollars)")
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False, loc="upper right")
    clean_axes(ax)
    fig.tight_layout()
    fig.savefig(FIGURES + "chart2_economic_vs_military.png", dpi=150)
    plt.close(fig)


def chart_top_agencies():
    s = pd.read_csv(REPORTS + "top10_agencies.csv", index_col=0).iloc[:, 0]
    s = (s / 1e9).sort_values()  # billion mein, chhota neeche bara upar
    colors = [GREY] * len(s)
    colors[-1] = BLUE  # sab se bari agency highlight

    fig, ax = plt.subplots(figsize=(10, 5.5))
    bars = ax.barh(s.index, s, color=colors)
    for bar, value in zip(bars, s):
        ax.text(value + 0.1, bar.get_y() + bar.get_height() / 2,
                f"{value:.2f}", va="center", color=TEXT)
    ax.set_title("Three agencies deliver most US aid to Pakistan",
                 loc="left", fontsize=14, fontweight="bold", color=TEXT)
    ax.set_xlabel("Total aid 2001-2021 (billion US dollars)")
    ax.set_ylabel("Implementing agency")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    fig.savefig(FIGURES + "chart3_top_agencies.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    chart_total_by_year()
    chart_economic_vs_military()
    chart_top_agencies()
    print("3 charts saved in outputs/figures/")