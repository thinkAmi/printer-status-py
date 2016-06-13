from flask import Flask, render_template
from printer import PX105

app = Flask(__name__)
app.config.from_object('config')

class HighCharts(object):
    def __init__(self, chart_id, chart, series, xAxis, plot_options):
        self.chart_id = chart_id
        self.chart = chart
        self.series = series
        self.xAxis = xAxis
        self.plot_options = plot_options


@app.route("/")
@app.route("/px105")
def index():
    p = PX105()
    
    charts = []
    for i, tank in enumerate(p.tanks):
        id = "chart_{}".format(i)
        charts.append(HighCharts(
            chart_id = id,
            chart = {"renderTo": id, "type": "column", "height": 400,},
            series = [{"name": "使用済", "data": [100 - tank.rest_volume], "pointWidth": 40, "color": "gray"},
                      {"name": "インク残量", "data": [tank.rest_volume], "pointWidth": 40, "color": tank.color}],
            xAxis = {"categories": [tank.name]},
            plot_options = { "column": { "stacking": "percent"}},
        ))
        
    return render_template("index.html", charts=charts, title="PX-105")


if __name__ == "__main__":
	app.run(debug = True, host="0.0.0.0", port=8080, passthrough_errors=True)