document.getElementById('summarizeButton').addEventListener('click', () => {
    fetch('/summarize')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                document.getElementById('summaryText').textContent = data.error;
            } else {
                document.getElementById('summaryText').textContent = data.summary;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('summaryText').textContent = 'Error fetching summary.';
        });
});
