import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import scipy.stats

filePath = "CUC2019_charts.csv"
df = pd.read_csv(filePath)

chart_title = "CUC2019 Average Spirit Score vs Normalized Rank"
chart_file_name = "CUC2019_SOTG_vs_rank_normalized.png"

colors = plt.get_cmap("tab20").colors
# Table of results 
divisionColors = ["#227a24", "#ba603a", "#ba603a", "#ba603a", "#ba603a", "#ba603a", "#ba603a" , "#ba603a", "#ba603a"]
divisions = df["Division"].unique()
global_spirit_mean = df["Spirit"].mean()

x_limits = [-2, 102]

fig = plt.figure(figsize=(12,8), dpi=300)
ax = plt.gca()
plt.plot(
    x_limits,
    [global_spirit_mean, global_spirit_mean],
    linestyle='--',
    alpha=0.4,
    color="#468c3a"
)
score_max = df["Score"].max()
x = 100 * (df["Score"].values - 1) / (score_max - 1)
y = df["Spirit"].values
m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
plt.plot(
    x_limits,
    b + m * np.asarray(x_limits),
    linestyle='--',
    color="#000000",
)
ax.annotate(
    'slope = ' + "{:.4f}".format(m) + "\n" + r'$\sigma_{est}$' + " = " + "{:.4f}".format(std_err) + "\n" + r'$r$' + " = " + "{:.4f}".format(r_value), 
    xy=(101, 101 * m + b),
    xytext=(95, 85 * m + b + 1 ), textcoords='data',
    arrowprops=dict(arrowstyle='->', facecolor='black'),
    horizontalalignment='right', verticalalignment='top',
)
for i, division in enumerate(divisions):
    df_div = df[df["Division"] == division]
    score_max = df_div["Score"].max()
    x = 100 * (df_div["Score"].values - 1) / (score_max - 1)
    y = df_div["Spirit"].values
    plt.plot(
        x,
        y,
        linestyle="none",
        # linewidth=genderLineWidths[i],
        color=colors[i],
        label=division,
        marker=".",
    )
    m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    plt.plot(
        x,
        b + m * x,
        linestyle='-',
        color=colors[i],
    )

plt.ylabel('Average Spirit Score' + "\n" + r'$\mu$' + " = " + "{:.2f}".format(global_spirit_mean))
plt.xlabel('Normalized Rank\n(% teams Ranked Higher)')
plt.xticks(np.arange(0, 120, 20))
plt.xlim(x_limits)
plt.legend(loc='lower right', ncol=4,)
plt.gca().set_axisbelow(True)
plt.grid(color='#EEEEEE', linestyle='-', linewidth=1)
plt.title(chart_title)
plt.savefig(chart_file_name)
plt.close()

print("Saved plot \"" + chart_title + "\" to file \"" + chart_file_name + "\"")