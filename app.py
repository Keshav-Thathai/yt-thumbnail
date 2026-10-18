import streamlit as st
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
        # Complex URL formats aur query parameters ko handle karne ka perfect split logic
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        elif "shorts/" in video_url:
            video_id = video_url.split("shorts/")[1].split("?")[0]
    except Exception:
        video_id = None

    if video_id:
        thumbnail_url = f"https://youtube.com{video_id}/maxresdefault.jpg"
        
        try:
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
                # Backup option agar standard maxresdefault image available nahi hai
                backup_url = f"https://youtube.com{video_id}/hqdefault.jpg"
                backup_response = requests.get(backup_url)
                if backup_response.status_code == 200:
                    img_bytes = backup_response.content
                    st.subheader("🖼️ Thumbnail Preview:")
                    st.image(backup_url, use_container_width=True)
                    st.write("---")
                    st.success("🎉 Download Ready! Click the button below to save.")
                    st.download_button(
                        label="📥 Click Here to Download Image",
                        data=img_bytes,
                        file_name=f"yt_thumbnail_{video_id}.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.error("High-Definition thumbnail is not available for this video.")
        except Exception:
            st.error("Network error occurred while fetching the image.")
    else:
        st.error("Invalid Link! Please enter a valid YouTube video URL.")

st.write("---")
st.caption("Developed by Keshav | Need custom video utility tools for your brand? Contact me!")



