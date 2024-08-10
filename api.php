<?php
// Database connection
$host = 'localhost';
$dbname = 'parking_db';
$user = 'root';
$pass = '';
$pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);

// API endpoint for parking status
if ($_SERVER['REQUEST_URI'] == '/api/parking-status') {
    $stmt = $pdo->query('SELECT COUNT(*) AS availableSpaces FROM parking_spaces WHERE is_occupied = 0');
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    echo json_encode($result);
}

// API endpoint for parking forecast
if ($_SERVER['REQUEST_URI'] == '/api/parking-forecast') {
    // Fetch forecast data from Python script
    $forecast = shell_exec('python3 forecast.py');
    echo $forecast;
}
?>
