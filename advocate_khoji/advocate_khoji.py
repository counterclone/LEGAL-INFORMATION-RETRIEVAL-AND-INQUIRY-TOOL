from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time, os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def listToString(s):
    str1 = " "
    return (str1.join(map(str, s)))

class Twitterbot:
    def __init__(self):
       
        print("login")
        self.k=0
        edge_options = Options()  # Use EdgeOptions instead of ChromeOptions
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
        
        edge_options.add_argument(f'user-agent={user_agent}')
        #edge_options.add_argument("--headless=new")
        
        self.bot = webdriver.Edge( options=edge_options)




    def get_links(self, lst,l): 
        bot=self.bot
        org=lst
        links=[]
        print(lst)
        lst=lst.replace(" ","+")
        bot.get('https://www.advocatekhoj.com/library/judgments/search.php?q=' + lst)
        time.sleep(2)
        page_source = bot.page_source
        soup = BeautifulSoup(page_source,'html.parser')
        
        # t-=1
        # print(soup)
        
        a=soup.find('div',{'class':'gsc-expansionArea'})
        # print(a)
        b=a.find_all('div',{'class':'gsc-webResult gsc-result'})
        # b=b.find('div',{'class':'gsc-thumbnail-inside'}).find('div',{'class':'gs-title'})
        for i in b:
            link=i.find('div',{'class':'gsc-thumbnail-inside'}).find('div',{'class':'gs-title'}).find('a')
            print(link['href'])
            links.append(link['href'])

        clk=bot.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[7]/td/form/div/div[2]/div[2]/div/div/div/div[5]/div[2]/div/div/div[2]/div/div[2]')
        
        clk.click()

        time.sleep(2)
        return links
    
    def get_data(self,link):
        bot=self.bot
        bot.get(link)
        time.sleep(2)
        page_source = bot.page_source
        soup = BeautifulSoup(page_source,'html.parser')
        soup=soup.find('div',{'class':'contentarea'}).find_all('p')
        content=""
        for i in soup:
            content+=i.text
        return content
        

        




       

     

        



            
