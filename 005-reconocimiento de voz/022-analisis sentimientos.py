import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained facial expression recognition model
model = load_model('path/to/pretrained_model.h5')

# Define facial expression labels
expression_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize the frame to the input size expected by the model
    input_size = (48, 48)
    resized_frame = cv2.resize(gray_frame, input_size)

    # Normalize the resized frame
    normalized_frame = resized_frame / 255.0

    # Expand the dimensions to match the input shape expected by the model
    input_data = np.expand_dims(normalized_frame, axis=-1)
    input_data = np.expand_dims(input_data, axis=0)

    # Perform facial expression recognition
    predictions = model.predict(input_data)

    # Get the predicted expression
    predicted_expression_index = np.argmax(predictions[0])
    predicted_expression = expression_labels[predicted_expression_index]

    # Display the predicted expression on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (0, 255, 0)  # Green color
    text_position = (20, 40)
    cv2.putText(frame, f"Expression: {predicted_expression}", text_position, font, font_scale, text_color, font_thickness)

    # Display the resulting frame
    cv2.imshow('Sentiment Analysis', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
