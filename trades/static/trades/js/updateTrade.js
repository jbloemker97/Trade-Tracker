// Grab form
    // Prevent Default
    // Input row into DOM
    // Send AJAX request

    function updateTrade () {
        let form = document.querySelector("#updateForm");
        let input = form.querySelectorAll(".addInput");
        let updateButton = document.querySelectorAll(".updateButton");
        let modal = document.querySelector("#updateModal");
        
        for (let i = 0; i < updateButton.length; i++) {
            updateButton[i].addEventListener("click", function (e) {
                let id = e.target.getAttribute("data-id");
                let row = e.target.parentElement.parentElement;
                let pnlVal;
                let data = new Object();

                for (let j = 0; j < row.children.length - 2; j++) {
                    if (row.children[j].classList.contains("pnl")) {
                        // input[j].value = row.children[j].innerHTML;
                        pnlVal = row.children[j];
                    }else if (row.children[j].classList.contains("exit-comments")) {
                        input[j].value = row.children[j].innerHTML;
                    }else {
                        values = row.children[j].innerHTML;
                        input[j].value = values;
                    }
                }

                //pnlVal = pnlVal.substring(1);
                
                form.addEventListener("submit", function (e) {
                    e.preventDefault();

                    let row = document.querySelector(`[data-id="${id}"]`).parentElement.parentElement;
                    let position;
                    let entryPrice;
                    let exitPrice;
                    let shares;
                    let success = true;
                    let dataKeys = ["ticker", "position", "shares", "entry_date", "exit_date", "entry_price", "exit_price", "pnl", "entry_comments", "exit_comments"]
                    
                    for (let i = 0; i < row.children.length - 2; i++) {
                        value = input[i].value;
                        if (row.children[i].id === "position")      position = row.children[i].innerHTML;
                        if (row.children[i].id === "shares")        shares = row.children[i].innerHTML;
                        if (row.children[i].id === "entryPrice")    entryPrice = row.children[i].innerHTML;
                        if (row.children[i].id === "exitPrice")     exitPrice = row.children[i].innerHTML;
            
                        

                        if (row.children[i].className === "exitPrice" || row.children[i].className === "pnl") {
                
                            if (row.children[i].textContent[0] === "$") {
                                row.children[i].innerHTML = value;
                            }else {
                                row.children[i].innerHTML = "$" + value;
                            }
                            
                        }else {
                            row.children[i].innerHTML = value;
                        }

                        if (row.children[i].classList.contains("pnl")) {
                            // Calculate pnl
                            if (position === "Long") {
                                pnl = (parseFloat(exitPrice) - parseFloat(entryPrice)) * shares 
                            }else {
                                pnl = (parseFloat(entryPrice) - parseFloat(exitPrice)) * shares 
                            }

                            pnlVal.innerHTML = pnl;

                            console.log(pnl, typeof pnl);
                            data["pnl"] = parseFloat(pnl);
                        }else {
                            data[dataKeys[i]] = value;
                        }
                        
                    }
                    
                    data['id'] = id;

                    // Loop through data and format correctly
                    for (key in data) {
                        if (data[key][0] === '$') {
                            data[key] = data[key].slice(1);
                        }
                    }

                    $('#updateModal').modal('hide');
                    
                    //Ajax Request
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