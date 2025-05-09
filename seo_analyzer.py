# streamlit_seo_analyzer.py

import streamlit as st
import tempfile
import os
from seoanalyzer import analyze

st.set_page_config(page_title="SEO Analyzer", layout="wide")
st.title("🔍 Python SEO Analyzer")

st.markdown("""
This app uses the [`python-seo-analyzer`](https://github.com/sethblack/python-seo-analyzer) library to analyze a webpage or local HTML file for basic SEO characteristics.
""")

analysis_target = st.radio("Choose Analysis Type", ["URL", "Local HTML File"])

# URL-based analysis
if analysis_target == "URL":
    url = st.text_input("Enter URL to analyze:", placeholder="https://example.com")
    if st.button("Analyze URL") and url:
        with st.spinner("Analyzing..."):
            result = analyze(url=url, options={"crawl": False})
        st.success("Analysis complete!")
        st.json(result)

# File-based analysis
else:
    uploaded_file = st.file_uploader("Upload an HTML file", type=["html", "htm"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        if st.button("Analyze File"):
            with st.spinner("Analyzing..."):
                result = analyze(url=temp_file_path, options={"crawl": False})
            st.success("Analysis complete!")
            st.json(result)

        # Clean up
        os.remove(temp_file_path)
