import streamlit as st
import pandas as pd
import google.generativeai as genai

genai.configure(api_key='AIzaSyCu6jKPW33Tz1-cKLpuC_lwFhcdqGMZnr8')
model = genai.GenerativeModel('gemini-pro')

df = pd.read_csv("C:/Users/devan/Desktop/work/law_websites/indian_kanoon/data.csv")
st.title("classify")
df["type"]=None
df["severity"]=None
df["judgement"]=None
st.write(df)

# for i in range(len(df)):
#     d=df['data'][i]
#     prompt = d + "give answer only among the following options: a)type of case : road accident,crime,marriage? b)severity of the case - death,injury,trauma,none? c)what is the judgement passed - death, fine, imprisonment?"
#     response = model.generate_content(prompt)
#     print(response.text)
d=df['data'][1]
#prompt = d + "classify the case and choose only among the options: a)type of case : 1.road accident,2.crime,3.marriage related b)severity of the case - 1.death,2.injury,3.trauma,4.none c)what is the judgement passed - 1.death, 2.fine, 3.imprisonment"
prompt = d+" strictly choose one of the following 1. type of case - road accident, crime ,marriage 2. severity of the case - death, medical issue, phycological trauma 3. judgements - death, fine, imprisonment years. "
response = model.generate_content(prompt)
print(response.text)
st.write(response.text)
