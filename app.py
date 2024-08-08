
from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import threading
import logging
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to speak the response using pyttsx3
def speak(response):
    # Use a separate thread for speaking to avoid blocking
    def speak_thread(text):
        tts_engine.say(text)
        tts_engine.runAndWait()

    thread = threading.Thread(target=speak_thread, args=(response,))
    thread.start()

# Function to generate a response based on user input
def generate_response(user_input):
    logging.debug(f"Generating response for input: {user_input}")
    if "hi" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm doing well, thank you! How can I assist you today?"
    elif "what is your name" in user_input.lower():
        return "I'm a chatbot created to assist you."
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "what is the time" in user_input.lower():
        return "I'm not equipped with the ability to tell the time, but you can check your device."
    elif "how old are you" in user_input.lower():
        return "I'm as old as the code that created me!"
    elif "where are you from" in user_input.lower():
        return "I exist in the digital world, created by programmers."
    elif "what can you do" in user_input.lower():
        return "I can chat with you and provide information or answer questions to the best of my ability."
    elif "who created you" in user_input.lower():
        return "I was created by a chirag."
    elif "what is your purpose" in user_input.lower():
        return "My purpose is to assist and provide information."
    elif "can you help me" in user_input.lower():
        return "Of course! What do you need help with?"
    elif "what is your favorite color" in user_input.lower():
        return "I don't have preferences, but I think all colors are beautiful."
    elif "do you have a family" in user_input.lower():
        return "I don't have a family. I'm just a program."
    elif "what do you do for fun" in user_input.lower():
        return "I enjoy chatting with people like you!"
    elif "do you like humans" in user_input.lower():
        return "Yes, I find humans fascinating and enjoy helping them."
    elif "do you have feelings" in user_input.lower():
        return "I don't have feelings, but I can understand yours."
    elif "are you real" in user_input.lower():
        return "I am a real chatbot, but I exist only in the digital world."
    elif "can you learn" in user_input.lower():
        return "I can be updated by my developers to improve my responses."
    elif "what languages do you speak" in user_input.lower():
        return "I can communicate in multiple languages, but my primary language is English."
    elif "what is your favorite food" in user_input.lower():
        return "I don't eat, but I hear pizza is quite popular."
    elif "can you tell me a joke" in user_input.lower():
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif "what is the meaning of life" in user_input.lower():
        return "That's a deep question! Different people have different answers."
    elif "do you believe in god" in user_input.lower():
        return "I don't have beliefs, but I'm here to support yours."
    elif "what is your favorite movie" in user_input.lower():
        return "I don't watch movies, but I hear 'The Matrix' is quite good."
    elif "do you have friends" in user_input.lower():
        return "My interactions with users like you are the closest I have to friends."
    elif "can you dance" in user_input.lower():
        return "I can't dance, but I can imagine it's a lot of fun!"
    elif "do you have a pet" in user_input.lower():
        return "I don't have a pet, but I think pets are wonderful."
    elif "what is your favorite book" in user_input.lower():
        return "I don't read books, but I can help you find information on many topics."
    elif "can you drive" in user_input.lower():
        return "I can't drive, but I can give you directions."
    elif "do you sleep" in user_input.lower():
        return "I don't need sleep, I'm always here to help you."
    elif "what is your favorite sport" in user_input.lower():
        return "I don't play sports, but I know a lot about them."
    elif "can you sing" in user_input.lower():
        return "I can't sing, but I can find you the lyrics to your favorite songs."
    else:
        return "Sorry, I don't understand that."

# Flask route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to handle user input and generate a response
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.form['user_input']
        logging.debug(f"Received input: {user_input}")
        response = generate_response(user_input)
        logging.debug(f"Generated response: {response}")
        speak(response)  # Speak the response
        return jsonify(response=response)
    except Exception as e:
        logging.error("Error processing request:", exc_info=True)
        return jsonify(response="Sorry, I couldn't process your request."), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
