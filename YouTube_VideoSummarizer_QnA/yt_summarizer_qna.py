import os
import io
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# configure gemini api
load_dotenv()
GEMINI_API_KEY = os.getenv(key="GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


# Instantiate the gemini model
def instantiate_model():
    model = genai.GenerativeModel(model_name="gemini-pro")
    return model

#To generate response
def generate_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text

#To get the video id from the entered youtube url
def get_id(url):
    
    video_id = url.split("=")[1]
    if "&" in video_id:
        video_id = video_id.split("&")[0]

    return video_id

#To transcribe the youtube video
def get_transcripts(video_id):

    transcription_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcription = " ".join([transcript["text"] for transcript in transcription_list])
    
    return transcription

