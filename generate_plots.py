import src.summary as summary
import src.division_subplots as division_subplots
import src.summary_normalized as summary_normalized
import src.division_subplots_normalized as division_subplots_normalized
import os

os.makedirs("./results", exist_ok=True)

y_limits = [7.5,14.5]
plot_defs = {
    "2018": {
        "arrow_x": [
            [70, 20],
            [65, 70],
            [55, 80],
            [70, 50],
        ],
        "an_x": [
            [90, 40],
            [70, 85],
            [55, 80],
            [80, 40],
        ],
        "an_y_off": [
            [-2, 2.5],
            [ 2.5, 2.5],
            [ 2,   2.5],
            [ 2.5, 2.5]
        ],
        "y_limits": y_limits
    },
    "2019": {
        "arrow_x": [
            [70, 80],
            [65, 60],
            [55, 80],
            [60, 50],
        ],
        "an_x": [
            [65, 75],
            [70, 60],
            [50, 80],
            [60, 70],
        ],
        "an_y_off": [
            [-1.4, 2.5],
            [ 2.5, 2],
            [ 3,   2.5],
            [ 2.5, 2.5]
        ],
        "y_limits": y_limits
    }
}

for year, plot_coords in plot_defs.items():
    summary.plot(year)
    division_subplots.plot(year)
    summary_normalized.plot(year)
    division_subplots_normalized.plot(year, plot_coords)