import streamlit as st
import requests

st.markdown("""
    <style>
    .big-font {
        font-size:18px !important;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        font-size: 16px !important;
        padding: 10px;
    }
    .stTextArea > div > textarea {
        font-size: 16px !important;
        padding: 10px;
    }
    .stButton > button {
        font-size: 20px !important;
        padding: 10px 20px;
    }
    .stMarkdown {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">PDF Chatbot with Llama 3.1</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    uploaded_file.seek(0)  # Reset file pointer
    files = {'file': (uploaded_file.name, uploaded_file, 'application/pdf')}
    with st.spinner('Uploading and extracting text...'):
        res = requests.post('http://127.0.0.1:5000/upload', files=files)
    if res.status_code == 200:
        data = res.json()
        context = data['text']
        st.success(f"Uploaded: {data['filename']}")
        st.session_state['context'] = context
    else:
        try:
            error_msg = res.json().get('error', 'Upload failed')
        except Exception:
            error_msg = f"Upload failed. Server response: {res.text}"
        st.error(error_msg)

if 'context' in st.session_state:
    st.markdown('<div class="big-font">Ask a question about the PDF:</div>', unsafe_allow_html=True)
    question = st.text_input("Your Question", key="question_input")
    if st.button("Ask", key="ask_button") and question:
        with st.spinner('Getting answer from Llama 3.1...'):
            res = requests.post('http://127.0.0.1:5000/ask', json={
                'question': question,
                'context': st.session_state['context']
            })
        if res.status_code == 200:
            answer = res.json()['answer']
            st.markdown(f"<div class='big-font' style='color:#1a73e8;'>Bot:</div> <div style='font-size:16px'>{answer}</div>", unsafe_allow_html=True)
        else:
            st.error(res.json().get('error', 'Failed to get answer'))
