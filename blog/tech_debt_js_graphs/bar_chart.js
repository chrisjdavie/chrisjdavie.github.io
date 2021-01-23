function draw_chart() {
    var patternSize = 20;
    var barChartData = {
        labels: ['Before', 'After (Expected)'],
        datasets: [{
            label: 'Other',
            backgroundColor: pattern.draw('diagonal', 'rgba(31, 119, 180)'), //',
            data: [
                40,
                40
            ]
        }, {
            label: 'Code debt',
            backgroundColor: pattern.draw('zigzag-vertical', 'rgba(44, 160, 44)'),
            data: [
                50,
                5
            ]
        }, {
            label: 'New Work',
            backgroundColor: pattern.draw('diagonal-right-left', 'rgba(214, 39, 40)'),
            data: [
                10,
                55
            ]
        }]

    };
    var ctx = document.getElementById('myChart').getContext('2d');
    var body = document.body;
    var style = window.getComputedStyle(body, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style);
    // body.style.fontSize;
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            legend: {
                display: true,
                labels: {
                    fontSize: fontSize
                }
            },
            tooltips: {
                mode: 'index',
                intersect: false
            },
            scales: {
                xAxes: [{
                    lineWeight: 2,
                    stacked: true,
                    ticks: {
                        fontSize: fontSize,
                        fontStyle: "bold"
                    },
                    gridLines: {
                        lineWidth: 0
                    }
                }],
                yAxes: [{
                    stacked: true,
                    display: true,
                    ticks: {
                        stepSize: 25,
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Proportion of dev time, %',
                        fontSize: fontSize,
                        fontStyle: "bold"
                    },
                    gridLines: {
                        drawBorder: false,
                        zeroLineWidth: 0.5
                    }
                }]
            }
        }
    });
}
