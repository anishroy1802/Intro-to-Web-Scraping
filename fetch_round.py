from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os

driver= webdriver.Chrome()
#delimiter is whitespace
problemset= input("Enter set number: ")

dir_name= "/"+problemset
current= os.getcwd()
dir= os.path.join(current, dir_name)
if not os.path.exists(dir):
    os.mkdir(dir)

os.chdir(dir)

pagename= "https://codeforces.com/contest/"+problemset
driver.get(pagename)

link= driver.find_element_by_link_text("Complete problemset")
link.click()

indexholder_list= driver.find_elements_by_class_name("problemindexholder")
#index_list= driver.find_elements_by_id("problemindex")
statement_list= driver.find_elements_by_class_name("problem-statement")
sampletest_list= driver.find_elements_by_class_name("sample-test")
l= len(statement_list)
print(l)
dir1= " "

for i in range(0,l):
    #statement_png= statement_list[i].screenshot_as_png()
    index= indexholder_list[i].get_attribute("problemindex")
    dir1_name= str(index)
    a= os.getcwd()
    dir1= dir+ "./"+dir1_name
    os.mkdir(dir1)
    os.chdir(dir1)

    input_list= sampletest_list[i].find_elements_by_class_name("input")
    output_list= sampletest_list[i].find_elements_by_class_name("output")
    m= len(input_list)
    print(os.getcwd())
    statement_list[i].screenshot("problem.png")
    for j in range(0,m):

        #input
        txt_i= input_list[j].text
        print(txt_i)
        file_i= "./"+"input"
        f1= open(file_i,"w")
        f1.write(txt_i)
        
        #output
        txt_o= output_list[j].text
        print(txt_o)
        file_o= "./output"
        f2= open(file_o,"w")
    
        f2.write(txt_o)

    os.chdir('..')    

    

time.sleep(5)
driver.quit()
