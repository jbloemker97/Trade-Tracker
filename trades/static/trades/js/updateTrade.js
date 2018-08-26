// Grab form
    // Prevent Default
    // Input row into DOM
    // Send AJAX request

    function updateTrade () {
        let form = document.querySelector("#updateForm");
        let input = form.querySelectorAll(".addInput");
        let updateButton = document.querySelectorAll(".updateButton");
        
        for (let i = 0; i < updateButton.length; i++) {
            updateButton[i].addEventListener("click", function (e) {
                let id = e.target.getAttribute("data-id");
                let row = e.target.parentElement.parentElement;
                let data = new Object();

                for (let j = 0; j < row.children.length - 2; j++) {
                    value = row.children[j].innerHTML;
                    input[j].value = value;
                }
                
                form.addEventListener("submit", function (e) {
                    e.preventDefault();

                    let row = document.querySelector(`[data-id="${id}"]`).parentElement.parentElement;
                    let dataKeys = ["ticker", "entry_date", "exit_date", "entry_price", "exit_price", "pnl", "entry_comments", "exit_comments"]
                    
                    for (let i = 0; i < row.children.length - 2; i++) {
                        value = input[i].value;
                        row.children[i].innerHTML = value;
                        data[dataKeys[i]] = value;
                    }

                    console.log(data);
                    
                    // Ajax Request
                    $.ajax({
                        url: 'update/' + id,
                        method: 'POST',
                        data: data,
                        beforeSend: function (xhr) {
                            xhr.setRequestHeader('X-CSRFToken', csrf_token)
                        }
                    })

                });
            });
        }
    }

    updateTrade();