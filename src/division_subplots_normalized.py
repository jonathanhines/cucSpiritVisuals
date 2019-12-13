import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import scipy.stats

def plot(year, coords):
    filePath = "./data/CUC" + year + ".csv"
    chart_title = "CUC" + year + " Average Spirit Score by Division"
    chart_file_name = "./results/CUC" + year + "_SOTG_vs_rank_by_division_normalized.png"
    df = pd.read_csv(filePath)

    # Table of results 
    divisions = df["Division"].unique()
    divisions.sort()
    global_spirit_mean = df["Spirit"].mean()
    x_limits = [-5, 105]
    fig, axs = plt.subplots(4, 2, figsize=(12,16), dpi=300, sharex=False, sharey=False)

    row = 0
    column = 0
    for division in divisions:
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
        m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
        ax.plot(
            x_limits,
            [m * x_limit + b for x_limit in x_limits],
            linestyle='-',
            color="#FD7F28"
        )
        ax.plot(
            x,
            y,
            linestyle="none",
            marker=".",
            color="#2678B2"
        )

        a_x = coords["arrow_x"][row][column]
        a_y = m * a_x + b
        ax.annotate(
            'slope = ' + "{:.4f}".format(m) + "\n" + r'$\sigma_{est}$' + " = " + "{:.4f}".format(std_err) + "\n" + r'$r$' + " = " + "{:.4f}".format(r_value), 
            xy=(a_x, a_y),
            xytext=(coords["an_x"][row][column], a_y + coords["an_y_off"][row][column] ), textcoords='data',
            arrowprops=dict(arrowstyle='->', facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
        )
        # ax.ylabel('Average Spirit Score')
        # ax.xlabel('Tournament Rank')

        ax.set_xticks(np.arange(0, 120, 20))
        ax.set_xlim(x_limits)
        ax.set_ylim(coords["y_limits"])
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
    fig.suptitle("CUC " + year + " Division Team Spirit Scores vs Normalized Rank", fontsize=16, y=0.96)
    plt.subplots_adjust(
        top=0.91,
        bottom=0.08,
        hspace= 0.3,
    )

    plt.savefig(chart_file_name)
    plt.close()

    print("Saved plot \"" + chart_title + "\" to file \"" + chart_file_name + "\"")