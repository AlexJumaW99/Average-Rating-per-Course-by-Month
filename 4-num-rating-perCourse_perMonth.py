import pandas 
import justpy as jp

df = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
#print(df)
df['Month'] = df['Timestamp'].dt.strftime('%Y-%m')
#print(df[:50])

#Group data by course and by month 
avg_month = df.groupby(['Month','Course Name'])['Rating'].mean().unstack()
print(avg_month)

chart_def = '''
 {
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average rating per course per month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
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
            text: 'Avg Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
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
'''

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Course Review Analysis', classes='text-h3 text-center')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(avg_month.index)
    hc.options.series = [{'name':v1,'data':[v2 for v2 in avg_month[v1]]} for v1 in avg_month.columns]

    return wp 

jp.justpy(app)


#print(avg_month)