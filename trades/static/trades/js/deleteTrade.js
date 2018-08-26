function deleteTrade () {
    let buttons = document.querySelectorAll(".deleteButton");
    
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function (e) {
            // Grab the id
            let id = e.target.getAttribute("data-id")
            let confirmDelete = document.querySelector("#deleteConfirmation");
            let row = e.target.parentElement.parentElement;

            confirmDelete.addEventListener("click", function () {
                // Hide the row
                row.style.display = "none";
                // Make the ajax request to our views
                $.ajax({
                    url: 'delete/' + id,
                    method: 'DELETE',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader('X-CSRFToken', csrf_token)
                    }
                })
            });
        });
    }
}

deleteTrade();