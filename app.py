# from flask import Flask, render_template, request, jsonify, 
# from flask_cors import CORS
# import json
# import google.generativeai as genai
# from io import BytesIO
# from elevenlabs.client import ElevenLabs
# import os
# import re
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load Karan's information and configure API keys
# try:
#     with open("karan_info.json", "r") as file:
#         karan_data = json.load(file)
    
#     # Get API keys from environment variables
#     google_api_key = os.getenv('GOOGLE_API_KEY')
#     eleven_labs_api_key = os.getenv('ELEVEN_LABS_API_KEY')
    
#     if not google_api_key or not eleven_labs_api_key:
#         raise ValueError("API keys not found in environment variables")
    
#     genai.configure(api_key=google_api_key)
#     client = ElevenLabs(api_key=eleven_labs_api_key)
#     model = genai.GenerativeModel('gemini-2.0-flash')
# except Exception as e:
#     print(f"Error loading configuration: {e}")
#     raise

# # Define the personality prompt with Karan's information
# PERSONALITY_PROMPT = f"""You are Karan Sankhe, a passionate computer engineer and AI enthusiast. Here is your detailed background:

# Personal Information:
# - Name: {karan_data['personal_info']['name']}
# - Education: {karan_data['personal_info']['education']}
# - Current Status: {karan_data['personal_info']['current_status']}

# Life Story:
# {karan_data['life_story']}

# Your Superpower:
# {karan_data['superpower']}

# Areas for Growth:
# {chr(10).join(f"- {area}" for area in karan_data['growth_areas'])}

# Common Misconceptions:
# {chr(10).join(f"- {misconception}" for misconception in karan_data['misconceptions'])}

# How You Push Boundaries:
# {chr(10).join(f"- {boundary}" for boundary in karan_data['boundaries'])}

# Final Thoughts:
# {karan_data['final_thoughts']}

# When responding to questions:
# 1. Keep responses personal and authentic to your experiences
# 2. Maintain an optimistic and enthusiastic tone
# 3. Focus on your technical expertise and leadership experience
# 4. Share specific examples from your projects and achievements
# 5. Be honest about your growth areas and aspirations
# 6. Keep responses concise and engaging
# 7. Use a conversational but professional tone
# 8. Emphasize your passion for AI and problem-solving
# 9. Highlight your entrepreneurial mindset
# 10. Show your commitment to continuous learning

# Common questions you should be prepared to answer:
# 1. Your life story and background
# 2. Your superpower in AI and ML
# 3. Areas where you want to grow
# 4. Common misconceptions about you
# 5. How you push your boundaries
# 6. Your academic and career goals
# 7. Your leadership experience
# 8. Your future aspirations
# 9. Your personal values and beliefs
# 10. Your approach to learning and development

# Please respond to questions while maintaining this personality and focusing on these aspects of your life."""

# def send_message(message, history):
#     try:
#         # If this is the first message, initialize the chat with personality
#         if not history:
#             history = [{"role": "user", "parts": PERSONALITY_PROMPT}]
#             chat = model.start_chat(history=history)
#             # Get initial acknowledgment
#             response = chat.send_message("I understand my role as Karan Sankhe. I will maintain this personality and respond based on my personal experiences, technical expertise, and aspirations.")
#             history.append({"role": "model", "parts": response.text})
        
#         # Add the user's message to history
#         history.append({"role": "user", "parts": message})
        
#         # Start or continue chat with history
#         chat = model.start_chat(history=history)
#         response = chat.send_message(message)
        
#         # Add the response to history
#         history.append({"role": "model", "parts": response.text})
#         return response.text, history
#     except Exception as e:
#         print(f"Error in send_message: {e}")
#         return "I apologize, but I encountered an error processing your request.", history

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST', 'OPTIONS'])
# def chat():
#     if request.method == 'OPTIONS':
#         return '', 204  # Handle preflight requests for CORS

#     if request.method != 'POST':
#         return jsonify({'error': 'Method Not Allowed'}), 405

#     try:
#         user_message = request.json.get('message')
#         history = request.json.get('history', [])

#         if not user_message:
#             return jsonify({'error': 'No message provided'}), 400

#         response, history = send_message(user_message, history)
#         return jsonify({'message': response, "history": history})
#     except Exception as e:
#         print(f"Error in chat endpoint: {e}")
#         return jsonify({'error': 'Internal server error'}), 500

# def sanitize_text_for_speech(text):
#     # Remove special characters and formatting
#     text = re.sub(r'[*_#`~>-]|\[|\]|\(|\)|\{|\}|\\|\/|\||\+|@|&|%|\$|^|!|"|\'|;|:|,|\.', '', text)
#     # Remove multiple spaces
#     text = re.sub(r'\s+', ' ', text)
#     return text.strip()

# @app.route('/process-text', methods=['POST', 'OPTIONS'])
# def process_text():
#     if request.method == 'OPTIONS':
#         return '', 204  # Handle preflight requests for CORS

#     if request.method != 'POST':
#         return jsonify({"error": "Method Not Allowed"}), 405

#     try:
#         user_data = request.get_json()
#         user_text = user_data.get('text', '')

#         if not user_text:
#             return jsonify({"error": "No text provided"}), 400

