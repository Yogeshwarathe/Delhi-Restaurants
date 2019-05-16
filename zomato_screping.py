from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint

driver = webdriver.Chrome()
driver.get('https://www.zomato.com/ncr/great-food-no-bull')
page = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(page,'html.parser')
# print(soup)
main = soup.find("div",class_="row col-res-list collection_listings_container")
all = main.findAll('div',class_="col-s-8 col-l-1by3")
# print(all)
big_list = []
id = 1
for i in all:
    a = i.find("div",class_='h100 pb20').find('a')['href']
    # print(a)
    driver = webdriver.Chrome()
    driver.get(a)
    page = driver.execute_script('return document.documentElement.outerHTML')
    driver.quit()
    soup = BeautifulSoup(page,'html.parser')
    # print(soup)
    name = soup.find('div',class_='col-l-12').find('a')['title']
    # print(name)
    detels = soup.findAll('div',class_='row ui segment')
    # print(detels)
    for j in detels:
        b = j.find('div',class_="mbot").text.split()
        phone_number = (b[2]+b[3])
        # print(phone_number)

    w = soup.find('div',class_='res-info-detail').text.split()
    # print(w)
    average = ''
    for k in w:
        average += k + ' '
    # print(average)

    opening = soup.findAll('div',class_='medium')
    # print(opening)
    opening_hours = ''
    for o in opening:
        opening_hours  = o.text
    # print(opening_hours)
        
    addr = soup.findAll('div',class_='resinfo-icon')
    # print(address)
    address = ''
    for m in addr:
        address = m.text


    more = soup.findAll('div',class_='res-info-feature-text')
    more_info = ''
    for e in more:
        # print(e.text)
        more_info +=  ' ' + e.text + ' /'
    # print(more_info)

    featured = soup.findAll('div',class_='ln24')
    # print(featured)
    featured_in_collecions = ''
    for s in featured:
        featured_in_collecions += ' ' + s.text + " "
    # print(featured_in_collecions)
    dict_1 = {"id":id,"Hotel_name":name,"Phone_number":phone_number,"Link":a,"Average_cast":average,"Opening_hours":opening_hours,"Address":address,"more_info":more_info,"Featured_in_Collections":featured_in_collecions}
    pprint(dict_1)
    big_list.append(dict_1)
    # print(big_list)
    id+=1
# pprint(big_list)
