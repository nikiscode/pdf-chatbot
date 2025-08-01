# PDF Chatbot with Llama 3.1 and Ollama

This project is a PDF chatbot that allows users to upload a PDF, ask questions about its content, and get answers using the Llama 3.1 model via Ollama. It consists of a Flask backend API and a Streamlit frontend UI.

## Features
- Upload a PDF and extract its text
- Ask questions about the PDF content
- Answers are generated using the Llama 3.1 model (via Ollama)
- Simple web interface with Streamlit

---

## Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running with the `llama3.1:latest` model pulled
- pip (Python package manager)

---

## Setup Instructions

### 1. Clone or Download the Repository
```
git clone <your-repo-url>
cd pdf-chatbot
```

### 2. Install Python Dependencies
It is recommended to use a virtual environment:
```sh
for windows
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
pip install -r requirements.txt  
python.exe -m pip install --upgrade pip   

```

### 3. Start Ollama and Pull the Model
Make sure Ollama is running and the Llama 3.1 model is available:
```sh
ollama serve
ollama pull llama3.1:latest
```

### 4. Start the Flask Backend
```sh
python pdf_api.py
```
The backend will run on [http://localhost:5000](http://localhost:5000)

### 5. Start the Streamlit Frontend
In a new terminal (with the virtual environment activated):
```sh
streamlit run pdf_chatbot_ui.py
```
The frontend will run on [http://localhost:8501](http://localhost:8501)

---

## Usage
1. Open [http://localhost:8501](http://localhost:8501) in your browser.
2. Upload a PDF file using the interface.
3. Ask questions about the PDF content in the chat box.
4. The bot will answer using the Llama 3.1 model.

---

## Troubleshooting
- **Flask or Streamlit not running?** Make sure you are in the correct directory and your virtual environment is activated.
- **Ollama errors?** Ensure Ollama is running and the model is pulled.
- **File upload issues?** Make sure the `uploads/` directory exists and is writable, or let the app create it automatically.
- **Port conflicts?** Change the port in `pdf_api.py` or when running Streamlit if needed.

---

## Running on a Different System
1. Copy the project folder to the new system.
2. Install Python 3.8+ and pip if not already installed.
3. Follow the setup instructions above (create virtual environment, install requirements, start Ollama, backend, and frontend).
4. Make sure ports 5000 (Flask) and 8501 (Streamlit) are open and not blocked by a firewall.

---

## License
MIT License

---

## Credits
- [Ollama](https://ollama.com/)
- [Llama 3.1 Model](https://ollama.com/library/llama3)
- [Streamlit](https://streamlit.io/)
- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
