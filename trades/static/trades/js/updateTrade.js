let updateButton = document.querySelectorAll(".updateButton");

for (let i = 0; i < updateButton.length; i++) {
    updateButton[i].addEventListener("click", (e) => {
        let id = e.target.getAttribute("data-id");
        let pkInput = document.querySelector("#pk");

        pkInput.value = id;
        console.log(pkInput.value)
        //Ajax Request
            $.ajax({
                url: 'data/' + id,
                method: 'POST',
                //data: id,
                success: function (res) {

                    let ticker = document.getElementById("updateTicker");
                    let position = document.getElementById("updatePosition");
                    let shares = document.getElementById("updateShares");
                    let entryDate = document.getElementById("entry-date");
                    let exitDate = document.getElementById("exit-date");
                    let entryPrice = document.getElementById("updateEntryPrice");
                    let exitPrice = document.getElementById("updateExitPrice");
                    let entryComments = document.getElementById("updateEntryComments");
                    let exitComments = document.getElementById("updateExitComments");

                    ticker.value = res[0].ticker;
                    position.value = res[0].position;
                    shares.value = res[0].shares;
                    entryDate.value = moment(res[0].entry_date).format("MM/DD/YY");
                    exitDate.value = moment(res[0].exit_date).format("MM/DD/YY");
                    entryPrice.value = res[0].entry_price;
                    exitPrice.value = res[0].exit_price;
                    exitComments.value = res[0].exit_comments;
                    entryComments.value = res[0].entry_comments;
                },
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('X-CSRFToken', csrf_token)
                },
            })
    });
}
