// Remove empty $
let rows = document.querySelectorAll(".trade-row");

for (let i = 0; i < rows.length; i++) {
    let children = rows[i].children;
    for (let j = 0; j < children.length; j++)  {
        if (children[j].innerHTML == "$") {
            children[j].innerHTML = "";
        }
    }
}