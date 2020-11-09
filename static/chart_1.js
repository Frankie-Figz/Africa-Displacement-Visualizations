var x_array = []
var y_array = []
var dataList = []
var countryList = []
var dataTrace = []

d3.json("http://localhost:5000/api/data_2").then((data) => {
  
  Object.values(data).forEach((x) => {
    console.log(x["Country"])

    if(!countryList.includes(x["Country"]))
      countryList.push(x["Country"])
  })

  dataList = data;

}).then(() => {
  console.log(countryList)
  console.log(dataList)
  countryList.forEach((x) => {
    var filtherCountryData = dataList.filter((input) => input["Country"] == x)
    console.log(filtherCountryData["Year"])
    var x_values = filtherCountryData.map((x) => x["Year"])
    var y_values = filtherCountryData.map((x) => x["displacements"])
    
    console.log(x_values)

    var trace = {
      x: x_values,
      y: y_values,
      name: x,
      type: "plot"
    };

    dataTrace.push(trace)

  })
}).then(() => {
  console.log(dataTrace)
  Plotly.newPlot("my_dataviz_2", dataTrace);
})