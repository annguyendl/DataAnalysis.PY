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
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors
    title: {
        floating: true,
        align: 'left',
        text: 'Average Rating by Course and Month'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: ''
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Cancelled<br>during<br>World War II'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Soviet Union fell,<br>Germany united'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7, 7, 6, 12, 7, 9, 5, 5
        ]
    }, {
        name: "Austria",
        data: [
            0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10, 21, 9, 17, 17, 23, 16, 17
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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
