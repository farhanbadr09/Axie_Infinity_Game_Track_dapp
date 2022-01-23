$(document).ready(function() {

	//get canvas
	var ctx = $("#line-chartcanvas");

	var data = {
		labels : ["", "", "", "", "","",""],
		datasets : [
			{
				label : "A",
				data : [80, 80, 20, 20, 0,80,80],
				backgroundColor : "rgba(227, 35, 255, 1)",
				borderColor : "rgba(227, 35, 255, 1)",
				fill : false,
				lineTension : 0,
				pointRadius : 0
			},
			{
				label : "B",
				data : [0, 0, 80, 40, 40, 0, 0],
				backgroundColor : "rgba(77, 255, 223, 1)",
				borderColor : "rgba(77, 255, 223, 1)",
				fill : false,
				lineTension : 0,
				pointRadius : 0
			}
		]
	};

	var options = {
		title : {
			display : true,
			position : "top",
			fontSize : 14,
			fontColor : "white",
			backgroundColor: "black"
		},
		legend : {
			display : true,
			position : "bottom"
		}
		
	};

	var chart = new Chart( ctx, {
		type : "line",
		data : data,
		options : options
	} );

});