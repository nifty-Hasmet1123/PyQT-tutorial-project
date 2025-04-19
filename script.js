document.addEventListener("DOMContentLoaded", () => {
    setDescriptionOnSQLTable();
    setMatPlotLibData();
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

function setMatPlotLibData() {
    const data = {
        ".subplots()": "Can <b>generate</b> one or more <b>plots</b> in a single figure",
        ".plot()": "Try to <b>plot the data</b> that it is given",
        ".show()": "<b>Opens and displays</b> the plot once completed",
        ".set_xlabel() / .set_ylabel() / .set_title()": "Allows you to <b>give a title</b> to the Chart, X Axis and Y Axis",
        ".figure()": "<b>Create a new figure</b> or get a reference to an existing figure",
        ".draw()": "Used to explicitly <b>redraw the figure</b> and update its contents"
    };
    const tableRow = document.querySelectorAll(".plt-body-tr");

    if (tableRow.length == Object.keys(data).length) {
        
        Object.entries(data).forEach((item, index) => {
            const [key, value] = item;
            const tdLabelKey = document.createElement("td");
            const tdLabelValue = document.createElement("td");
            
            tdLabelKey.textContent = key;
            tdLabelValue.innerHTML = value;

            tableRow[index].appendChild(tdLabelKey);
            tableRow[index].appendChild(tdLabelValue);
        })
    }
}