import streamlit as st
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

st.set_page_config(page_title="Sosovideo", layout="centered")

st.title("🎬 Welcome to Sosovideo!")
st.write("This is your AI-powered video generation app. Just enter a script, and let the AI do the magic!")

script = st.text_area("Enter your video script here:")

if st.button("Generate Video"):
    if script.strip() == "":
        st.warning("Please enter a script.")
    else:
        with st.spinner("Generating video..."):

            # Step 1: Convert text to speech
            audio_filename = f"{uuid.uuid4().hex}_audio.mp3"
            tts = gTTS(text=script, lang='en')
            tts.save(audio_filename)

            # Step 2: Create an image with the script text
            img_filename = f"{uuid.uuid4().hex}_image.png"
            img = Image.new('RGB', (1280, 720), color=(10, 10, 30))
            draw = ImageDraw.Draw(img)

            font = ImageFont.truetype("arial.ttf", 48) if os.path.exists("arial.ttf") else ImageFont.load_default()

            # Wrap text
            max_width = 50
            lines = []
            words = script.split()
            line = ""
            for word in words:
                if len(line + " " + word) < max_width:
                    line += " " + word
                else:
                    lines.append(line.strip())
                    line = word
            lines.append(line.strip())

            y_text = 250
            for line in lines:
                width, height = draw.textsize(line, font=font)
                draw.text(((1280 - width) / 2, y_text), line, font=font, fill=(255, 255, 255))
                y_text += height + 10

            img.save(img_filename)

            # Step 3: Create video from image and audio
            clip = ImageClip(img_filename).set_duration(AudioFileClip(audio_filename).duration)
            clip = clip.set_audio(AudioFileClip(audio_filename))
            video_filename = f"{uuid.uuid4().hex}_video.mp4"
            clip.write_videofile(video_filename, fps=24)

            # Step 4: Show video and provide download
            st.success("✅ Video generated successfully!")
            st.video(video_filename)

            with open(video_filename, "rb") as f:
                st.download_button("Download Video", f, file_name="sosovideo.mp4", mime="video/mp4")

            # Cleanup
            os.remove(audio_filename)
            os.remove(img_filename)
            os.remove(video_filename)
