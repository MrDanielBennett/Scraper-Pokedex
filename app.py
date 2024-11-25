from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import config

    ## Sumarize using chat GPT
    ## Write Sumarized Dex Desc to Json File
    ## JSON element will contain number, desc, maybe picture link

driver = webdriver.Chrome()

base_url = "https://www.serebii.net/pokedex-rs/"
num_pages = 9
num_pages_double = 99
num_pages_triple = 151
ruby_entry = " "
emerald_entry = " "
firered_entry = " "
ruby_element = ''
emerald_element = ''
firered_element = ''
base_image_url = "https://www.serebii.net/emerald/pokemon/"
api_key = config.gpt_api_key

print(api_key)

for i in range(1, num_pages + 1):
    url=f"{base_url}" + "00" + f"{i}" + ".shtml"
    print(f"Navigating to: {url}")
    driver.get(url)

    time.sleep(3)

    ## Description grab
    ruby_element = driver.find_element(By.XPATH, "//table//td[@class='ruby']")
    ruby_entry = ruby_element.find_element(By.XPATH, "following-sibling::td")
    ruby_entry_text = ruby_entry.text
    print("Ruby Dex: " + ruby_entry_text)

    emerald_element = driver.find_element(By.XPATH, "//table//td[@class='emerald']")
    emerald_entry = emerald_element.find_element(By.XPATH, "following-sibling::td")
    emerald_entry_text = emerald_entry.text
    print("Emerald Dex: " + emerald_entry_text)

    firered_element = driver.find_element(By.XPATH, "//table//td[@class='firered']")
    firered_entry = firered_element.find_element(By.XPATH, "following-sibling::td")
    firered_entry_text = firered_entry.text
    print("Fire Red Dex: " + firered_entry_text)

    ##image url grab
    image_url = f"{base_image_url}" + "00" + f"{i}" + ".png"
    print("This is the image link" + image_url)

    ##Summarize Descriptions using ChatGPT
    description_for_gpt = "Summarize these Descriptions as a Pokedex entry: " + ruby_entry_text + emerald_entry_text + firered_entry_text
    print(description_for_gpt)
    

for i in range(10, num_pages_double +1):
    url=f"{base_url}" + "0" + f"{i}" + ".shtml"
    print(f"Navigating to: {url}")
    driver.get(url)

    time.sleep(3)

    ##Description grab
    ruby_element = driver.find_element(By.XPATH, "//table//td[@class='ruby']")
    ruby_entry = ruby_element.find_element(By.XPATH, "following-sibling::td")
    ruby_entry_text = ruby_entry.text
    print("Ruby Dex: " + ruby_entry_text)

    emerald_element = driver.find_element(By.XPATH, "//table//td[@class='emerald']")
    emerald_entry = emerald_element.find_element(By.XPATH, "following-sibling::td")
    emerald_entry_text = emerald_entry.text
    print("Emerald Dex: " + emerald_entry_text)

    firered_element = driver.find_element(By.XPATH, "//table//td[@class='firered']")
    firered_entry = firered_element.find_element(By.XPATH, "following-sibling::td")
    firered_entry_text = firered_entry.text
    print("Fire Red Dex: " + firered_entry_text)

    ##image url grab
    image_url = f"{base_image_url}" + "0" + f"{i}" + ".png"
    print("This is the image link " + image_url)


for i in range(100, num_pages_triple +1):
    url=f"{base_url}" + f"{i}" + ".shtml"
    print(f"Navigating to: {url}")
    driver.get(url)

    time.sleep(3)

    ##Description grab
    ruby_element = driver.find_element(By.XPATH, "//table//td[@class='ruby']")
    ruby_entry = ruby_element.find_element(By.XPATH, "following-sibling::td")
    ruby_entry_text = ruby_entry.text
    print("Ruby Dex: " + ruby_entry_text)

    emerald_element = driver.find_element(By.XPATH, "//table//td[@class='emerald']")
    emerald_entry = emerald_element.find_element(By.XPATH, "following-sibling::td")
    emerald_entry_text = emerald_entry.text
    print("Emerald Dex: " + emerald_entry_text)

    firered_element = driver.find_element(By.XPATH, "//table//td[@class='firered']")
    firered_entry = firered_element.find_element(By.XPATH, "following-sibling::td")
    firered_entry_text = firered_entry.text
    print("Fire Red Dex: " + firered_entry_text)

    ##image url grab
    image_url = f"{base_image_url}" + f"{i}" + ".png"
    print("This is the image link " + image_url)

driver.quit()
