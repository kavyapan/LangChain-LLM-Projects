## YouTube-VideoSummarization-QnA-Gemini
Leveraging the power of Gemini Pro LLM model from google , this project offers a streamlined solution for summarizing lengthy videos into concise summaries, facilitating quick comprehension of key points and also answeing user queries from the videos.

## Code Explanation

**Instantiate model**: This function initializes the Gemini Pro model from Google Generative AI.  

**Generate response**: Generates a response from the provided model and prompt.It takes two parameters: model, which is the initialized model instance, and prompt, which is the input text for generating the response.Within the function, it calls the generate_content method of the model object, passing the prompt as an argument.  

**Get Video ID** : Extracts the video ID from the YouTube video URL.  

**Get transcripts**:Retrieves the transcripts of a YouTube video using the YouTubeTranscriptApi.If successful, it concatenates the text from each transcript into a single string and returns it.  

**Streamlit setup:** This code block sets up a Streamlit application for the project. Allows users to choose between the YouTube video summarizer and question answering functionalities. It Integrates the model to generate summaries and respond to user queries.  
 

### Setup
Before running the application, make sure to set up your environment by installing the necessary dependencies. You can install the required packages by running:  
`pip install -r requirements.txt` 

### Configuration
The application uses environment variables to configure the Gemini API key. Ensure you have a .env file in the project directory containing your Gemini API key in the following format:  
*GEMINI_API_KEY=your_gemini_api_key_here*
  
**Run Streamlit App**: For running the application you simply need to go to the terminal and write `streamlit run main_app.py`  

**App Response**  
![App Response](https://github.com/kavyapan/LangChain-LLM-Projects/blob/main/YouTube_VideoSummarizer_QnA/app_response.JPG) 

![App Response](https://github.com/kavyapan/LangChain-LLM-Projects/blob/main/YouTube_VideoSummarizer_QnA/app_response_2.JPG)