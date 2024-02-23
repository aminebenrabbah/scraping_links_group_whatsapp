from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#in first you need install python and selenium and webdriver for google chrome
web_chrome  = webdriver.Chrome()




def save(nom_file ,a_or_write_or_read,text):
    file = open(nom_file+'.txt',a_or_write_or_read)
    file.write(text+str('\n'))
    file.close()

#this function for get links web site from bing
def get_link_form_bing(web_chrome):
    links  = web_chrome.find_elements(By.TAG_NAME , value = 'cite')
    #this liste for add links
    liste_links = []
    for link in links:
        if link.text in liste_links:
            continue
        #get link save in liiste
        liste_links.append(link.text)
    #return liste 
    return liste_links


#this function for get group
def scraping_group_whathsap(web_chrome,link,name_file):
    web_chrome.get(link)
    time.sleep(5)
    links = web_chrome.find_elements(By.TAG_NAME , value = 'a')
    time.sleep(3)
    liste_group = []
    
    for link in links:
        if 'https://chat.whatsapp.com/invite' in link.get_attribute('href'):
            print(link.get_attribute('href'))
            if link.get_attribute('href') in liste_group:
                continue
            liste_group.append(link.get_attribute('href'))
            #this function for save link for groupe
            save(name_file,'a',link.get_attribute('href'))

 


#this function for scrole in bing
def scrole(web_chrome,number):
    contry = input('give country you need extract has nuber')
    name_file = input('give me name file for save data')
    web_chrome.get('https://www.bing.com/search?q=whatsapp+group+'+contry)
    time.sleep(4)
    for num in range(1,number+1):
        try:
            
            #function for get links
            links_web_site = get_link_form_bing(web_chrome)
            for link in links_web_site:
                scraping_group_whathsap(web_chrome,link,name_file)
                time.sleep(5)
            #click for next page 
            web_chrome.find_element(By.CLASS_NAME , value = "sb_pagN").click()
                                
        except:
            print('err')
            web_chrome.refresh()
            time.sleep(10)
        time.sleep(3)

           







scrole(web_chrome,110)		
