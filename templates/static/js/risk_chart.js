document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("riskChart").getContext("2d");
  const chartData = JSON.parse(
    document.getElementById("riskChart").dataset.chart
  );

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Healthy", "Moderate Risk", "High Risk"],
      datasets: [
        {
          label: "User Count",
          data: chartData,
          backgroundColor: ["#38b000", "#f9c74f", "#f94144"],
          borderColor: "#fff",
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              return `${context.label}: ${context.raw}`;
            },
          },
        },
      },
    },
  });
});
