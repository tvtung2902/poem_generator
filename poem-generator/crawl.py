from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import requests
import time
import random

from tqdm import tqdm


WAIT_TIME = 10

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, WAIT_TIME)

deletion_script = 'arguments[0].parentNode.removeChild(arguments[0]);'

datasets = []
for page_idx in tqdm(range(1, 10)):
    main_url = f'https://www.thivien.net/search-poem.php?PoemType=13&ViewType=1&ReplyType=3&Sort=Date&SortOrder=desc&Page={page_idx}'
    driver.get(main_url)
    
    selector_list_poem = '/html/body/div[4]/div[2]/div/div[@class="list-item"]'
    list_poem = driver.find_elements(By.XPATH, selector_list_poem)
    
    for idx in range(len(list_poem)):
        content_tag_xpath = f'/html/body/div[4]/div[2]/div/div[{2+idx}]'
        content_title_xpath = f'/html/body/div[4]/div[2]/div/div[{2+idx}]/h4/a'
        
        content_tag = wait.until(EC.presence_of_element_located((By.XPATH, content_tag_xpath)))
        poem_title = wait.until(EC.presence_of_element_located((By.XPATH, content_title_xpath))).text
        
        poem_url = wait.until(EC.presence_of_element_located((By.XPATH, content_title_xpath))).get_attribute('href')
        try:
            driver.get(poem_url)

            poem_src_xpath = '//div[@class="small"]'
            poem_content_tag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'poem-content')))

            poem_content = poem_content_tag.text
            print(poem_content)
            try:
                poem_src_tag = wait.until(EC.presence_of_element_located((By.XPATH, poem_src_xpath)))
                poem_src = poem_src_tag.text
            except:
                poem_src = ''

            poem_info = {
                'title': poem_title,
                'content': poem_content,
                'source': poem_src,
                'url': poem_url
            }

            datasets.append(poem_info)

            driver.back()
            print(datasets)
            
        except Exception as e:
            print(e)
            print(poem_url)

df = pd.DataFrame(datasets)[['title', 'content']]
df.to_csv('poems_dataset.csv', index=False)

driver.quit()
