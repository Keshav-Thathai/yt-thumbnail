import streamlit as st
import requests
import re

st.set_page_config(page_title="YT Thumbnail Downloader", page_icon="📸")
st.title("📸 YouTube Thumbnail Grabber & Downloader")
st.write("Paste any YouTube video link and download the HD Thumbnail instantly!")

st.write("---")

video_url = st.text_input("Enter YouTube Video Link:", placeholder="https://youtube.com...")

st.write("---")

if video_url:
    video_id = None
    
    try:
        regex = r"(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|shorts\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})"
        match = re.search(regex, video_url)
        if match:
            video_id = match.group(1)
    except Exception:
        video_id = None

    if video_id:
        thumbnail_url = f"https://youtube.com{video_id}/maxresdefault.jpg"
        
        try:
            response = requests.get(thumbnail_url)
            
            if response.status_code != 200:
                thumbnail_url = f"https://youtube.com{video_id}/hqdefault.jpg"
                response = requests.get(thumbnail_url)
                
            if response.status_code == 200:
                img_bytes = response.content
                
                st.subheader("🖼️ Thumbnail Preview:")
                st.image(thumbnail_url, use_container_width=True)
                
                st.write("---")
                st.success("🎉 Download Ready! Click the button below to save.")
                st.download_button(
                    label="📥 Click Here to Download Image",
                    data=img_bytes,
                    file_name=f"yt_thumbnail_{video_id}.jpg",
                    mime="image/jpeg"
                )
            else:
                st.error("High-Definition thumbnail is not available for this video link.")
        except Exception:
            st.error("Network error occurred while fetching the image database.")
    else:
        st.error("Invalid Link! Please enter a valid YouTube video URL.")

st.write("---")
st.caption("Developed by Keshav Thathai | Need custom video utility tools for your brand? Contact me: thataikeshav873@gmail.com")





