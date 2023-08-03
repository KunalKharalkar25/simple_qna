from langchain import OpenAI
#importing openai model from langchain 

import streamlit as st 
#importing streamlit for UI

#function for response
def load_answer(question):
    llm=OpenAI(model_name="text-davinci-003", temperature=0)
    answer=llm(question)
    return answer

st.set_page_config(page_title="Simple Q&A App", page_icon=":robot:")
st.header("Simple Q&A App")

#function which collects input from user
def input_data():
    input_text= st.text_input("You: ", key="input")
    return input_text

#main process
user_input=input_data()
response=load_answer(user_input)

submit= st.button("Generate")

if submit:
    st.subheader("Answer: ")
    st.write(response)
