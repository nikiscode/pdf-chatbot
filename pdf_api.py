from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import PyPDF2
import requests

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "llama3.1:latest"


def extract_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    text = extract_pdf_text(filepath)
    return jsonify({'filename': filename, 'text': text})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    if not question or not context:
        return jsonify({'error': 'Missing question or context'}), 400
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    answer = response.json().get("response", "No answer from model.")
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
