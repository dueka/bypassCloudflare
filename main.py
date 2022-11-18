from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cloudscraper
from bs4 import BeautifulSoup as beauty
# import cfscrape
import json

# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()
# isNextDisabled = False
scraper = cloudscraper.create_scraper(delay=100, disableCloudflareV1=True, browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False,
        'custom': 'ScraperBot/1.0',
    }) 
print(scraper.get('https://www.datacamp.com/users/sign_in').text)

# scraper = cfscrape.create_scraper(disableCloudflareV1=True) 

# driver.get('https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cp_36%3A1253503011&dc&fs=true&qid=1645954406&ref=sr_ex_n_1')
# driver.get('https://www.datacamp.com/users/sign_in')

# info = scraper.get('https://www.datacamp.com/users/sign_in').text
# while not isNextDisabled:
#     try:
#         element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#             (By.XPATH, '//div[@data-component-type="s-search-result"]')))

#         elem_list = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")

#         items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        
#         for item in items:
#             title = item.find_element(By.TAG_NAME, 'h2').text
#             price = "No Price Found"
#             img = "No Image Found"
#             link = item.find_element(
#                 By.CLASS_NAME, 'a-link-normal').get_attribute('href')

#             try:
#                 price = item.find_element(
#                     By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
#             except:
#                 pass

#             try:
#                 img = item.find_element(
#                     By.CSS_SELECTOR, '.s-image').get_attribute("src")
#             except:
#                 pass

#             print("Title: " + title)
#             print("Price: " + price)
#             print("Image: " + img)
#             print("Link: " + link + "\n")

#         next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#             (By.CLASS_NAME, 's-pagination-next')))

#         next_class = next_btn.get_attribute('class')

#         if "disabled" in next_class:
#             isNextDisabled = True
#         else:
#             driver.find_element(By.CLASS_NAME, 's-pagination-next').click()

#     except Exception as e:
#         print(e, "Main Error")
#         isNextDisabled = True
# print(driver.page_source)
# print(h1)
# print(driver.current_url)
# driver.quit()