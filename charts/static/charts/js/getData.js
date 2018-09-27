// Max PnL
$.ajax({
    url: "/charts/data/max_pnl",
    method: "GET",
    error: function (res) {
        console.log(res);
    }
})
.done(function (res) {
    let biggestPnl = document.getElementById("biggest-pnl");
    biggestPnl.innerHTML = "$" + Math.round(res.pnl__max * 100) / 100;
});

// Trades PnL
$.ajax({
    url: "/charts/data",
    method: "GET",
    success: function (res) {
        let finalizedData = [];
        let labels = [];
        let pricesPerDate = {};
        res.forEach(el => {
            if (el.exit_date in pricesPerDate) {
                pricesPerDate[el.exit_date] += parseInt(el.pnl);
            }else {
                pricesPerDate[el.exit_date] = parseInt(el.pnl);
            }
        });

        for (let date in pricesPerDate) {    
            labels.push(moment(date).format('MMM Do YY'));
            finalizedData.push(pricesPerDate[date])
        }
    
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
                    data: finalizedData.sort((a, b) => a - b),
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




let date_sort_asc = function (date1, date2) {
    if (date1 > date2) return 1;
    if (date1 < date2) return -1;
    return 0;
  };

