from bs4 import BeautifulSoup

def stats(driver):
    
    soup=BeautifulSoup(driver.page_source,'lxml')

    last = soup.find("td", {"class": "spent_on"})
    isue=soup.find("td",{"class":"issue"})
    print(last.text)
    print(isue.text)
    f=open("last.txt","w")

    f.write(last.text+"\n")
    f.write(isue.text)

    f.close()

