import os 
import time
from selenium import webdriver
os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()


driver.get('https://www.accuweather.com/en/in/kurla-west/3352451/weather-forecast/3352451?current=true')
temperature_innerHTML = list(driver.find_element("xpath",'/html/body/div/div[7]/div[1]/div[1]/a[1]/div[1]/div[1]/div/div/div[1]').get_attribute('outerHTML'))
temp_list1 = []

for i in temperature_innerHTML:
    anchor_index = temperature_innerHTML.index('°')
temp_tens = str(temperature_innerHTML[anchor_index-2])
temp_unis = str(temperature_innerHTML[anchor_index-1])
temperature_string = temp_tens+temp_unis
print(f"The current temperature is: {temperature_string}")
temperature_int = int(temperature_string)
# print(anchor_index)

# print(temp_list1)
# print(temperature_innerHTML)
# time.sleep(5)
