import justpy as jp
from datetime import datetime
from pytz import utc
import pandas

data = pandas.read_csv("./resources/reviews.csv", parse_dates=["Timestamp"])
data["Week"] = data["Timestamp"].dt.strftime("%Y-%U")
data["Weekday"] = data["Timestamp"].dt.strftime("%A")
data["Daynum"] = data["Timestamp"].dt.strftime("%w")
week_avg1 = data.groupby(["Weekday", "Daynum"]).mean()
week_avg1 = week_avg1.sort_values("Daynum")

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Happies day'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Week: {point.x}, Avg Rating: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rate',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course view", classes="text-h3 text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(week_avg1.index)
    hc.options.series[0].data = list(week_avg1["Rating"])
    
    return wp

jp.justpy(app)
