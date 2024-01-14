import os, datetime, traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time, os, traceback
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

directory = ".cache/"
file_name_extension = ".time"

def getCurrentTimestamp(): return datetime.datetime.fromtimestamp(int(datetime.datetime.now().timestamp()), tz=datetime.timezone.utc) 

def getLastScanTimestamp(filename) -> datetime:
    
    timestamp = None
    
    if not os.path.exists(directory): 
        raise FileNotFoundError()
    
    with open (directory + "/" + str(filename) + file_name_extension, "r") as data_file:
        timestamp = datetime.datetime.fromtimestamp(int(data_file.read()), tz=datetime.timezone.utc)
        data_file.close()
    
    return timestamp

def setLastScanTimestamp(filename) -> datetime:
    
    if not os.path.exists(directory): 
        os.mkdir(directory)
        print (f"Created a cache directory at: {os.path.abspath(directory)}")
    
    timestamp = int(datetime.datetime.now().timestamp())
    
    with open (directory + "/" +  str(filename) + file_name_extension, "w") as data_file:
        data_file.write(str(timestamp))
        data_file.close()
    
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)  

def substringAfter(text, substring): return text.split(substring, 1)[-1]

def saveData(data, file_name):
    directory = ".cache/"
    if not os.path.exists(directory): 
        os.mkdir(directory)
        print (f"Created a cache directory at: {os.path.abspath(directory)}")
        
    with open (directory + "/" + file_name, "w") as data_file:
        data_file.write(data)
        data_file.close()
    
    return True
    
def scrapePage (url):
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

def grabPortTable(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    table = soup.find('table', class_='port-outer')
    rows = []
    for row in table.find_all('tr'):
        cells = [cell.text for cell in row.find_all(['th', 'td'])]
        rows.append(cells)
    for row in rows: print(row[0])  