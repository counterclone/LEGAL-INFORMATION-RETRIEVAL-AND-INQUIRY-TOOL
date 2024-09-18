import streamlit as st
import indian_kanoon_bot as tb
import pandas as pd
import time
import os
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from scipy.special import softmax

st.set_page_config(page_title="Start", page_icon="^0^")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

hashtag = [""]

st.title("indian kanoon")





lst = st.text_input('Enter ', "supereme court")
rate = st.number_input('Refresh Rate', 2)
links=[]

if ( st.button('Submit') 
    # or st.session_state["submit"]
    ):
    # lst = [tag.strip() for tag in lst.split(" ")]
    # hashtag.extend(lst)


    bot = tb.Twitterbot()

    
    st.write("fetching data")
    links = bot.get_links(lst, rate)
    
    df = pd.DataFrame({'links': links})
    st.write(df)
    title=[]
    author=[]
    data=[]
    t=0
    for i in links:
        tit,auth,d=bot.get_data(i)
        title.append(tit)
        author.append(auth)
        data.append(d)
        t+=1
        print(t)
    
    df=pd.DataFrame({'title':title,"author":author,"data":data})
    st.write(df)
    df.to_csv('data.csv', index=False)
        
    