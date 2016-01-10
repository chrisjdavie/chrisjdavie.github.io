var map, pointarray, heatmap;

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
        
        var london = new google.maps.LatLng(51.508867, -0.128061);

        map = new google.maps.Map(document.getElementById('map'), {
          center: london,
          zoom: 13,
//          mapTypeId: google.maps.MapTypeId.SATELLITE
        });

        var heatmap = new google.maps.visualization.HeatmapLayer({
          data: heatMapData,
		  radius: 15*Math.pow(2,map.getZoom()-11)
        });
        heatmap.setMap(map);
        

        google.maps.event.addListener(map, 'zoom_changed', function () {
          heatmap.setOptions({radius:15*Math.pow(2,map.getZoom()-11)});
        });      
          
    });
}
