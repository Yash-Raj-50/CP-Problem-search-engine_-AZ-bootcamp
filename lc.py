# Import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

page_URL = "https://leetcode.com/problemset/all/?page="

def get_a_tags():
    # driver.get(url)
    # time.sleep(7)
    links= driver.find_elements(By.TAG_NAME, "a")
    ans=[]
    pattern = "/problems"
    for i in links:
        try:
            if pattern in i.get_attribute("href"):
                ans.append(i.get_attribute("href"))
        except:
            pass    
    ans=list(set(ans))
    return ans
    # print(ans)

all_ques = []
total_pages = 55
def get_all_links(url):

    driver.get(url)
    time.sleep(7)

    links = [] 
    for i in range(1,total_pages+1):
        links += get_a_tags()
        
        if i != total_pages: 
            x_path = "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/nav/button[10]"
            element = driver.find_element("xpath",x_path)
            element.click() 
            time.sleep(7)
    
    links = list(set(links))  
    return links


# for i in range(1, 55):
#     all_ques += (get_a_tags(page_URL+str(i)))
all_ques= get_all_links(page_URL)
all_ques = list(set(all_ques))

with open('lc.txt', 'a') as f:
    for j in all_ques:
        f.write(j+'\n')

print(len(all_ques))

driver.quit()