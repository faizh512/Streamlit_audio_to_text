import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment, silence
recog=sr.Recognizer()
final=""
st.markdown("<h1 style='text-align:center;'>Audio To Text</h1>", unsafe_allow_html=True)
st.markdown("---")
audio=st.file_uploader("Upload your Audio",type="mp3")
if audio:
    st.audio(audio)
    audio_segments=AudioSegment.from_file(audio)
    chunks=silence.split_on_silence(audio_segments,min_silence_len=500,silence_thresh=audio_segments.dBFS-20, keep_silence=100)
    for index,chunk in enumerate(chunks):
        chunk.export(str(index)+".wav",format="wav")
        with sr.AudioFile(str(index)+".wav") as source:
            recorded=recog.record(source)
            try:
                text=recog.recognize_google(recorded)
                final=final+" "+text
            except:
                st.write("Please Try Again File not Convertable")
    with st.form("Result"):
        result= st.text_area("",value=final)
        d_btn=st.form_submit_button("Download")
        if(d_btn):
            with open("Transcript.txt",'w') as f:

                f.write(result)
