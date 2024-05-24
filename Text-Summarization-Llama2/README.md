## Text-Summarization-Llama2
Leveraging the power of the Llama2 text summarization model, this project offers a streamlined solution for condensing lengthy documents into concise summaries, facilitating quick comprehension of key points.

## Explanation
The project provides functions to split data into smaller chunks, load the Llama2 model, and generate summarization responses:

**1.Function to split data into smaller chunks and convert in document format:** This function takes a text input and splits it into smaller chunks using a CharacterTextSplitter. Each chunk is then converted into a Document object. The function returns a list of these Document objects, representing the segmented text.

**Llama 2 LLM:** Here, a function named load_llm_model is defined, responsible for loading the Llama2 model for text summarization. It initializes a callback manager and loads the Llama2 model using the CTransformers class. The function returns the loaded Llama2 model.

**Functions to generate response:** This function, generate_response, utilizes the loaded Llama2 model to generate a summarization response. It loads a summarization chain, likely defined elsewhere, and runs it on the input documents to produce the response.

**Streamlit setup:** This code block sets up a Streamlit application for the text summarization project. It imports the necessary libraries, sets the page title and title text, provides a text area for user input, and creates a form to accept user input for summarization. When the form is submitted, it processes the input text, generates a summarization response, and displays the result using Streamlit's UI elements.  

These code blocks collectively form the core functionality of the text summarization project using Llama2, including text preprocessing, model loading, response generation, and integration with the Streamlit framework for user interaction.  

### Requirements
**1.Download the Llama2 Model**: The latest Llama2 Model can be downloaded from [huggingface](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) and save in the folder named models in project directory.  
**2.Install Requirements**:Activate the virtual environment and install necessary libraries/modules `pip install -r requirements.txt`  
**3.Run Streamlit App**: For running the application you simply need to go to the terminal and write `streamlit run texts_app.py`  
