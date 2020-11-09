var labels = []
var values = []

d3.json("http://localhost:5000/api/data_3").then((data) => {
    
    Object.values(data).forEach(element => {
        labels.push(element["Country"])
        values.push(element["total_displacements"])
    });
  
  console.log(labels)
  console.log(values)

  var trace1 = {
    values: values,
    labels: labels,
    type: "pie"
  };

  // var layout = {
  //   height: 400,
  //   width: 500
  // };
  
  var data = [trace1];
  
  // Note that we omitted the layout object this time
  // This will use default parameters for the layout
  // Plotly.newPlot("my_dataviz_3", data, layout);
  Plotly.newPlot("my_dataviz_3", data);

  
})