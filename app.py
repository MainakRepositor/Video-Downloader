import streamlit as st
import yt_dlp
import os

# Ensure 'videos/' directory exists
if not os.path.exists('videos'):
    os.makedirs('videos')

# Function to download video using yt-dlp
def download_video(url):
    ydl_opts = {
        'format': 'mp4[height<=720]',  # Limit to 720p
        'outtmpl': 'videos/video.mp4',  # Output file location
        'noplaylist': True  # Avoid downloading playlists
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            return 'videos/video.mp4'
    except Exception as e:
        st.error(f"Error downloading video: {e}")
        return None

# Streamlit Interface
st.title("Free Youtube Video Downloader")

# Input box for URL
url = st.text_input("Enter the Youtube video URL")

# Check if URL is entered
if url:
    try:
        st.sidebar.write("Video Preview:")
        st.sidebar.video(url)  # Display the video in the sidebar as a preview
    except Exception as e:
        st.sidebar.error(f"Unable to load preview: {e}")

    # Download button logic
    if st.button("Download Video"):
        st.info("Fetching video...")
        
        # Use yt-dlp for all platforms
        file_path = download_video(url)
        
        # If file is downloaded successfully
        if file_path and os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.success("Video downloaded successfully!")
                st.download_button("Download", file, file_name="video.mp4", mime="video/mp4")
        else:
            st.error("Failed to download the video.")
