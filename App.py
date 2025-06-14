# import streamlit as st

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

