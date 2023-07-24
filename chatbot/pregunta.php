<?php

// Function to send a POST request to the API
function callOpenAIChatAPI($prompt) {
    $apiKey = ''; // Replace with your actual API key
    $url = 'https://api.openai.com/v1/chat/completions';
    $data = array(
        'model' => 'gpt-3.5-turbo',
        'messages' => array(
            array('role' => 'system', 'content' => 'You are a helpful assistant.'),
            array('role' => 'user', 'content' => $prompt)
        )
    );

    $jsonData = json_encode($data);

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',
        'Authorization: Bearer ' . $apiKey
    ));

    $response = curl_exec($ch);
    curl_close($ch);

    return json_decode($response, true);
}

// User input prompt
$userPrompt = $_GET['pregunta'];

// Call the API with the user input prompt
$response = callOpenAIChatAPI($userPrompt);

// Extract the assistant's reply from the API response
$assistantReply = $response['choices'][0]['message']['content'];

// Output the assistant's reply
echo $assistantReply;
?>