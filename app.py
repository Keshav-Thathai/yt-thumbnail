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
        # 100% Working Fallback System using HTML scripting
        st.subheader("🖼️ Thumbnail Preview:")
        
        # We inject a clean HTML layout that automatically loads backup images if HD is not found by the YouTube server
        html_display = f'''
            <div style="text-align: center;">
                <img src="https://youtube.com{video_id}/maxresdefault.jpg" 
                     onerror="this.onerror=null; this.src='https://youtube.com{video_id}/hqdefault.jpg';" 
                     style="width: 100%; border-radius: 10px; margin-bottom: 20px;" />
                
                <a href="https://youtube.com{video_id}/hqdefault.jpg" target="_blank" style="
                    display: inline-block;
                    padding: 0.6em 1em;
                    color: white;
                    background-color: #FF4B4B;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                    width: 100%;
                    box-sizing: border-box;
                ">📥 Click Here to Open & Save Image</a>
            </div>
        '''
        st.markdown(html_display, unsafe_allow_html=True)
        st.success("🎉 Thumbnail processed safely!")
        
    else:
        st.error("Invalid Link! Please enter a valid YouTube video URL.")

st.write("---")
st.caption("Developed by Keshav Thathai | Need custom video utility tools for your brand? Contact me: thataikeshav873@gmail.com")


