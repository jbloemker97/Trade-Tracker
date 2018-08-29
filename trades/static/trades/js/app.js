// Remove empty $
let rows = document.querySelectorAll(".trade-row");

// Loop through rows
for (let i = 0; i < rows.length; i++) {
    let children = rows[i].children;
    // Loop through row horizontal
    for (let j = 0; j < children.length; j++)  {
        if (children[j].innerHTML == "$") {
            children[j].innerHTML = "";
        }

        // If long
        if (children[j].innerHTML === "Long") {
            let entryPrice = rows[i].getElementsByClassName("entryPrice")[0];
            let exitPrice = rows[i].getElementsByClassName("exitPrice")[0];
            let pnl = rows[i].getElementsByClassName("pnl")[0];
            
            // Completed long trade
            if (entryPrice.textContent.length > 1 && exitPrice.textContent.length > 1) {
                exitPrice = String(exitPrice.textContent.slice(1));
                entryPrice = String(entryPrice.textContent.slice(1));
                
                exitPrice = Number(exitPrice)
                entryPrice = Number(entryPrice)
            
                
                //If successfull trade
                if (exitPrice > entryPrice) {
                    pnl.style.color = "green";
                }else {
                    pnl.style.color = "red";
                }
            }
        }else if (children[j].innerHTML === "Short") { // If short
            let entryPrice = rows[i].getElementsByClassName("entryPrice")[0];
            let exitPrice = rows[i].getElementsByClassName("exitPrice")[0];
            let pnl = rows[i].getElementsByClassName("pnl")[0];
            
            // Completed long trade
            if (entryPrice.textContent.length > 1 && exitPrice.textContent.length > 1) {
                exitPrice = String(exitPrice.textContent.slice(1));
                entryPrice = String(entryPrice.textContent.slice(1));
                
                exitPrice = Number(exitPrice)
                entryPrice = Number(entryPrice)
            
                
                //If successfull trade
                if (exitPrice < entryPrice) {
                    pnl.style.color = "green";
                }else {
                    pnl.style.color = "red";
                }
            }
        }
    }
}