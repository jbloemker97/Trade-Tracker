
$.ajax({
    url: "/charts/data",
    method: "GET",
    success: function (res) {
        let finalizedData = [];
        res.forEach(el => {
            finalizedData.push(parseInt(el.pnl));
        });
    
        var ctx = document.getElementById("chart1").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["Red", "Blue", "Yellow"],
                datasets: [{
                    label: 'PNL',
                    data: finalizedData,
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    },
    error: function (err) {
        console.log(err)
    }
});

