# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time, os
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def remove_non_ascii(input_string):
#     return ''.join(char if ord(char) < 128 else '' for char in input_string)

# def remove_extra_spaces(text):
#     cleaned_text = re.sub(r'\s+', ' ', text)
#     cleaned_text = cleaned_text.strip()
#     return cleaned_text

# def keep_alphabets_and_spaces(input_string):
#     cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
#     return cleaned_string

# def remove_duplicates(input_list):
#     seen = set()
#     result = []
#     for item in input_list:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
#     return result



# cred =pd.read_csv("cred.csv")
# k=0

def listToString(s):
    str1 = " "
    return (str1.join(map(str, s)))

class Twitterbot:
   

    def get_links(self, lst,l): 
        org=lst
        links=[]
        print(lst)
        lst=lst.replace(" ","+")
        res=requests.get('https://indiankanoon.org/search/?formInput=' + lst)

        soup = BeautifulSoup(res.content,'lxml')
        # t-=1
        
        a=soup.find('div',{'class':'results_middle'})
        b=a.find_all('div',{'class':'result'})
        
        for i in b:
            link=i.find('a')
            link=str(link)
            pattern = r'/docfragment/(\d+)/'
            match = re.search(pattern, link).group(1)
            print(match)
            links.append("https://indiankanoon.org/doc/"+match+"/")
            # p+=1
        # k+=1
        lst=org.replace(" ","%20")
        t=1
        while(t<=l):
            print("page : ",t)
            # https://indiankanoon.org/search/?formInput=supereme%20court&pagenum=1
            res=requests.get('https://indiankanoon.org/search/?formInput=' + lst+"&pagenum="+str(t))
            print('https://indiankanoon.org/search/?formInput=' + lst+"&courtpagenum="+str(t))
            soup = BeautifulSoup(res.content,'lxml')
            a=soup.find('div',{'class':'results_middle'})
            print("number of links ", len(a))
            b=a.find_all('div',{'class':'result'})
            
            for i in b:
                link=i.find('a')
                link=str(link)
                pattern = r'/docfragment/(\d+)/'
                match = re.search(pattern, link).group(1)
                print(match)
                links.append("https://indiankanoon.org/doc/"+match+"/")
            t+=1


        return links
    
    def get_data(self,link):
        res=requests.get(link)
        soup = BeautifulSoup(res.content,'lxml')
        title=soup.find("h2",{"class": "doc_title"}).text
        author=soup.find("h3",{"class":"doc_author"})
        if(author!=None):
            author=author.find('a').text
        else:
            author=""
        data=""
        pt=soup.find_all('p')
        for i in pt:
            data=data+(i.text)
        return title,author,data

        




       

     

        



            
