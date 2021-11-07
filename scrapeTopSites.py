#!/usr/bin/python3

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

urls = ["https://www.alexa.com/topsites", "https://www.alexa.com/topsites/countries/US"]

def scrape(url):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    arr = []
    with webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 10) 
        driver.get(url)
        elems = driver.find_elements(By.XPATH, "//div[@class='td DescriptionCell']/p")
        print(url, ': ', len(elems))
        arr = [e.text for e in elems]   
    return arr

def main():
    sites = set()
    for url in urls:
        sites.update(scrape(url))

    with open('topsites.txt', 'w') as f:
        print(len(sites))
        for s in sites:
            f.write(s + '\n')

main()