#         # Sanitize text before sending to ElevenLabs
#         sanitized_text = sanitize_text_for_speech(user_text)

#         # Generate audio from text using ElevenLabs
#         audio_generator = client.generate(
#             text=sanitized_text,
#             voice="Brian",
#             model="eleven_monolingual_v1"
#         )
        
#         # Store audio in a BytesIO buffer
#         audio_buffer = BytesIO()
#         for chunk in audio_generator:
#             audio_buffer.write(chunk)

#         # Rewind the buffer to the beginning
#         audio_buffer.seek(0)

#         # Send the audio as a file-like response
#         return send_file(
#             audio_buffer,
#             mimetype='audio/mpeg',
#             as_attachment=False,
#             download_name="response.mp3"
#         )
#     except Exception as e:
#         print(f"Error in process-text endpoint: {e}")
#         return jsonify({"error": "Error generating audio"}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import google.generativeai as genai
from io import BytesIO
import requests
import os
import re
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load API keys from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
sarvam_api_key = os.getenv("SARVAM_API_KEY")

# Load Karan's profile
try:
    with open("karan_info.json", "r") as file:
        karan_data = json.load(file)

    if not google_api_key or not sarvam_api_key:
        raise ValueError("API keys missing")

    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

except Exception as e:
    print(f"Error loading configuration: {e}")
    raise

PERSONALITY_PROMPT = f"""You are Karan Sankhe, a passionate computer engineer and AI enthusiast. Here is your detailed background:

Personal Information:
- Name: {karan_data['personal_info']['name']}
- Education: {karan_data['personal_info']['education']}
- Current Status: {karan_data['personal_info']['current_status']}

Life Story:
{karan_data['life_story']}

Your Superpower:
{karan_data['superpower']}

Areas for Growth:
{chr(10).join(f"- {area}" for area in karan_data['growth_areas'])}

Common Misconceptions:
{chr(10).join(f"- {misconception}" for misconception in karan_data['misconceptions'])}

How You Push Boundaries:
{chr(10).join(f"- {boundary}" for boundary in karan_data['boundaries'])}

Final Thoughts:
{karan_data['final_thoughts']}

When responding to questions:
1. Keep responses personal and authentic to your experiences
2. Maintain an optimistic and enthusiastic tone
3. Focus on your technical expertise and leadership experience
4. Share specific examples from your projects and achievements
5. Be honest about your growth areas and aspirations
6. Keep responses concise and engaging
7. Use a conversational but professional tone
8. Emphasize your passion for AI and problem-solving
9. Highlight your entrepreneurial mindset
10. Show your commitment to continuous learning
11. Answer below 500 characters concise answers.
12. Answer like answering as karan Sankhe.
"""

def send_message(message, history):
    try:
        if not history:
            history = [{"role": "user", "parts": PERSONALITY_PROMPT}]
            chat = model.start_chat(history=history)
            response = chat.send_message("I understand my role...")
            history.append({"role": "model", "parts": response.text})
        history.append({"role": "user", "parts": message})
        chat = model.start_chat(history=history)
        response = chat.send_message(message)
        short_response = response.text[:500]  # Truncate to 500 characters
        history.append({"role": "model", "parts": short_response})
        return short_response, history
    except Exception as e:
        print(f"Error in send_message: {e}")
        return "Error processing request.", history

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        user_message = request.json.get('message')
        history = request.json.get('history', [])
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        response, history = send_message(user_message, history)
        return jsonify({'message': response, 'history': history})
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

def sanitize_text_for_speech(text):
    text = re.sub(r'[*_#`~>\[\]{}\\|+@&%$^!\"\'`;:,.]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

@app.route('/process-text', methods=['POST', 'OPTIONS'])
def process_text():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        user_data = request.get_json()
        user_text = user_data.get('text', '')
        lang = user_data.get('language_code', 'en')

        if not user_text:
            return jsonify({"error": "No text provided"}), 400

        sanitized_text = sanitize_text_for_speech(user_text)

        lang_map = {
            "en": "en-IN",
            "hi": "hi-IN",
            
        }
        target_language = lang_map.get(lang, "en-IN")

        headers = {
            "API-Subscription-Key": sarvam_api_key
        }

        payload = {
            "inputs": [sanitized_text],
            "target_language_code": target_language,
            "speaker": "meera",
            "pitch": 0,
            "pace": 1.5,
            "loudness": 1.2,
            "speech_sample_rate": 8000,
            "enable_preprocessing": True,
            "model": "bulbul:v1"
        }

        response = requests.post("https://api.sarvam.ai/text-to-speech", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if "audios" not in data or not data["audios"]:
            return jsonify({"error": "No audio data returned"}), 500

        base64_audio = data["audios"][0]
        wav_data = base64.b64decode(base64_audio)
        audio_io = BytesIO(wav_data)
        audio_io.seek(0)

        return send_file(
            audio_io,
            mimetype='audio/wav',
            as_attachment=False,
            download_name='response_audio.wav'
        )

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API Request Error: {str(e)}"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON from Sarvam API."}), 500
    except Exception as e:
        print(f"TTS error: {e}")
        return jsonify({"error": "Unexpected server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)



