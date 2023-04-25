import re
import pandas as pd
from parsel import Selector
# from time import sleep
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()

driver = webdriver.Chrome(options=opts, executable_path='chromedriver')

# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field
    if field:
        pass
    # if field is not present print text else:
    else:
        field = "No results"
    return field

# driver.get method() will navigate to a page given by th url address
driver.get("https://www.linkedin.com")

username = driver.find_element(By.ID, 'session_key')
username.send_keys('patricklboll@gmail.com')

time.sleep(0.5)

password = driver.find_element(By.ID, 'session_password')
password.send_keys('molly123')

time.sleep(0.5)

sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

sign_in_button.click()
time.sleep(15)

Jobdata = []
lnks = []


# this for loop doesn't make sense to me, range(0,20,10) outputs 0 and 10. It outputs two numbers which makes the script 
# run twice, that's why I'm getting two of my results
'''
for x in range (0,20,10):
    driver.get(f'https://www.google.com/search?q=site%3Alinkedin.com+AND+%22Python+Developer%22+AND+%22New+York%22+%40gmail.com&sxsrf=APwXEdcEmArnht7VKgj6GdyF8oR_dkIfvA%3A1679991103615&ei=P6EiZK2YJeHIkPIP2tK-oAM&ved=0ahUKEwjts9PHlv79AhVhJEQIHVqpDzQQ4dUDCBA&uact=5&oq=site%3Alinkedin.com+AND+%22Python+Developer%22+AND+%22New+York%22+%40gmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVCSB1jZH2CGI2gBcAB4AIABiAGIAaILkgEEMC4xMZgBAKABAcABAQ&sclient=gws-wiz-serp#ip=1')
    # I got the above link by typing this into Google: site:linkedin.com AND "Python Developer" AND "New York" @gmail.com
               
    time.sleep(random.uniform(2.5, 4.9))
    linkedin_urls = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
    lnks.append(linkedin_urls)
    '''
    

driver.get(f'https://www.google.com/search?q=site%3Alinkedin.com+AND+%22Python+Developer%22+AND+%22New+York%22+%40gmail.com&sxsrf=APwXEdcEmArnht7VKgj6GdyF8oR_dkIfvA%3A1679991103615&ei=P6EiZK2YJeHIkPIP2tK-oAM&ved=0ahUKEwjts9PHlv79AhVhJEQIHVqpDzQQ4dUDCBA&uact=5&oq=site%3Alinkedin.com+AND+%22Python+Developer%22+AND+%22New+York%22+%40gmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVCSB1jZH2CGI2gBcAB4AIABiAGIAaILkgEEMC4xMZgBAKABAcABAQ&sclient=gws-wiz-serp#ip=1')
# I got the above link by typing this into Google: site:linkedin.com AND "Python Developer" AND "New York" @gmail.com


# This loop scrolls down the google page so more links can be selected
# Make the 4 higher to get more links, lower to get less
j = 0
while j < 4:
    time.sleep(random.uniform(2.5, 4.9))
    driver.execute_script("window.scrollBy(0,1000)","")
    time.sleep(random.uniform(2.5, 4.9))
    j += 1

linkedin_urls = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
lnks.append(linkedin_urls)
    
for x in lnks:
    for i in x:
        
        # get the profile URL
        driver.get(i)
        time.sleep(random.uniform(2.5, 4.9))
        
        # Assigning the source code from the source code to the variable sel
        sel = Selector(text=driver.page_source)
               
        # XPATH to extract the class from the text containing the name
        name = sel.xpath('//*[starts-with(@class, "text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()
        
        if name:
            name = name.strip()
               
        job_title = sel.xpath('//*[starts-with(@class, "text-body-medium break-words")]/text()').extract_first()
        
        if job_title:
            job_title = job_title.strip()
        
        try:
            # xpath to extract the text from the class containing the college
            company = driver.find_element(By.XPATH, '//ul[@class="pv-text-details_right-panel"]').text
        
        except:
            company = "None"
            
        if company:
            company = company.strip()
            
        location = sel.xpath('//*[starts-with(@class, "text-body-small inline t-black--light break-words")]/text()').extract_first()
        
        if location:
               location = location.strip()
                
        # Code to find the email
        page_source = driver.page_source

        EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

        list_of_emails = []

        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.append(re_match.group())
       
    
        
        # Validating if the fields exist on the profile
        name = validate_field(name)
        job_title = validate_field(job_title)
        company = validate_field(company)
        # college = validate_field(college)
        location = validate_field(location)
        # linkedin_url = validate_field(linkedin_url)
        list_of_emails = validate_field(list_of_emails)
        
               
        # Printing the output
        print('\n')
        print('Name: ' + name)
        print('Job Title: ' + job_title)
        print('Company: ' + company)
        print('Location: ' + location)
        for i in range(len(list_of_emails)):
            print('Email: ' + list_of_emails[i])
        # print('URL: ' + linkedin_url)
        print('\n')
               
        data = {
            'Name' : name,
            'Job Title' : job_title,
            'Company' : company,
            'Location' : location, 
            # 'URL' : linkedin_url
            'Email' : list_of_emails,
        }
        Jobdata.append(data)

df = pd.DataFrame(Jobdata)
df.to_csv('Jobdata_linkedin.csv')


# Terminated the application
driver.quit()   
               
