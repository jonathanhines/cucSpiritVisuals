import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

def plot(year):
    filePath = "CUC" + year + "_charts.csv"
    chart_title = "CUC" + year + " Average Spirit Score vs Rank"
    chart_file_name = "CUC" + year + "_SOTG_vs_rank.png"
    df = pd.read_csv(filePath)

    colors = plt.get_cmap("tab20").colors
    # Table of results 
    divisionColors = ["#227a24", "#ba603a", "#ba603a", "#ba603a", "#ba603a", "#ba603a", "#ba603a" , "#ba603a", "#ba603a"]
    divisions = df["Division"].unique()
    divisions.sort()

    plt.figure(figsize=(12,8), dpi=300)
    for i, division in enumerate(divisions):
        df_div = df[df["Division"] == division]
        plt.plot(
            df_div["Score"],
            df_div["Spirit"],
            linestyle="none",
            # linewidth=genderLineWidths[i],
            color=colors[i],
            label=division,
            marker=".",
        )
        b, m = polyfit(df_div["Score"], df_div["Spirit"], 1)
        plt.plot(
            df_div["Score"],
            b + m * df_div["Score"],
            linestyle='-',
            color=colors[i],
        )

    plt.ylabel("Average CUC" + year + " Spirit Score")
    plt.xlabel('Final Rank based on Score')
    plt.xticks(np.arange(1, 21, 1))
    plt.legend(loc='lower right', ncol=4,)
    plt.gca().set_axisbelow(True)
    plt.grid(color='#EEEEEE', linestyle='-', linewidth=1)
    plt.title(chart_title)
    plt.savefig(chart_file_name)
    plt.close()

    print("Saved plot \"" + chart_title + "\" to file \"" + chart_file_name + "\"")