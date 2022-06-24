import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import csv
from datetime import datetime
import sys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='driver/chromedriver',chrome_options=chrome_options)

desired_cap = chrome_options.to_capabilities()


base_url_g = u'https://google.com/search?q='
youtube_base_url = 'https://youtube.com/results?search_query='
serp_folder_path = 'SERP_{}'.format(datetime.now())

def y_search_bot(query):
    '''
    This helper function takes in a query and searches for that query on YouTube using Selenium. 
    '''
    url_to_send = f"{youtube_base_url}{query}"
    driver.get(url_to_send)
    sleep(3)
    return driver.page_source


def search_and_get_results(query):
    '''
    Combines y_search_bot and y_get_results to search and collect results from YouTube.
    '''
    result_html = y_search_bot(query)
    with open('{}/{}.html'.format(serp_folder_path, query), 'w') as result_file:
        result_file.write(result_html)

def search_all_queries(queries_file_csv):
    os.mkdir(serp_folder_path)
    with open(queries_file_csv, 'r') as inputF:
        queries = []
        reader = csv.reader(inputF)
        for row in reader:
            queries.append(row[0])

    for query in queries:
        search_and_get_results(query.replace('/',''))

if __name__ == "__main__":
    search_all_queries(sys.argv[1])
    driver.close()