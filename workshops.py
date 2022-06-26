from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import csv 

filename="/home/sreeraj/Desktop/ws_insti.csv"
chromedriver_location="/home/sreeraj/Desktop/chromedriver"
mailid="workshop@shaastra.org"
password=""

fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # fields = next(csvreader)
    for row in csvreader:
        rows.append(row)    


driver = webdriver.Chrome(chromedriver_location)
driver.get("https://app.podia.com/coupons/new")

email='//*[@id="email"]'
passwd='//*[@id="password"]'
login='//*[@id="login"]/div[2]/form/input[2]'

driver.find_element_by_xpath(email).send_keys(mailid)
driver.find_element_by_xpath(passwd).send_keys(password)
driver.find_element_by_xpath(login).click()
ctr=0

for row in rows:
    couponname=row[3]+"_SW"

    #WebDriverWait(driver, timeout=20).until(ec.visibility_of_element_located((By.ID, "coupon_code")))     
    driver.get("https://app.podia.com/coupons/new")

 
    cname='//*[@id="coupon_code"]'
    driver.find_element_by_xpath(cname).send_keys(couponname)

    prodonly='//*[@id="details"]/div[2]/div[2]/div[2]/div[2]/div/div/label'
    WebDriverWait(driver, timeout=60).until(ec.visibility_of_element_located((By.ID, "details"))) 
    driver.find_element_by_xpath(prodonly).click()

    percent='//*[@id="coupon_amount_percentage"]'
    driver.find_element_by_xpath(percent).clear()
    driver.find_element_by_xpath(percent).send_keys("100")

    limit='//*[@id="options"]/div[2]/div[1]/div[2]/div[2]/div[1]/label'
    WebDriverWait(driver, timeout=60).until(ec.visibility_of_element_located((By.ID, "options")))     
    driver.find_element_by_xpath(limit).click()
    limitblank='//*[@id="coupon_usage_limit"]'
    driver.find_element_by_xpath(limitblank).clear()
    driver.find_element_by_xpath(limitblank).send_keys("24")    

    create='/html/body/div[4]/form/div[3]/input[1]'
    driver.find_element_by_xpath(create).click()
    ctr+=1


print(ctr," coupons generated\n")
print("last roll number generated: ",couponname)
print("done! \n program made by Sreeraj")


