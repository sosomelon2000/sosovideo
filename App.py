# import streamlit as st

# File: App.py

import streamlit as st
from PIL import Image
from gtts import gTTS
import os
from moviepy.editor import *

st.title("🎬 Sosovideo - AI Script to Video")

# Step 1: Take Script Input
script = st.text_area("Enter your video script", height=200)

# Step 2: Generate Voice from Script
if st.button("Generate Video"):
    if script.strip() == "":
        st.warning("Please enter a script.")
    else:
        # Save audio
        tts = gTTS(script)
        audio_path = "voice.mp3"
        tts.save(audio_path)

        # Create a sample image (you can later replace this with AI-generated image)
        img = Image.new('RGB', (1280, 720), color = (73, 109, 137))
        img_path = "scene.jpg"
        img.save(img_path)

        # Combine image and audio into video
        image_clip = ImageClip(img_path).set_duration(10)
        audio_clip = AudioFileClip(audio_path).subclip(0, 10)
        video = image_clip.set_audio(audio_clip)
        video_path = "final_video.mp4"
        video.write_videofile(video_path, fps=24)

        # Show video
        st.video(video_path)
        st.success("🎉 Video generated successfully!")
st.set_page_config(page_title="SosoVideo AI", layout="centered")

st.title("🎬 Welcome to SosoVideo AI!")
st.write("Create AI-generated videos from your scripts in just one click.")

script = st.text_area("✍️ Enter your video script here:", height=200)

if st.button("🎥 Generate Video"):
    if script.strip() == "":
        st.warning("Please enter a script to generate the video.")
    else:
        with st.spinner("Generating video..."):
            # Simulated video generation
            st.success("✅ Video generated successfully!")
            st.video("https://samplelib.com/lib/preview/mp4/sample-5s.mp4")  # Placeholder

st.info("Note: This is a prototype version of the SosoVideo AI app.")

