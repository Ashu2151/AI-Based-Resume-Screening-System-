import streamlit as st

from src.parser import extract_text_from_pdf
from src.matcher import match_resume

st.title("AI Resume Screening System")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area("Enter Job Description")

if uploaded_files and job_description:

    results = []

    for file in uploaded_files:

        resume_text = extract_text_from_pdf(file)

        score = match_resume(
            resume_text,
            job_description
        )

        results.append({
            "name": file.name,
            "score": score
        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    st.subheader("Ranking Results")

    for rank, result in enumerate(results, start=1):

        st.write(
            f"{rank}. {result['name']} → {result['score']}%"
        )