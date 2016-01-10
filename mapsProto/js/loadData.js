$(document).ready(function(){
    $.getJSON("js/sfDataJson.js", function(data){
        var Append = "test";
        for (var i = 0; i < data.tableData.length; i++) {
            Append += data.tableData[i].lat + " ";
        }
        $("div").append(Append);
    });
});
