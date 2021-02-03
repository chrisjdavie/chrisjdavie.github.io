function draw_scatter_chart(pointRadius) {

    class Node {
        constructor(x, y) {
            this.x = x
            this.y = y
            this.children = []
        }
    }
    let node3 = new Node(300, 310)
    let node2 = new Node(265, 300)

    let node100 = new Node(170, 320)
    let node10 = new Node(210, 250)
    node10.children.push(node100)
    let node1 = new Node(260, 190)
    node1.children.push(node10)

    let node01 = new Node(120, 225)
    let node00 = new Node(110, 180)
    let node0 = new Node(150, 100)
    node0.children.push(node01)
    node0.children.push(node00)

    let trunkNode = new Node(301, 99)
    trunkNode.children.push(node3)
    trunkNode.children.push(node2)
    trunkNode.children.push(node1)
    trunkNode.children.push(node0)

    var player_data = []
    var heap_nodes = [...trunkNode.children];

    while (heap_nodes.length > 0) {
        var next_node = heap_nodes.pop()
        var heap_nodes = heap_nodes.concat(next_node.children)
        player_data.push({ x: next_node.x, y: next_node.y })
    }
    trunk_data = [{ x: trunkNode.x, y: trunkNode.y }]

    var lineWidth = 3
    line_colors_generation = [
        'rgba(44, 160, 44)',
        'rgba(255, 165, 0)',
        'rgba(0, 0, 0)'
    ]
    line_dash_generation = [
        [8, 8],
        [8, 4, 4, 4],
        [4, 4]
    ]

    var pointHoverBorderWidth = pointRadius / 2
    var pointHoverRadius = 1.5 * pointRadius

    var scatterChartData = {
        datasets: [{
            label: 'Players',
            data: player_data,
            backgroundColor: 'rgba(31, 119, 180)',
            pointBackgroundColor: 'rgba(31, 119, 180)',
            pointRadius: pointRadius,
            pointHoverBorderWidth: pointHoverBorderWidth,
            pointHoverRadius: pointHoverRadius
        }, {
            label: 'Trunk Node',
            data: trunk_data,
            backgroundColor: 'rgba(214, 39, 40)',
            pointBackgroundColor: 'rgba(214, 39, 40)',
            pointRadius: pointRadius,
            pointHoverBorderWidth: pointHoverBorderWidth,
            pointHoverRadius: pointHoverRadius,
            pointStyle: 'triangle'
        }, {
            type: 'line',
            label: 'Branch',
            data: trunk_data,
            pointRadius: 0,
            backgroundColor: 'white',
            borderColor: line_colors_generation[0],
            borderWidth: lineWidth,
            borderDash: line_dash_generation[0]
        }],
    };

    node_annotations = {}

    heap_nodes = [[trunkNode, 0]]

    var annotation_index = 0


    var body = document.body;
    var style = window.getComputedStyle(body, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style);

    while (heap_nodes.length > 0) {
        var next = heap_nodes.pop()
        var parent_node = next[0]
        var generation = next[1]
        parent_node.children.forEach(function (node) {
            node_annotations[annotation_index] = {
                type: 'line',
                xScaleID: 'x',
                yScaleID: 'y',
                xMin: parent_node.x,
                yMin: parent_node.y,
                xMax: node.x,
                yMax: node.y,
                borderColor: line_colors_generation[generation],
                borderWidth: lineWidth,
                borderDash: line_dash_generation[generation],
            }
            annotation_index++
            heap_nodes.push([node, generation + 1])
        });
    }
    var body = document.body;
    var style = window.getComputedStyle(body, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style);
    var ctx = document.getElementById('scatter_chart').getContext('2d');
    var myScatter = new Chart(ctx, {
        type: 'scatter',
        data: scatterChartData,
        options: {
            animation: {
                duration: 1
            },
            interaction: {
                mode: 'nearest'
            },
            plugins: {
                annotation: {
                    drawTime: 'beforeDatasetsDraw',
                    annotations: node_annotations
                },
                legend: {
                    labels: {
                        font: {
                            size: fontSize,
                        }
                    }
                }
            },
            scales: {
                x: {
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Points',
                        font: {
                            size: fontSize,
                            style: "bold"
                        }
                    },
                    ticks: {
                        font: {
                            size: fontSize
                        }
                    }
                },
                y: {
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Salary',
                        font: {
                            size: fontSize,
                            style: "bold"
                        }
                    },
                    ticks: {
                        font: {
                            size: fontSize
                        }
                    }
                }
            },
            aspectRatio: 1.5
        }
    });

    return myScatter
}

function manage_chart_dynamics() {

    function draw_scatter_chart_sized(chart) {
        if (chart) {
            chart.destroy()
        }

        if (window.innerWidth < 768) {
            new_chart = draw_scatter_chart(10)
        } else {
            new_chart = draw_scatter_chart(20)
        };
        return new_chart
    };
    chart = draw_scatter_chart_sized(null)
    window.onresize = function () {
        chart = draw_scatter_chart_sized(chart)
    };
}
