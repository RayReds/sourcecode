from selenium import webdriver
from datetime import date
import time

web = webdriver.Chrome("D:\Ray\Coding\Private Coding\chromedriver.exe")
web.get('https://docs.google.com/forms/d/e/1FAIpQLSeDCMxNLSMco29PKwUWQT22soNJ5YOT3-mXT3DYHGrBGBjgMQ/formResponse')

time.sleep(2)

Date = date.today()
print(Date)
time = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
time.send_keys(str(Date))

Next1 = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
Next1.click()


Name =

'Michelle'
Nama = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
Nama.send_keys(Name)

Absen = '10'
Absent = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
Absent.send_keys(Absen)

web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()

import time
time.sleep(1)

web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('Sehat')
web.find_element('xpath', '//*[@id="i12"]/div[3]/div').click()
web.find_element('xpath', '//*[@id="i22"]/div[3]/div').click()
web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('Di rumah dan sekolah')
web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('36')
web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
