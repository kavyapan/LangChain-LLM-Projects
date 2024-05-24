## Blog-Generation-Llama2
Leveraging the power of the Llama2 , this project offers a solution for creating blogs in the specified number of words for the target audience.

## Explanation

**1.Function to get response:** This function is responsible for generating a blog response based on three main parameters:  
topic: The topic for which the blog is being generated.  
word_count: The desired word count for the generated blog.  
selection: The target audience for the blog, which can be either "Children" or "Adult".  

**LLaMA 2 Model Initialization:** This part initializes the LLaMA 2 model using the CTransformers class from the ct2 library. It loads the pre-trained LLaMA 2 model file (llama-2-7b-chat.ggmlv3.q8_0.bin) located in the model directory.

**Prompt Template Creation:** A prompt template is created  to denote placeholders for the selection, topic, and word_count variables. This template will be used to formulate the input prompt for the LLaMA 2 model..

**Streamlit setup:** The Streamlit setup creates a simple user interface with text input fields for the topic and word count, and a dropdown menu for selecting the target audience (children or adults). Upon clicking the "Submit" button, the generated blog response is displayed.  


### Requirements
**1.Download the Llama2 Model**: The latest Llama2 Model can be downloaded from [huggingface](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) . Ensure that the LLaMA 2 model file (llama-2-7b-chat.ggmlv3.q8_0.bin) is placed in the model directory before running the application.
**2.Install Requirements**:Activate the virtual environment and install necessary libraries/modules `pip install -r requirements.txt`  
**3.Run Streamlit App**: For running the application you simply need to go to the terminal and write `streamlit run blog_app.py` 