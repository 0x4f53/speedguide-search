from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time, os, traceback
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

from PIL import Image

def scrape_page (url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(                      
        service=Service(
            executable_path=ChromeDriverManager().install()
        ),
        options=options
    )
    
    source =""
    
    try:  
        print (f"Fetching page from {url}")
        driver.get(url)
        time.sleep(2)
        
        source = driver.page_source

    except:
        print ("An error occurred:")
        traceback.print_exc()
        driver.quit()
        
    return source

def grab_port_table(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    table = soup.find('table', class_='port-outer')
    rows = []
    for row in table.find_all('tr'):
        cells = [cell.text for cell in row.find_all(['th', 'td'])]
        rows.append(cells)
    for row in rows: print(row[0])  

source = scrape_page("https://www.speedguide.net/port.php?port=443")
grab_port_table(source)
