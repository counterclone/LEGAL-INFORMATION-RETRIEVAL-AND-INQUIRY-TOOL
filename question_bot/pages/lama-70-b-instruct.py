import openai
import pandas as pd
import streamlit as st
client = openai.OpenAI(
    api_key="3952139433174d408c09c2d584a00dcb",
    base_url="https://api.aimlapi.com",
)

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

    system_content = question
    user_content = d

    chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=128,
    )

    #prompt = d + question
    response = chat_completion.choices[0].message.content
    print(response) 
    st.write(f":blue[{str(response)}]")
    st.session_state.messages.append({"question":question , "answer": response})

