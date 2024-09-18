import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import pandas as pd
import streamlit as st



genai.configure(api_key='AIzaSyCu6jKPW33Tz1-cKLpuC_lwFhcdqGMZnr8')
model = genai.GenerativeModel('gemini-pro')

df = pd.read_csv('output.txt', sep='\t')
link = df['text'].iloc[0]
st.title(link)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["question"]):
        st.markdown(message["question"]+" --> "+message["answer"])

df = pd.read_csv("C:/Users/devan/Desktop/work/law_websites/indian_kanoon/data.csv")
# st.write(df)
d = (df[df['title']==link]['data'])
print(d)
# st.write(d)
d = '\n'.join(d.astype(str).values.tolist())




if question := st.chat_input('questions'):
    st.write(f":red[{question}]")

    prompt = d + question
    response = model.generate_content(prompt)
    print(response.text) 
    st.write(f":blue[{str(response.text)}]")
    st.session_state.messages.append({"question":question , "answer": response.text})
