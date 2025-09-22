# Mood Inferencer 🌿

Ever wonder what your face is telling the world? Or maybe you just want to answer a fun quiz to check your vibe? We've got you covered\! **Mood Inferencer** is a delightful web app that guesses your mood in two awesome ways.

## ✨ Features

  * **🤔 Two Ways to Play:** Choose between a quick, rule-based quiz to check in with yourself or use our AI-powered camera feature for real-time facial analysis.
  * **🤖 AI Magic:** The camera mode is powered by the impressive `DeepFace` library, which analyzes your facial expression to detect your dominant emotion. It's like magic, but it's science\!
  * **🎨 Sleek & Snazzy UI:** A fully responsive and modern interface built with HTML, CSS, and Tailwind CSS. It features a cool gradient background and fun, bubbly buttons.
  * **⚡ Instant Feedback:** Get your results immediately, whether you finish the quiz or snap a picture.


## 🚀 How It Works

So, how does the magic happen? You have two paths to choose from on the home page:

### 1\. The Quiz Whiz Method (`quiz.html`)

This method uses a fun, built-in scoring system.

1.  You answer three simple questions about your morning, energy levels, and weather preference.
2.  Our JavaScript code peeks at a special, hidden `<ruleml>` tag in the HTML to find the score for each of your answers.
3.  It crunches the numbers, and based on your total score, we reveal your inferred mood\! ✨

### 2\. The Camera Power Method (`camera.html`)

This is where the AI comes out to play\!

1.  Smile for the camera\! (Or don't, we're not judging). You grant access to your webcam, and a live video feed appears on the screen.
2.  Click the **"📸 Capture & Detect Mood"** button. A snapshot of your lovely face is sent to our Python Flask backend.
3.  The backend, our mission control, uses `DeepFace` and `OpenCV` to process the image and find your dominant emotion (like "happy", "sad", or "neutral").
4.  *Boom\!* The detected mood is sent right back to your browser and displayed on your screen.

### 3\. The Word Weaver Method (`text.html`)
This is for when you'd rather write it out.

1.  You type a few sentences about your day or how you're feeling into the text area.
2.  Click the "Analyze My Mood" button. Your text is sent to a dedicated endpoint on our Flask backend.
3.  The backend uses the TextBlob library to perform sentiment analysis, calculating a "polarity" score for your text.
4.  Based on whether the score is positive, negative, or neutral, your mood is inferred and sent back to be displayed on your screen.


-----

## 🛠️ Tech Stack

This project is a blend of cool frontend and powerful backend technologies.

#### ✨ **Frontend** (The Pretty Face)

  * **HTML5**
  * **CSS3** (with **Tailwind CSS**)
  * **JavaScript** (for interactivity and API calls)

#### 🧠 **Backend** (The Brains of the Operation)

  * **Python**
  * **Flask:** Our lightweight and speedy web server.
  * **DeepFace:** The star of the show for all facial analysis.
  * **TextBlob:** For simple and effective sentiment analysis of your written thoughts.
  * **OpenCV:** Helps us handle and process the images from your camera.
  * **Flask-CORS:** Lets our frontend and backend talk to each other without any drama.

-----

## 📂 Project Structure

Here's a map of the project so you know your way around:

```
/
├── 🏠 index.html      # The main landing page
├── 📝 quiz.html        # The quiz and its logic
├── 📸 camera.html      # The camera and its logic
├── ✍️ text.html        # The text analysis page and its logic
├── 🎨 style.css       # The one stylesheet to rule them all
└── 🧠 app.py         # Our Python backend server
```

-----

## ⚙️ Get It Running

Ready to try it out locally? Let's get you set up\!

#### **Prerequisites**

  * Python 3.8+
  * pip (Python's package installer)
  * A modern web browser (like Chrome or Firefox)
  * A webcam (for the AI magic\!)

### Step 1: Grab the Code

Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/mood-inferencer.git
cd mood-inferencer
```

### Step 2: Get the Backend Ready (For the AI Magic ✨)

The backend is only needed for the camera feature.

1.  **Create a virtual environment** (Pro-tip: this keeps your project dependencies tidy\!).

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

2.  **Install the Python goodies.**
    Create a file named `requirements.txt` in the project folder and add this content:

    ```
    Flask
    Flask-Cors
    deepface
    opencv-python
    numpy
    ```

    Now, run this command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    *(Psst\! The first time you run the app, `DeepFace` might take a moment to download its pre-trained models. This is a one-time thing\!)*

### Step 3: Launch\! 🚀

1.  **Start the backend server:**

    ```bash
    python app.py
    ```

    Your terminal should tell you the server is running on `http://127.0.0.1:5000`.

2.  **Open the frontend:**
    Find the `index.html` file in your project folder and open it with your web browser.

That's it\! You're all set to explore your moods. Have fun\!
