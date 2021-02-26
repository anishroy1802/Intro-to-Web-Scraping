from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome()

driver.get("https://moodle.iitd.ac.in/login/index.php")
texit = driver.find_element_by_id("login").text
print(texit)
time.sleep(10)
username1= driver.find_element_by_id("username")
passwd1= driver.find_element_by_id("password")

user_input= input("enter username ")

pass_input= input("enter password ")
username1.send_keys(user_input)
passwd1.send_keys(pass_input)

loginbutton= driver.find_element_by_id("loginbtn")
box= driver.find_element_by_id("valuepkg3")
#now we manipulate the texit string
result= 0
m1=0
m2=0
result1=0
res_arr= texit.split()

if ("first" in texit):
    for i in range(0,len(res_arr)):
        if (res_arr[i]== ","):
            result= res_arr[i-1]
elif ("second" in texit):
    for i in range(0,len(res_arr)):
        if (res_arr[i]== ","):
            result= res_arr[i+1]
elif ("add" in texit):
    for i in range(0,len(res_arr)):
        if (res_arr[i]== "+"):
            result1= int(res_arr[i-1])+ int(res_arr[i+1])
            result= str(result1)
else:
    for i in range(0,len(res_arr)):
        if (res_arr[i]== "-"):
            result1= (int(res_arr[i-1])- int(res_arr[i+1]))
            result= str(result1)


box.send_keys(result)

time.sleep(5)
loginbutton.click()


time.sleep(5)
driver.quit()
