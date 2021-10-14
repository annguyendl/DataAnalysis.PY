import justpy as jp
from datetime import datetime
from pytz import utc
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("./resources/reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_avg_crs1 = data.groupby(["Month", "Course Name"]).mean().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by course monthly'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course view", classes="text-h3 text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h4 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_avg_crs1.index)
    
    hc_data = [{"name":v1, "data":[v2 for v2 in month_avg_crs1[v1]]} for v1 in month_avg_crs1.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)
