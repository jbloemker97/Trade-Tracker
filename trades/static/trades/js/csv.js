let download = document.querySelector("#downloadCSV");

download.addEventListener("click", function () {
    //Ajax Request
    $.ajax({
        url: 'csv_write/',
        method: 'GET',
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
    })
});