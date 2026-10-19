import streamlit as st
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
        
        st.subheader("🖼️ Thumbnail Preview:")
        st.image(thumbnail_url, use_container_width=True)
        
        st.write("---")
        st.success("🎉 Thumbnail Grabbed Successfully!")
        
        # HTML dynamic link to directly trigger download window bypassing cloud block
        download_html = f'''
            <a href="{thumbnail_url}" target="_blank" download="yt_thumbnail.jpg" style="
                display: inline-block;
                padding: 0.5em 1em;
                color: white;
                background-color: #FF4B4B;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                text-align: center;
                width: 100%;
            ">📥 Click Here to Open & Save Image</a>
        '''
        st.markdown(download_html, unsafe_allow_html=True)
        
    else:
        st.error("Invalid Link! Please enter a valid YouTube video URL.")

st.write("---")
st.caption("Developed by Keshav Thathai | Need custom video utility tools for your brand? Contact me: thataikeshav873@gmail.com")

