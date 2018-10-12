from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("http://profiles.doe.mass.edu/statereport/mcas.aspx")
html = driver.page_source
soup = BeautifulSoup(html)

yearPickerCounter = 0
gradePickerCounter = 0

#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#yearPicker.click()

yearPicker = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddYear"))
yearPicker.select_by_index(2)
print(len(yearPicker.options))

gradePicker = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddGrade"))

gradePicker.select_by_index(2)

studentGroupPicker = Select(driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_ddSubGroup"))
studentGroupPicker.select_by_index(4)

viewReportButton = driver.find_element_by_css_selector("#btnViewReport")
viewReportButton.click()

myElem = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'btnViewReport')))
print("Page is ready!")

'''
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
'''
driver.close()