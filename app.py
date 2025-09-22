from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
from textblob import TextBlob # Import TextBlob
import cv2
import numpy as np

# Create the Flask application instance
app = Flask(__name__)
# Enable CORS to allow requests from the HTML file running in a browser
CORS(app)

# --- NEW: Text Analysis Route ---
@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    # Get the text from the incoming JSON request
    text_data = request.get_json()
    if not text_data or 'text' not in text_data:
        return jsonify({"error": "No text provided"}), 400

    text = text_data['text']
    
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score (-1.0 to 1.0)
    polarity = blob.sentiment.polarity
    
    # Determine mood based on polarity
    mood = "Neutral 😐"
    if polarity > 0.2:
        mood = "Positive 😊"
    elif polarity < -0.2:
        mood = "Negative 😟"
        
    return jsonify({"mood": mood})

# --- Existing: Mood Detection Route ---
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
        analysis = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        
        # The result is a list of dictionaries for each face.
        dominant_emotion = analysis[0]['dominant_emotion']
        return jsonify({"mood": dominant_emotion})

    except Exception as e:
        # This can happen if no face is detected, or another error occurs
        print(f"An error occurred: {e}")
        return jsonify({"mood": "Could not analyze image 🤷"}), 500

# This block ensures the server runs only when the script is executed directly
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
