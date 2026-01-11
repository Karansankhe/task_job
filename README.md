aran Sankhe's AI Assistant
A personal AI chatbot powered by Google Gemini (Generative AI) for text-based conversations and ElevenLabs for high-quality text-to-speech responses.

🚀 Features
✅ Conversational AI: Uses Google Gemini to generate responses in a natural and engaging way.
✅ Text-to-Speech (TTS): Converts chatbot responses into high-quality speech using ElevenLabs.
✅ Speech Recognition: Uses the browser's built-in speech recognition to convert spoken words into text.
✅ Web-based UI: A simple and clean front-end built with HTML, CSS, and JavaScript.
✅ Flask Backend: Serves API endpoints for chat and text-to-speech processing.
✅ CORS Enabled: Allows cross-origin requests for frontend-backend communication.

🛠️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/Karansankhe/task_job.git
cd .\Personal-Voice-Assistant  

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate 
venv\Scripts\activate    

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables
Create a .env file in the project root and add your API keys:
GOOGLE_API_KEY=your_google_gemini_api_key
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key

5️⃣ Run the Flask App
python app.py
The server will start at http://127.0.0.1:5000/

🎤 Usage
1️⃣ Open index.html in a browser.
2️⃣ Click the microphone button to start speaking.
3️⃣ The chatbot will process your speech, generate a response, and speak it back using ElevenLabs.
