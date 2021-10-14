import justpy as jp
from datetime import datetime
from pytz import utc
import pandas

data = pandas.read_csv("./resources/reviews.csv", parse_dates=["Timestamp"])
share = data.groupby(["Course Name"])["Rating"].count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Average rating by course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course view", classes="text-h3 text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h4 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc_data
    
    return wp

jp.justpy(app)
