import streamlit as st
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os, uuid, textwrap

st.set_page_config(page_title="Sosovideo", layout="centered")
st.title("🎬 Sosovideo: Script to AI Video Generator")
script = st.text_area("Enter your script below:", height=200)

if st.button("Generate Video"):
    if not script.strip():
        st.warning("Please enter a script.")
    else:
        with st.spinner("Generating video…"):
            # 1. Create audio
            audio_file = f"{uuid.uuid4()}.mp3"
            gTTS(text=script, lang='en').save(audio_file)
            
            # 2. Create image
            W, H = 720, 480
            bg = Image.new("RGB", (W, H), (0, 0, 0))
            draw = ImageDraw.Draw(bg)
            font = ImageFont.load_default()
            
            lines = textwrap.wrap(script, width=40)
            y = 150
            for line in lines:
                w, h = draw.textsize(line, font=font)
                draw.text(((W-w)/2, y), line, font=font, fill="white")
                y += h + 5

            img_file = f"{uuid.uuid4()}.png"
            bg.save(img_file)

            # 3. Combine image + audio into video
            audio_clip = AudioFileClip(audio_file)
            img_clip = ImageClip(img_file).set_duration(audio_clip.duration)
            video = img_clip.set_audio(audio_clip)
            video_file = f"{uuid.uuid4()}.mp4"
            video.write_videofile(video_file, fps=24, audio_codec="aac")

            # 4. Display & download
            st.success("✅ Video generated successfully!")
            st.video(video_file)
            with open(video_file, "rb") as file:
                st.download_button("Download Video", file, file_name="sosovideo.mp4")

            # 5. Cleanup
            os.remove(audio_file)
            os.remove(img_file)
            os.remove(video_file)
