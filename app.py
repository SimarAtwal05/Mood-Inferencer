from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import cv2
import numpy as np

# Create the Flask application instance
app = Flask(__name__)
# Enable CORS to allow requests from the HTML file running in a browser
CORS(app)

# Define the route that will handle image uploads and mood detection
@app.route("/detect_mood", methods=["POST"])
def detect_mood():
    # Check if a file named 'image' was sent in the request
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']

    try:
        # Read the image data from the request file
        nparr = np.frombuffer(image_file.read(), np.uint8)
        # Decode the image data into an OpenCV format (numpy array)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Use DeepFace to analyze the image for emotions
        # We specify 'emotion' as the only action to analyze
        analysis = DeepFace.analyze(img, actions=['emotion'])
        
        # Check if DeepFace found any faces in the image
        if analysis:
            # The result is a list of dictionaries. We get the dominant emotion
            # from the first face found.
            dominant_emotion = analysis[0]['dominant_emotion']
            # Return the detected mood as a JSON response
            return jsonify({"mood": dominant_emotion})
        else:
            # No face was detected, return a user-friendly message
            return jsonify({"mood": "No face detected 🤷"}), 404

    except Exception as e:
        # If any other error occurs, print it to the console and return an error message
        print(f"An error occurred: {e}")
        return jsonify({"mood": "Error detecting mood 😢"}), 500

# This block ensures the server runs only when the script is executed directly
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
