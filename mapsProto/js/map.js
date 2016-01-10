var map, pointarray, heatmap, gradient;

function initMap() {
    /* Data points defined as a mixture of WeightedLocation and LatLng objects */
    var heatMapData = [];
    
    $.getJSON("js/chickenJson10000.js", function(data){
        for (var i = 0; i < data.tableData.length; i++) {
            heatMapData.push({
                location: new google.maps.LatLng(data.tableData[i].lat, data.tableData[i].lon),
                weight: data.tableData[i].weight
            });
        }
        
        var london = new google.maps.LatLng(51.528867, -0.118061);

        map = new google.maps.Map(document.getElementById('map'), {
          center: london,
          zoom: 11,
//          mapTypeId: google.maps.MapTypeId.SATELLITE
        });

        heatmap = new google.maps.visualization.HeatmapLayer({
          data: heatMapData,
		  radius: 15*Math.pow(2,map.getZoom()-11)
        });
        heatmap.setMap(map);
        changeGradient();
        setLegendGradient();
        setLegendLabels();
        
        google.maps.event.addListener(map, 'zoom_changed', function () {
            heatmap.setOptions({radius:15*Math.pow(2,map.getZoom()-11)});
        });
        
    });
}

function changeGradient() {
  gradient = [
    'rgba(0, 0, 0, 0)',
    'rgba(109, 83, 16, 0.6)',
    'rgba(174,132, 26, 0.8)',
    'rgba(196,149, 28, 0.9)',
    'rgba(218,165, 32, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function setLegendGradient() {
    var gradientCss = '(left';
    for (var i = 0; i < gradient.length; ++i) {
        gradientCss += ', ' + gradient[i];
    }
    gradientCss += ')';
    
    $('#legendGradient').css('background', '-webkit-linear-gradient' + gradientCss);
    $('#legendGradient').css('background', '-moz-linear-gradient' + gradientCss);
    $('#legendGradient').css('background', '-o-linear-gradient' + gradientCss);
    $('#legendGradient').css('background', 'linear-gradient' + gradientCss);
}

function setLegendLabels() {
        var legendWidth = $('#legendGradient').outerWidth();
          $('#legend').append($('<div>').css({
            'position': 'absolute',
            'right': 0 + 'px',
            'top': '18px',
            'text-align': 'center'
        }).html('More chicken'));  
}


