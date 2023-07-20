<?php
$servername = "localhost";
$username = "vidaartificial";
$password = "vidaartificial";
$dbname = "vidaartificial";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Assuming you have a table called 'your_table_name'
$sql = "SELECT * FROM entidades";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Fetch data and store in an associative array
    $data = array();
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
} else {
    echo "No data found.";
}

$conn->close();

// Convert the data to JSON format
$json_data = json_encode($data);

// Set the appropriate headers to indicate JSON response
header('Content-Type: application/json');

// Send the JSON response
echo $json_data;
