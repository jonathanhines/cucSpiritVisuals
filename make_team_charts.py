import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import scipy.stats

filePath = "CUC2019_charts.csv"
df = pd.read_csv(filePath)
print(df)

chart_title = "CUC2019 Average Spirit Score by Division"
chart_file_name = "CUC2019_SOTG_vs_rank_by_division.png"

# Table of results 
divisions = df["Division"].unique()
fig, axs = plt.subplots(4, 2, figsize=(12,16), dpi=300)

print(divisions)
row = 0
column = 0
for i, division in enumerate(divisions):
    df_div = df[df["Division"] == division]
    ax = axs[row, column]
    ax.plot(
        df_div["Score"],
        df_div["Spirit"],
        linestyle="none",
        # linewidth=genderLineWidths[i],
        marker=".",
    )
    b, m = polyfit(df_div["Score"], df_div["Spirit"], 1)
    m, b, r_value, p_value, std_err = scipy.stats.linregress(df_div["Score"], df_div["Spirit"])
    ax.plot(
        df_div["Score"],
        b + m * df_div["Score"],
        linestyle='-',
        label= "spirit = " + "{:.2f}".format(m) + " x rank + " + "{:.2f}".format(b) + "\n" + r'$\sigma_{est}$' + " = " + "{:.2f}".format(std_err),
    )
    # ax.ylabel('Average Spirit Score')
    # ax.xlabel('Tournament Rank')
    xmax = df_div["Score"].max()
    step = 1
    if xmax > 8:
        step = 2

    if xmax > 16:
        step = 4

    ax.set_xticks(np.arange(step, xmax + step, step))
    ax.set_xlim([0,xmax + 1])
    ax.legend(loc='lower right')
    # ax.set(xlabel='Rank', ylabel='Spirit')
    ax.set_axisbelow(True)
    ax.grid(color='#EEEEEE', linestyle='-', linewidth=1)
    ax.set_title(division)
    if column < 1:
        column += 1
    elif column == 1:
        row += 1
        column = 0

fig.text(0.5, 0.04, 'Tournament Standings Rank', ha='center', va='center')
fig.text(0.06, 0.5, 'Average Spirit Score', ha='center', va='center', rotation='vertical')
fig.suptitle("CUC 2019 Division Team Spirit Scores vs Rank", fontsize=16, y=0.96)
plt.subplots_adjust(
    top=0.92,
    bottom=0.08,
    hspace= 0.3,
)

plt.savefig(chart_file_name)
plt.close()

print("Saved plot \"" + chart_title + "\" to file \"" + chart_file_name + "\"")