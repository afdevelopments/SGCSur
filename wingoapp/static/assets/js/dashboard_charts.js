document.addEventListener("DOMContentLoaded", function () {
  // Carga los paquetes necesarios de Google Charts
  google.charts.load("current", { packages: ["corechart"] });
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    // Obtiene los datos de la vista

    console.log("Datos recibidos:", conveniosPorCarrera); // Imprime los datos recibidos

    const carreras = conveniosPorCarrera.map((carrera) => carrera.nombreCarrera);
    const conveniosCount = conveniosPorCarrera.map((carrera) => carrera.convenios_count);

    const data = new google.visualization.DataTable();
    data.addColumn("string", "Carrera");
    data.addColumn("number", "Convenios");

    for (let i = 0; i < carreras.length; i++) {
      data.addRow([carreras[i], conveniosCount[i]]);
    }

    const options = {
      title: "Convenios por carrera",
      hAxis: { title: "Carrera", titleTextStyle: { color: "#333" } },
      vAxis: { minValue: 0 },
      chartArea: { width: "50%", height: "70%" },
    };

    const chart = new google.visualization.ColumnChart(document.getElementById("convenios_por_carrera"));
    chart.draw(data, options);
  }

  function drawLineChart() {
    console.log("Datos recibidos para convenios por mes:", conveniosPorMes); // Imprime los datos recibidos

    const meses = conveniosPorMes.map((mes) => new Date(mes.month));
    const conveniosCountMes = conveniosPorMes.map((mes) => mes.convenios_count);

    console.log("Meses:", meses); // Imprime los meses
    console.log("Convenios por mes:", conveniosCountMes); // Imprime la cantidad de convenios por mes

    // Gráfico de líneas
    const dataLine = new google.visualization.DataTable();
    dataLine.addColumn("date", "Mes");
    dataLine.addColumn("number", "Convenios");

    for (let i = 0; i < meses.length; i++) {
      dataLine.addRow([meses[i], conveniosCountMes[i]]);
    }

    const optionsLine = {
      title: "Convenios por mes en los últimos 12 meses",
      hAxis: { title: "Mes", titleTextStyle: { color: "#333" } },
      vAxis: { minValue: 0 },
      chartArea: { width: "70%", height: "70%" },
    };

    const chartLine = new google.visualization.LineChart(document.getElementById("convenios_por_mes"));
    chartLine.draw(dataLine, optionsLine);
  }

  google.charts.setOnLoadCallback(drawLineChart);
});
