#Importing Libraries/Modules
import streamlit as st

from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler



# Function to split data into smaller chunks and convert in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter() 
    texts = text_splitter.split_text(txt) 
    docs = [Document(page_content=t) for t in texts] 
    
    return docs
    
# Llama 2 LLM
def load_llm():
    # We instantiate the callback with a streaming stdout handler
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])   

    # loading the LLM model
    # This open source model can be downloaded from here
    # Their are multiple models available just replace it in place of model and try it.
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':1024,
                              'temperature':0.6})
        
    return llm
 
# Functions to generate response 
def chains_and_response(docs):
    
    llm = load_llm()
    chain = load_summarize_chain(llm,chain_type='map_reduce')
    
    return chain.run(docs)

#Streamlit setup
    
# Page title
st.set_page_config(page_title='Text Summarization App')
st.title('Text Summarization')

# Text input
txt_input = st.text_area('Enter the text to be summarized', '', height=200)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Processing...'):
            docs = chunks_and_document(txt_input)
            response = chains_and_response(docs)
            result.append(response)

if len(result):
    st.title('Summarization Result')
    st.info(response)