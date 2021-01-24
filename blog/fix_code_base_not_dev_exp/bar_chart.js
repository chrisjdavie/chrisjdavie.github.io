function draw_chart(
    plot_id,
    after_label,
    other = null,
    code_debt = null,
    new_work = null,
    servers = null) {

    var patternSize = 20;
    var datasets = [];
    if (other) {
        datasets.push({
            label: 'Other',
            backgroundColor: pattern.draw('diagonal', 'rgba(31, 119, 180)'), //',
            data: other
        })
    }
    if (servers) {
        datasets.push({
            label: 'Servers',
            backgroundColor: pattern.draw('diamond', 'rgba(255, 127, 14)'),
            data: servers
        })
    }
    if (code_debt) {
        datasets.push({
            label: 'Code problems',
            backgroundColor: pattern.draw('zigzag-vertical', 'rgba(44, 160, 44)'),
            data: code_debt
        })
    }
    if (new_work) {
        datasets.push({
            label: 'New Work',
            backgroundColor: pattern.draw('diagonal-right-left', 'rgba(214, 39, 40)'),
            data: new_work
        })
    }
    var barChartData = {
        labels: ['Before', after_label],
        datasets: datasets
    };
    var ctx = document.getElementById(plot_id).getContext('2d');
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
            },
            aspectRatio: 1.75
        }
    });
}
