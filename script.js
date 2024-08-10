// Fetch parking status from the backend
async function fetchParkingStatus() {
    try {
        const response = await fetch('/api/parking-status');
        const data = await response.json();
        document.getElementById('status').innerText = `Available Spaces: ${data.availableSpaces}`;
    } catch (error) {
        console.error('Error fetching parking status:', error);
    }
}

// Fetch parking forecast from the backend
async function fetchParkingForecast() {
    try {
        const response = await fetch('/api/parking-forecast');
        const data = await response.json();
        document.getElementById('forecast-data').innerText = `Forecast for the next 24 hours: ${data.forecast}`;
    } catch (error) {
        console.error('Error fetching parking forecast:', error);
    }
}

// Initial load
fetchParkingStatus();
fetchParkingForecast();
