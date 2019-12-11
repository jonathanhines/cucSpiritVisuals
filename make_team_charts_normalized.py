import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import scipy.stats

filePath = "CUC2019_charts.csv"
df = pd.read_csv(filePath)

chart_title = "CUC2019 Average Spirit Score by Division"
chart_file_name = "CUC2019_SOTG_vs_rank_by_division_normalized.png"

# Table of results 
divisions = df["Division"].unique()
global_spirit_mean = df["Spirit"].mean()
# Where on the line will the arrow point
a_x = [70, 80, 55, 70, 40, 70, 70, 50]
# Where will the text be relative to the point on the line
an_x = [-5, 10, 5, 20, 20, 10, -10, 10]
an_y = [-1.4, 2, 2.5, 2, 2, 2.5, 2, 2.5]
x_limits = [-5, 105]
y_limits = [7.5,14.5]
fig, axs = plt.subplots(4, 2, figsize=(12,16), dpi=300, sharex=False, sharey=False)

row = 0
column = 0
for i, division in enumerate(divisions):
    df_div = df[df["Division"] == division]
    score_max = df_div["Score"].max()
    x = 100 * (df_div["Score"].values - 1) / (score_max - 1)
    y = df_div["Spirit"].values
    spirit_mean = np.mean(y)
    ax = axs[row, column]
    ax.plot(
        x_limits,
        [spirit_mean, spirit_mean],
        linestyle=':',
        alpha=0.4,
        color="#3636a3"
    )
    ax.plot(
        x_limits,
        [global_spirit_mean, global_spirit_mean],
        linestyle='--',
        alpha=0.4,
        color="#468c3a"
    )
    ax.plot(
        x,
        y,
        linestyle="none",
        # linewidth=genderLineWidths[i],
        marker=".",
    )
    m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    ax.plot(
        x,
        b + m * x,
        linestyle='-',
        #label= "spirit = " + "{:.3f}".format(m) + " x  + " + "{:.2f}".format(b) + "\n" + r'$\sigma_{est}$' + " = " + "{:.2f}".format(std_err),
    )

    a_y = m * a_x[i] + b
    ax.annotate(
        'slope = ' + "{:.4f}".format(m) + "\n" + r'$\sigma_{est}$' + " = " + "{:.4f}".format(std_err) + "\n" + r'$r$' + " = " + "{:.4f}".format(r_value), 
        xy=(a_x[i], a_y),
        xytext=(a_x[i] + an_x[i], a_y + an_y[i] ), textcoords='data',
        arrowprops=dict(arrowstyle='->', facecolor='black'),
        horizontalalignment='right', verticalalignment='top',
    )
    # ax.ylabel('Average Spirit Score')
    # ax.xlabel('Tournament Rank')

    ax.set_xticks(np.arange(0, 120, 20))
    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_axisbelow(True)
    ax.grid(color='#EEEEEE', linestyle='-', linewidth=1)
    ax.set_title(division + " (" + r'$\mu$' + " = " + "{:.2f}".format(spirit_mean) + ")")
    if column < 1:
        column += 1
    elif column == 1:
        row += 1
        column = 0

fig.text(0.5, 0.04, 'Normalized Rank\n(% teams Ranked Higher)', ha='center', va='center', fontsize=14)
fig.text(0.5, 0.94, "(" + r'$\mu$' + " = " + "{:.2f}".format(global_spirit_mean) + ")", ha='center', va='center', fontsize=12)
fig.text(0.06, 0.5, 'Average Spirit Score', ha='center', va='center', rotation='vertical', fontsize=14)
fig.suptitle("CUC 2019 Division Team Spirit Scores vs Normalized Rank", fontsize=16, y=0.96)
plt.subplots_adjust(
    top=0.91,
    bottom=0.08,
    hspace= 0.3,
)

plt.savefig(chart_file_name)
plt.close()

print("Saved plot \"" + chart_title + "\" to file \"" + chart_file_name + "\"")