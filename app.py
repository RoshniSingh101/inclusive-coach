import streamlit as st
from google import genai
from google.genai import types
from database import init_db, save_session, get_all_sessions

# 1. Initialize DB outside the UI loop
init_db()

st.set_page_config(page_title="Gemini Inclusivity Coach", page_icon="💎")
st.title("💎 Gemini Workplace Coach")

gemini_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- UI Layout: Tabs make the pitch much cleaner! ---
tab1, tab2 = st.tabs(["🎙️ Live Coach", "📜 History"])

if gemini_key:
    # Initialize client safely
    client = genai.Client(api_key=gemini_key)

    with tab1:
        # Verify Key Logic
        if st.sidebar.button("Verify Key"):
            try:
                client.models.generate_content(model="gemini-2.5-flash", contents="Hi")
                st.sidebar.success("Key is valid!")
            except Exception:
                st.sidebar.error("Invalid API Key. Please check and try again.")

        # Recording Logic (updated for cloud deployment)
        audio_file = st.audio_input("Record your segment (click to start/stop)")

        if audio_file:
            with st.spinner("Gemini is analyzing your inclusivity..."):
                try:
                    # Read bytes directly from the widget
                    audio_bytes = audio_file.read()

                    prompt = "Analyze this audio for workplace stereotypes, tone, and provide coaching."

                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=[
                            prompt,
                            types.Part.from_bytes(data=audio_bytes, mime_type="audio/wav")
                        ]
                    )

                    save_session("Voice Recording", response.text)
                    st.success("Analysis saved!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"API Error: {e}")

    with tab2:
        st.header("📜 Meeting History")
        history = get_all_sessions()
        if not history:
            st.info("No past sessions yet.")
        else:
            for timestamp, trans, feed in history:
                with st.expander(f"Session: {timestamp}"):
                    st.write(feed)

else:
    st.info("👋 Welcome! Please enter your Gemini API Key in the sidebar to begin.")