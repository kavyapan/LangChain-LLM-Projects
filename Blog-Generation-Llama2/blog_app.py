import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function To get response from LLAma 2 model
def get_response(topic,word_count,selection):

    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':1024,
                              'temperature':0.1})
    
    #Creating Prompt Template
    template="""
        Write a blog for {selection} on topic {topic},
        the word limit for blog should be {word_count} words.
            """
    
    prompt=PromptTemplate(input_variables=["selection","topic","word_count"],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(selection=selection,topic=topic,word_count=word_count))
    print(response)
    return response



# Streamlit Setup

# Page title
st.set_page_config(page_title='Blog Generation App')
st.title('Blog Generation')


# Text input
topic = st.text_input("Enter the Topic to Generate Blog")


col1,col2 = st.columns([4,4])

with col1:
    word_count = st.text_input('Specify Word Count for Blog')
with col2:
    selection = st.selectbox('Writing the blog for',
                            ('Children','Adult'),index=0)
    
submit = st.button("Submit")

## Final response
if submit:
    st.write(get_response(topic,word_count,selection))