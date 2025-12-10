
import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import os
import uuid

st.title("🎵 YouTube MP3 Player")
st.write("Paste a YouTube Video URL to extract and play its audio.")

url = st.text_input("YouTube URL")

if url:
    try:
        yt = YouTube(url)
        st.write(f"**Title:** {yt.title}")
        st.write("Downloading audio...")

        # Download audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        temp_file = audio_stream.download(filename=f"{uuid.uuid4()}.mp4")

        # Convert to MP3
        mp3_filename = temp_file.replace(".mp4", ".mp3")
        sound = AudioSegment.from_file(temp_file)
        sound.export(mp3_filename, format="mp3")

        # Load MP3 into player
        audio_bytes = open(mp3_filename, "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

        # Cleanup
        os.remove(temp_file)
        os.remove(mp3_filename)

    except Exception as e:
        st.error(f"Error: {e}")
