import streamlit as st
import PyPDF2
from llm_response import generate_answer

# 💡 Set page layout and title
st.set_page_config(page_title="StudyMate - AI Study Helper", page_icon="📚", layout="wide")

# 🎨 Custom background color
def set_bg_color():
    st.markdown("""
        <style>
            body {
                background-color: #f5f7fa;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 0.5em 1.2em;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #45a049;
                color: white;
            }
            .stTextInput>div>div>input {
                border-radius: 8px;
            }
            .stTextArea>div>textarea {
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

set_bg_color()

# 🏷️ Title and intro
st.title("📘 StudyMate: Your AI-Powered Study Partner")
st.markdown("""
Welcome to **StudyMate**, your intelligent study assistant!  
Just upload your **course notes or textbooks (PDF)** and **ask any question** from them.  
You'll get accurate, well-explained answers instantly! 🚀
""")

# 📂 Sidebar (optional)
with st.sidebar:
    st.header("📂 Navigation")
    st.markdown("📝 **Steps:**")
    st.markdown("1. Upload your PDF")
    st.markdown("2. Type your question")
    st.markdown("3. Click 'Generate Answer'")
    st.markdown("4. See your AI-generated explanation 💬")
    st.markdown("---")
    st.info("Built with 💙 using Hugging Face & Streamlit")

# 📤 Upload PDF
pdf_file = st.file_uploader("📄 Upload your PDF notes or textbook", type=["pdf"])

# 🧠 Ask a Question
question = st.text_area("❓ Ask your question based on the PDF:", height=100, placeholder="e.g., What are the key differences between AC and DC?")

# 📖 Extract PDF text
def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# 🧠 Answer Generation
if st.button("🧠 Generate Answer"):
    if pdf_file is not None and question.strip() != "":
        with st.spinner("🔎 Analyzing PDF and generating answer..."):
            content = extract_pdf_text(pdf_file)
            answer = generate_answer(content, question)
            st.success("✅ Answer generated:")
            st.markdown(f"**Answer:**\n\n{answer}")
    else:
        st.warning("Please upload a PDF and enter a valid question.")

# 📌 Footer
st.markdown("---")
#st.markdown("<center>Made with ❤️ by Mallika • MSME Hackathon 5.0 • 2025</center>", unsafe_allow_html=True)
