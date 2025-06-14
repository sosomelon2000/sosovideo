import streamlit as st
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
import uuid
import textwrap

st.set_page_config(page_title="Sosovideo", layout="centered")
st.title("🎬 Sosovideo: Script to AI Video Generator")

script = st.text_area("Enter your script below:", height=200)

if st.button("Generate Video"):
    if not script.strip():
        st.warning("Please enter a script.")
    else:
        with st.spinner("Generating video..."):

            # 1. Convert text to audio
            audio_filename = f"{uuid.uuid4()}.mp3"
            tts = gTTS(text=script, lang='en')
            tts.save(audio_filename)

            # 2. Create image with subtitle text
            W, H = 720, 480
            img = Image.new("RGB", (W, H), color=(0, 0, 0))
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()

            # Wrap text into multiple lines
            lines = textwrap.wrap(script, width=40)
            y_text = 150
            for line in lines:
                w, h = draw.textsize(line, font=font)
                draw.text(((W - w) / 2, y_text), line, font=font, fill="white")
                y_text += h + 10

            image_filename = f"{uuid.uuid4()}.png"
            img.save(image_filename)

            # 3. Combine image and audio into a video
            audio_clip = AudioFileClip(audio_filename)
            image_clip = ImageClip(image_filename).set_duration(audio_clip.duration)
            video = image_clip.set_audio(audio_clip)

            video_filename = f"{uuid.uuid4()}.mp4"
            video.write_videofile(video_filename, fps=24, audio_codec="aac")

            # 4. Display video and download option
            st.success("✅ Video generated successfully!")
            st.video(video_filename)
            with open(video_filename, "rb") as f:
                st.download_button("📥 Download Video", f, file_name="sosovideo.mp4")

            # 5. Cleanup
            os.remove(audio_filename)
            os.remove(image_filename)
            os.remove(video_filename)
