import make_chart_normalized
import make_chart
import make_team_charts
import make_team_charts_normalized
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
    make_team_charts_normalized.plot(year, plot_coords)