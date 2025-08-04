# Jarvis---Your-Python-Voice-Assistant
🎙️ Jarvis is a Python-based voice assistant that listens to your commands and performs tasks like **searching Google/Wikipedia, playing YouTube songs, opening apps, and solving basic math** — all through natural speech. Just say **"Jarvis"** to activate it and let the automation begin! Built using **SpeechRecognition, pyttsx3, Wikipedia, and PyWhatKit.**

---

**🎯 Features**

- 🎙️ Voice recognition using `speech_recognition`
- 🗣️ Text-to-speech responses via `pyttsx3`
- 🔍 Wikipedia and Google search
- 🎵 Play YouTube videos using voice commands
- 🧮 Perform basic calculations
- 🖥️ Open popular apps (Chrome, Notepad, Calculator, VS Code)
- 🧠 Wake word detection ("Jarvis")

---
 **🚀 Getting Started**

 **✅ Prerequisites**

Ensure you have Python installed. Then install the required packages:

```bash
pip install SpeechRecognition pyttsx3 wikipedia pywhatkit
For Windows users, also install PyAudio:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
🔧 How to Run
Clone the repository or copy the script.

Save the code in a file named jarvis.py.

Open terminal and run:

bash
Copy
Edit
python jarvis.py
Say "Jarvis" to activate the assistant, then give your command.

🧪 Example Commands
"Jarvis, who is Narendra Modi" – searches and reads a Wikipedia summary.

"Jarvis, play Kesariya on YouTube" – opens YouTube and plays the song.

"Jarvis, search for AI news" – performs a Google search.

"Jarvis, calculate 10 plus 5" – speaks out the result.

"Jarvis, open Chrome" – launches Google Chrome (if installed).

"Jarvis, exit" – exits the assistant.


🛠️ Code Structure
speak(text) – Converts text to voice.

calculate_expression(text) – Evaluates spoken arithmetic expressions.

processCommand(command) – Parses and executes the user’s command.

Main loop – Listens for wake word, then processes next command.

💡 Notes
Make sure your microphone is enabled and working.

Background noise can affect recognition accuracy. Use a quiet environment.

Supports only English voice commands.

📄 License
This project is licensed under the MIT License.

🙌 Credits
SpeechRecognition

Pyttsx3

Wikipedia

PyWhatKit

PyWhatKit
