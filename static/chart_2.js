var x_array = []
var y_array = []

d3.json("http://localhost:5000/api/data").then((data) => {
    
    Object.values(data).forEach(element => {
        x_array.push(element["Hazard_Type"])
        y_array.push(element["Count_Displacement"])
    });

  var trace1 = {
    x: x_array,
    y: y_array,
    type: "bar"
  };
  
  var data = [trace1];
  
  // Note that we omitted the layout object this time
  // This will use default parameters for the layout
  Plotly.newPlot("my_dataviz_1", data);
  
})