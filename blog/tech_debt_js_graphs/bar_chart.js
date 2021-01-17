function draw_chart(){
    var barChartData = {
        labels: ['Before', 'After (Expected)'],
        datasets: [{
            label: 'Other',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            data: [
                40,
                40
            ]
        }, {
            label: 'Code debt',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            data: [
                50,
                5
            ]
        }, {
            label: 'New Work',
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            data: [
                10,
                55
            ]
        }]

    };
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            title: {
                display: true,
                text: ['Expected work time,', 'before and after resolving code debt'],
                fontSize: 32
            },
            legend: {
                display: true,
                labels: {
                    fontSize: 20
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
                        fontSize: 24
                    },
                    gridLines : {
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
                        labelString: 'Proportion of developer time, %',
                        fontSize: 24
                    },
                    gridLines : {
                        drawBorder: false,
                        zeroLineWidth: 0.5
                    }
                }]
            }
        }
    });
}
