import streamlit as st
from urllib.parse import urlparse, parse_qs
import requests

st.set_page_config(page_title="YT Thumbnail Downloader", page_icon="📸")
st.title("📸 YouTube Thumbnail Grabber & Downloader")
st.write("Paste any YouTube video link and download the HD Thumbnail instantly!")

st.write("---")

video_url = st.text_input("Enter YouTube Video Link:", placeholder="https://youtube.com...")

st.write("---")

if video_url:
    video_id = None
    
    try:
        parsed_url = urlparse(video_url)
        if parsed_url.hostname in ('://youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                video_id = parse_qs(parsed_url.query).get('v', [None])[0]
            elif parsed_url.path.startswith(('/embed/', '/v/', '/shorts/')):
                video_id = parsed_url.path.split('/')[2]
        elif parsed_url.hostname == 'youtu.be':
            video_id = parsed_url.path[1:]
    except Exception:
        video_id = None

    if video_id:
        thumbnail_url = f"https://youtube.com{video_id}/maxresdefault.jpg"
        
        st.subheader("🖼️ Thumbnail Preview:")
        st.image(thumbnail_url, use_container_width=True)
        
        st.write("---")
        
        try:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                img_bytes = response.content
                
                st.success("🎉 Download Ready! Click the button below to save.")
                st.download_button(
                    label="📥 Click Here to Download Image",
                    data=img_bytes,
                    file_name=f"yt_thumbnail_{video_id}.jpg",
                    mime="image/jpeg"
                )
            else:
                st.error("High-Definition thumbnail is not available for this video.")
        except Exception as e:
            st.error("Network error occurred while fetching the image.")
    else:
        st.error("Invalid Link! Please enter a valid YouTube video URL.")

st.write("---")
st.caption("Developed by Keshav  Thathai| Need custom video utility tools for your brand? Contact me: thataikeshav873@gmail.com")


