from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    time.sleep(5)
    print("Website Opened Successfully")
#  ------ Header element  ------
    header_elements = driver.find_elements(By.XPATH,"//header[@id='header-container']/div[1]")
    print("Header Elements :")
    for header in header_elements:
       text = header.text
       if text != "":
         print(text)

# ------ Parent element ------
    parent_element = driver.find_element(By.XPATH,"//a[contains(.,'Courses')]")
    print("Parent Element Text:", parent_element.get_attribute("innerHTML"))

# ----- First Child element -----
    first_child_element_text = driver.find_element(By.XPATH,"//div[@id='solutions']/p[text()='LIVE Classes']").text
    print("first_child_element_text:",first_child_element_text)

# ----- second sibling of the first child element ------
    second_sibling_element = driver.find_element(By.XPATH, "//a[text()='Courses']/following-sibling::*[2]")
    print( "second_sibling_element_text:",second_sibling_element.get_attribute("innerHTML"))

# ----- Attribute href ------
    parent_of_href = driver.find_element(By.XPATH,"//a[@href= '/courses/programming/python/']/../../../p").text
    print("parent_of_href:",parent_of_href)

# ----- All ancestor elements -----
#  click on courses
    courses = driver.find_element(By.XPATH, "//p[text()='Courses']")
# find all ancestor elements
    ancestors =  driver.find_elements(By.XPATH,"//p[text()='Courses']/ancestor::div")
    print("Ancestors of 'Courses':")
    for ancestor in ancestors:
        print(ancestor.tag_name)

# Locate the "Courses" menu item
    courses = driver.find_element(By.XPATH, "//a[text()='Courses']")

# Find all following siblings of "Courses"
    siblings = driver.find_elements(By.XPATH, "//a[text()='Courses']/parent::li/following-sibling::li/a")
    for sibling in siblings:
        print(sibling.text)

#  ----- preceding sibling ------
    all_preceding_sibling = driver.find_elements(By.XPATH, "//a[text()='combos']/parent::li/preceding-sibling::li/a")
    all_preceding_sibling_texts = [el.text for el in all_preceding_sibling]
    print(all_preceding_sibling_texts)

