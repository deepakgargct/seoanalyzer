# app.py

import streamlit as st
import tempfile
import os
from seoanalyzer import analyze

st.set_page_config(page_title="SEO Analyzer", layout="wide")
st.title("🔍 Python SEO Analyzer")

st.markdown("""
This app uses the [`python-seo-analyzer`](https://github.com/sethblack/python-seo-analyzer) library to analyze a webpage or local HTML file for basic SEO issues.
""")

analysis_type = st.radio("Choose analysis type:", ["Analyze a URL", "Analyze an uploaded HTML file"])

if analysis_type == "Analyze a URL":
    url = st.text_input("Enter URL to analyze:")
    if st.button("Run Analysis") and url:
        with st.spinner("Analyzing URL..."):
            result = analyze(url=url, options={"crawl": False})
        st.success("Analysis complete!")
        st.json(result)

else:
    uploaded_file = st.file_uploader("Upload an HTML file", type=["html", "htm"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        if st.button("Run Analysis"):
            with st.spinner("Analyzing file..."):
                result = analyze(url=tmp_path, options={"crawl": False})
            st.success("Analysis complete!")
            st.json(result)

        os.remove(tmp_path)
