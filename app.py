import streamlit as st

from utils.pdf_reader import read_pdf
from utils.extractor import extract_info
from utils.qa import answer_question
from utils.summarizer import generate_summary
from utils.comparator import compare_documents

st.set_page_config(page_title="DocInsight AI")


st.title("📄 DocInsight AI")
st.markdown("""
### AI-Powered Document Analysis Platform

Features:
- Document Upload
- Smart Summarization
- Information Extraction
- Document Q&A
- Document Comparison
""")

tab1, tab2 = st.tabs(
    ["Document Analysis", "Compare Documents"]
)

# -------------------------------------------------
# TAB 1
# -------------------------------------------------

with tab1:

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        text = read_pdf(uploaded_file)

        st.success("PDF Loaded Successfully")

        st.subheader("Document Summary")

        if st.button("Generate Summary"):

            summary = generate_summary(text)

            st.write(summary)

        st.subheader("Extracted Information")

        information = extract_info(text)

        st.json(information)

        st.subheader("Ask Questions")

        question = st.text_input(
            "Enter Question"
        )

        if question:

            answer = answer_question(
                text,
                question
            )

            st.write(answer)

# -------------------------------------------------
# TAB 2
# -------------------------------------------------

with tab2:

    file1 = st.file_uploader(
        "Upload First PDF",
        type=["pdf"],
        key="pdf1"
    )

    file2 = st.file_uploader(
        "Upload Second PDF",
        type=["pdf"],
        key="pdf2"
    )

    if file1 and file2:

        text1 = read_pdf(file1)
        text2 = read_pdf(file2)

        result = compare_documents(
            text1,
            text2
        )

        st.subheader("Comparison Result")

        st.json(result)
