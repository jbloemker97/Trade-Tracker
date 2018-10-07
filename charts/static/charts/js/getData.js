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

// PnL
$.ajax({
    url: "/charts/data/",
    method: "GET",
    error: function (res) {
        console.log(res);
    }
})
.done(function (res) {
    let pnl = document.getElementById("charts-pnl");
    pnl.innerHTML = "$" + res[res.length - 1].account_balance;
});

// Counts & Winning Percentage
$.ajax({
    url: "/charts/data/wins",
    method: "GET",
    error: function (res) {
        console.log(res);
    },
    success: function (res) {
        console.log(res)
        let winPercent = document.getElementById("winningPercentage");
        let winCount = document.getElementById("win-count");
        let loseCount = document.getElementById("lose-count");

        winCount.innerHTML = res["wins"];
        loseCount.innerHTML = res["losses"];
        winPercent.innerHTML = res["percent"] * 100 + "%";
    }
})


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
                pricesPerDate[el.exit_date] += parseInt(el.account_balance);
            }else {
                pricesPerDate[el.exit_date] = parseInt(el.account_balance);
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
                    fillColor : "#ffff00",
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

let date_sort_asc = function (date1, date2) {
    if (date1 > date2) return 1;
    if (date1 < date2) return -1;
    return 0;
  };

