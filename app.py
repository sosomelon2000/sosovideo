
import streamlit as st

st.set_page_config(page_title="Sosovideo", layout="wide")

st.title("🎬 Welcome to Sosovideo!")
st.write("This is your AI-powered video generation app. Just enter a script, and let the AI do the magic!")

# Input area for script
script = st.text_area("Enter your video script here:")

if st.button("Generate Video"):
    if script.strip() == "":
        st.warning("Please enter a script to generate the video.")
    else:
        st.success("Video generation started! (This is a placeholder)")
        st.info("🚧 The video generation feature is under development.")
