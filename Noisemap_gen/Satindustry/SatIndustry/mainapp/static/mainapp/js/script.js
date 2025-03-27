const map = L.map('map').setView([20.5937, 78.9629], 5); // Default center: India

let currentMarker;

const coordinatesDiv = document.getElementById('coordinates');
const NoisePanel = document.getElementById('noise-panel');
const noiseResultsDiv = document.getElementById('noise-results');

// Add map layers, tile layers, etc. (Keep these as they are)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);


function addMarker(lat, lon, title) {
    if (currentMarker) map.removeLayer(currentMarker);
    currentMarker = L.marker([lat, lon]).addTo(map).bindPopup(title).openPopup();
    map.setView([lat, lon], 13);
}

function toggleSpinner(show) {
    document.getElementById('spinner').style.display = show ? 'flex' : 'none';
}


let currentChart = null;
let currentChart2 = null;

async function createAirQualityChart(lat, lon) {
    if (currentChart2) {
        currentChart2.destroy();
        currentChart2 = null;
    }


    try {
        const response = await fetch(historicalAQIDataUrl);
        if (!response.ok) {
            const message = `Error fetching historical air quality data: ${response.status} ${response.statusText}`;
            throw new Error(message);
        }
        const responseData = await response.json();
        const airQualityData = responseData.airQualityData; // Access airQualityData from response JSON

        const ctx = document.getElementById('chart2').getContext('2d');

        currentChart2 = new Chart(ctx, {
            type: 'line',
            data: {
                labels: airQualityData.map(entry => entry.year),
                datasets: [{
                    label: 'Average Air Quality Index (AQI)',
                    data: airQualityData.map(entry => entry.averageAQI),
                    borderColor: '#ff5722',
                    backgroundColor: 'rgba(255, 87, 34, 0.2)',
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Year',
                        },
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'AQI',
                        },
                        ticks: {
                            beginAtZero: true,
                        }
                    }
                }
            }
        });


    } catch (error) {
        console.error('Error fetching historical air quality data:', error);
        //alert('Failed to fetch historical air quality data.');
    }
}

function createChart(data) {
    if (currentChart) {
        currentChart.destroy();
        currentChart = null;
    }
    const ctx = document.getElementById('chart').getContext('2d');
    currentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(entry => entry.year),
            datasets: [{
                label: 'Average Temperature (°C)',
                data: data.map(entry => entry.temp),
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.2)',
                fill: true,
                tension: 0.4,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: '#ddd',
                    },
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                },
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Year',
                        color: '#ddd',
                    },
                    ticks: {
                        color: '#ddd',
                    },
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)',
                        color: '#ddd',
                    },
                    ticks: {
                        color: '#ddd',
                    },
                },
            },
        },
    });
}



// Handle Search Button
document.getElementById('search-button').addEventListener('click', () => {
    console.log("Search button clicked!"); // ADDED console.log
    const location = document.getElementById('search-input').value;
    if (location) {
        fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${location}`)
            .then(response => response.json())
            .then(data => {
                if (data && data.length > 0) {
                    const { lat, lon, display_name } = data[0];
                    addMarker(lat, lon, display_name);
                    fetchData(lat, lon);
                } else {
                    alert('Location not found');
                }
            })
            .catch(error => {
                console.error('Error fetching location:', error);
                alert('Failed to fetch location.');
            });
    } else {
        alert('Please enter a location.');
    }
});

// Handle Location Button
document.getElementById('location-button').addEventListener('click', () => {
    console.log("Location button clicked!"); // ADDED console.log
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const { latitude, longitude } = position.coords;
            addMarker(latitude, longitude, 'Your Location');
            fetchData(latitude, longitude);
        }, error => {
            console.error('Error fetching geolocation:', error);
            alert('Failed to get your location.');
        });
    } else {
        alert('Geolocation is not supported by your browser.');
    }
});

async function fetchData(lat, lon) {
    console.log("fetchData function called with lat:", lat, "lon:", lon);
    toggleSpinner(true);

    try {
        lat = parseFloat(lat);
        lon = parseFloat(lon);

        if (isNaN(lat) || isNaN(lon)) {
            throw new Error('Invalid latitude or longitude');
        }


        fetchNoiseData(lat, lon); // Call NoisePollution data here

    } catch (error) {
        console.error('Error fetching data:', error);
        //alert('Failed to fetch data.');
    } finally {
        toggleSpinner(false);
    }
}

async function fetchNoiseData(lat, lon) {
    toggleSpinner(true);
    console.log("fetchNoiseData function called with lat:", lat, "lon:", lon);

    const location = document.getElementById('search-input')?.value; // Ensure search-input exists
    if (!location) {
        console.error("Error: Location is empty or missing.");
        noiseResultsDiv.innerHTML = "<p>Error: Please enter a location.</p>";
        toggleSpinner(false);
        return;
    }

    NoisePanel.style.display = 'flex'; // Show Noise Panel
    noiseResultsDiv.innerHTML = "<p>Getting noise data...</p>"; // Initial message

    const noiseAnalysisUrl = `/fetch-noise-data/?location=${encodeURIComponent(location)}`; // Encode URL parameter

    try {
        const response = await fetch(noiseAnalysisUrl);
        
        if (!response.ok) {
            const message = `Error fetching Noise analysis: ${response.status} ${response.statusText}`;
            console.log("Error fetching Noise analysis:", message);
            throw new Error(message);
        }

        const noiseData = await response.json();
        console.log("Noise Analysis Data:", noiseData);

        if (!noiseData || Object.keys(noiseData).length === 0) {
            noiseResultsDiv.innerHTML = "<p>No data found for this location.</p>";
        } else {
            noiseResultsDiv.innerHTML = `
                <strong>City:</strong> ${noiseData[0].City} <br>
                <strong>Place:</strong> ${noiseData[0].Place} <br>
                <strong>Noise Level (dB):</strong> ${noiseData[0]["Noise level(dB)"]} <br>
                <strong>Category:</strong> ${noiseData[0].Category} <br>
            `;
        }
    } catch (error) {
        console.error('Error fetching Noise analysis:', error);
        noiseResultsDiv.innerHTML = `<p>Error fetching data: ${error.message}</p>`;
    } finally {
        toggleSpinner(false); // Ensure spinner is turned off
    }
}

// CLOSE NOISE PANEL BUTTON
document.getElementById('closePlanetBtn').addEventListener('click', () => {
    console.log("Close Planet Panel button clicked!");
    NoisePanel.style.display = 'none';
});