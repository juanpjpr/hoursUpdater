
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from stadistics import stats



def guardarHoras(user,pwd,id,hs,coments):
   
       #PATH="C:\Program Files (x86)\chromedriver.exe"
        PATH="./chromedriver.exe"
        
        driver= webdriver.Chrome(PATH)

        driver.get("http://152.170.241.87/login")

        username=driver.find_element_by_id("username")
        username.send_keys(user)

        password=driver.find_element_by_id("password")
        password.send_keys(pwd)
        

        password.send_keys(Keys.RETURN)
   
        driver.get("http://152.170.241.87/issues/"+id+"/time_entries/new")
        print("http://152.170.241.87/issues/"+id+"/time_entries/new")

        time_entry_hours=driver.find_element_by_id("time_entry_hours")
        time_entry_hours.send_keys(hs)

        time_entry_coments=driver.find_element_by_id("time_entry_comments")
        time_entry_coments.send_keys(coments)

        time_entry_coments.send_keys(Keys.RETURN)

        driver.get("http://152.170.241.87/issues/"+id+"/time_entries")
        
        stats(driver)

        driver.implicitly_wait(5)


        
