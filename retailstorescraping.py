# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:11:47 2023

@author: hnrne
"""
import json
import pandas
import sqlite3
from itertools import zip_longest
from selenium import webdriver
from time import sleep
import csv
path = r'C:\Users\hnrne\Downloads\chromedriver_win32\chromedriver'
# open the browser
browser = webdriver.Chrome(executable_path=path)
# load the webpage
browser.get('https://www.bing.com/maps?ty=17&q=lenskart&chain=18473912&segment=Local&mb=16.712133%7E80.59745%7E16.498838%7E81.097473&ppois=16.498838424682617_80.64946746826172_Lenskart.Com+At+Mg+Road_YN4070x12458816184159521382%7E16.535968780517578_80.59745025634766_Lenskart.com+at+Bhavanipuram_YN4070x8243183120069838512%7E16.712133407592773_81.09747314453125_Lenskart.com+At+Eluru_YN4070x9547571026267406038%7E&usebfpr=true&v=2&sV=1&FORM=SNAPST&cp=16.471533%7E80.847267&lvl=10.4')
browser.maximize_window()
storenames = []
addresses=[]
timings=[]
latitudes=[]
longitudes=[]
phonenumbers=[]

store = browser.find_elements_by_xpath("//a[@class='listings-item  ']")
time=browser.find_elements_by_xpath("//span[@class='data-appns']")
phone=browser.find_elements_by_xpath("//div[@class='b_factrow']")
for anchor_tag in store:
    #entity_data = json.loads(anchor_tag['data-entity'])
    entity_data=anchor_tag.get_attribute("data-entity")
    entity_data=json.loads(entity_data)
    title = entity_data['entity']['title']
    storenames.append(title)
    address = entity_data['entity']['address']
    addresses.append(address)
    latitude=entity_data['routablePoint']['latitude']
    latitudes.append(latitude)
    longitude=entity_data['routablePoint']['longitude']
    longitudes.append(longitude)
    print(title)
    print(address)
    print(latitude)
    print(longitude)
for i in time:
    timings.append(i.text)
for j in phone:
    phonenumbers.append(j.text)
print(timings)
print(phonenumbers)
   
    
    

header=['store Name','Address','Timings','Latitude','Longitude','phone number']

with open(r"C:\Users\hnrne\Downloads\retailstores.csv", 'w', newline='',encoding='UTF8') as output_file:
    dict_writer = csv.writer(output_file)
    dict_writer.writerow(header)
    for row in zip(storenames,addresses,timings,latitudes,longitudes,phonenumbers):
        dict_writer.writerow(row)
    print(storenames)



