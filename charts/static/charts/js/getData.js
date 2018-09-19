// Trades PnL
$.ajax({
    url: "/charts/data",
    method: "GET",
    success: function (res) {
        let finalizedData = [];
        let labels = [];
        res.forEach(el => {
            finalizedData.push(parseInt(el.pnl));
            labels.push(moment(el.exit_date).format('MMM Do YY'));
        });
    
        var ctx = document.getElementById("chart1").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
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
        console.log(err);
    }
});

// Compounded Growth
$.ajax({
    url: "/charts/data",
    method: "GET",
    success: function (res) {
        let finalizedData = [];
        res.forEach(el => {
            finalizedData.push(parseInt(el.pnl));
        });
    
        var ctx = document.getElementById("compoundedGrowth").getContext('2d');
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

