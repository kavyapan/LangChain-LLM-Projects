import streamlit as st
import yt_summarizer_qna as yt

def main():
    with st.sidebar:
        st.subheader("Select application!")
        option = st.selectbox(
            'Select from below options',
            ('Generate Video Summary', 'Ask Questions related to video')),

    if option[0] == "Generate Video Summary":
        st.title("YouTube-Video Summarizer")
        youtube_url = st.text_input("Enter link of youtube video :")
        if youtube_url:
            video_id = yt.get_id(youtube_url)
            st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=50)
        submit = st.button("submit")

        # Defining Prompt
        model_behavior = """ You are an expert in  youtube video summarization from transcription of video.
                    Input is video transcription and output will be summary of video including all 
                    the important information.Generate summary in 2 to 3 paragraphs and maximum 500 words. 
                    Provide relevant topic for the summary. Please don't add extra information but fix any typos .
                    If transcription is meaningless or empty return `Couldn't generate summary for the given video`.
                    This is the transcriptions for the video.
                """

        if submit:
            transcriptions = yt.get_transcripts(video_id)


            # initializing gemini-pro model
            gemini_model = yt.instantiate_model()
            final_prompt = model_behavior + "\n\n" + transcriptions
            summary = yt.generate_response(model=gemini_model, prompt=final_prompt)
            st.write(summary)


    if option[0] == "Ask Questions related to video":
        st.title("Answering questions from YouTube video")
        youtube_url = st.text_input("Enter link of youtube video :")
        if youtube_url:
            video_id = yt.get_id(youtube_url)
            st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=50)

        user_prompt = st.text_area("Please ask your question related to entered video", key="user_prompt")
        submit = st.button("submit")

        model_behavior = """ You are expert in summarization of youtube videos from transcription of videos.
             Input is transcriptions of videos along with prompt which have the user query. Please make sure that you have
             understood all the information present in the video from transcription and respond to user query. 
             Please don't add extra information that doesn't make sense but fix typos and return `Couldn't transcribe the video` 
             if transcription of video is empty otherwise respond accordingly!.
        """
        if user_prompt or submit:
            video_transcriptions = yt.get_transcripts(video_id)
            gemini_model = yt.instantiate_model()
            model_behavior = model_behavior + f"\nvideo transcription: {video_transcriptions} \nprompt: {user_prompt}"
            response = yt.generate_response(model=gemini_model, prompt=model_behavior)
            st.write(response)


if __name__ == "__main__":
    main()