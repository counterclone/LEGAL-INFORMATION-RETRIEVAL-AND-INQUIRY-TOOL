import streamlit as st
import advocate_khoji as tb
import pandas as pd
import time
import os
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from scipy.special import softmax

st.set_page_config(page_title="Start", page_icon="^0^")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

hashtag = [""]

st.title("advocate khoji")





lst = st.text_input('Enter ', "tamil nadu")
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
    st.write(links)
    
    con=[]
    for i in links:
        con.append(bot.get_data(i))
    df=pd.DataFrame(con)
    st.write(df)
    df.to_csv("output.csv")
    
    
        
    