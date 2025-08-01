import sys
import PyPDF2
import requests

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "llama3.1:latest"


def extract_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def ask_ollama(question, context, model=OLLAMA_MODEL):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    response.raise_for_status()
    return response.json().get("response", "No answer from model.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_chatbot.py <pdf_path>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    print(f"Extracting text from {pdf_path}...")
    context = extract_pdf_text(pdf_path)
    print("PDF loaded. You can now ask questions about its content. Type 'exit' to quit.")
    while True:
        question = input("You: ")
        if question.lower() in ("exit", "quit"): 
            break
        answer = ask_ollama(question, context)
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
