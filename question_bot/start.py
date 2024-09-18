import streamlit as st
import pandas as pd


df = pd.read_csv("C:/Users/devan/Desktop/work/law_websites/indian_kanoon/data.csv")
st.title("chatbot implementation")

txt=df['title']

for i in txt:
    if st.button(i):
        st.write(i)
        string_data = i
        df = pd.DataFrame({'text': [string_data]})
        df.to_csv('output.txt', sep='\t', index=False)
        st.write("button selected move to fetch")
