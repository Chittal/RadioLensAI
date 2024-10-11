function filterReports() {
    const input = document.getElementById('search-patient');
    const filter = input.value.toLowerCase();
    const table = document.querySelector('.report-table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) { // Start at 1 to skip the header
        const cells = rows[i].getElementsByTagName('td');
        let found = false;

        // Check Patient ID and Name for matches
        for (let j = 0; j < cells.length; j++) {
            if (cells[j]) {
                const cellValue = cells[j].textContent || cells[j].innerText;
                if (cellValue.toLowerCase().indexOf(filter) > -1) {
                    found = true;
                    break;
                }
            }
        }

        rows[i].style.display = found ? '' : 'none'; // Show or hide the row
    }
}
