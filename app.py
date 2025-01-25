import streamlit as st
import os

# Set the title of the web app
st.title("CodeQuest: A Hackathon for young tinkerers")

# Load HTML content
def load_html(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

# Display the HTML content
html_content_en = load_html('index.html')
html_content_de = load_html('index_de.html')

# Add a radio button for language selection
language = st.radio("Select Language", ('English', 'Deutsch'))

if language == 'English':
    st.markdown(html_content_en, unsafe_allow_html=True)
else:
    st.markdown(html_content_de, unsafe_allow_html=True)

# Serve static files
st.markdown("""
<style>
    @import url('styles.css');
</style>
""", unsafe_allow_html=True)