import streamlit as st
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

st.title("🎬 Sosovideo: Script to AI Video Generator")

script = st.text_area("Enter your script here", height=200)

if st.button("Generate Video"):
    if not script.strip():
        st.warning("Please enter a script first.")
    else:
        with st.spinner("Generating video..."):
            # Generate audio from script
            audio_filename = f"{uuid.uuid4()}.mp3"
            tts = gTTS(text=script, lang='en')
            tts.save(audio_filename)

            # Create a background image
            W, H = 720, 480
            background = Image.new("RGB", (W, H), (0, 0, 0))  # black background
            draw = ImageDraw.Draw(background)

            # Use default font
            font = ImageFont.load_default()

            # Wrap text
            import textwrap
            lines = textwrap.wrap(script, width=40)
            y_text = 150
            for line in lines:
                w, h = draw.textsize(line, font=font)
                draw.text(((W - w) / 2, y_text), line, font=font, fill="white")
                y_text += h + 5

            img_path = f"{uuid.uuid4()}.png"
            background.save(img_path)

            # Create video
            audio_clip = AudioFileClip(audio_filename)
            image_clip = ImageClip(img_path).set_duration(audio_clip.duration)
            video = image_clip.set_audio(audio_clip)

            output_path = f"{uuid.uuid4()}.mp4"
            video.write_videofile(output_path, fps=24)

            st.success("✅ Video generated!")
            st.video(output_path)

            with open(output_path, "rb") as f:
                st.download_button("📥 Download Video", f, file_name="sosovideo.mp4")

            # Clean up
            os.remove(img_path)
            os.remove(audio_filename)
            os.remove(output_path)
