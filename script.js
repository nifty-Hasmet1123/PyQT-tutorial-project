document.addEventListener("DOMContentLoaded", () => {
    setDescriptionOnSQLTable();
})

function setDescriptionOnSQLTable() {
    const data = {
        ".addDatabase()": "Establishing a Connection to a SQLite Database",
        ".setDatabaseName()": "Set the name of your new Database",
        ".open()": "Python open method to open our Database"
    }


    const tbodyTableRow = document.querySelectorAll("#sql-tbody > tr");
    
    tbodyTableRow.forEach(element => {
        const td = document.createElement("td");
        let textContent = element.textContent.trim();
        
        td.textContent = data[textContent];
        element.appendChild(td);
    })
}