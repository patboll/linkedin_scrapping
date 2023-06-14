import win32com.client as win32
import pandas as pd
import time
import random

# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**
# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**

messages = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapping\ChatGPT_messages_2.csv")
df3 = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapping\contact_list_2.csv")

'''
for i in range(len(df3['Name'])):
    mail = df3['Email'].values[i]
    message = messages['Message'].values[i]
    print(mail)
    print(message)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
'''
for i in range(1):
# for i in range(len(df3['Name'])):
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')
    mail_item = olApp.CreateItem(0)
    mail_item.Subject = "Power BI Consulting Services from DataTouches"

    '''
    mail_item.GetInspector
    index = mail_item.HTMLbody.find('>', mail_item.HTMLbody.find('<body'))
    mail_item.HTMLbody = mail_item.HTMLbody[:index + 1] + messages['Message'].values[i] + mail_item.HTMLbody[index + 1:]
    '''
    mail_item.BodyFormat = 1
    mail_item.Body = messages['Message'].values[i]
    mail_item.Sender = 'dev@datatouches.com'
    # Change the "to" address to the column to loop thru
    # ******** NEXT LINE NEEDS TO BE CHANGED *****
    # mail_item.To = df3['Email'].values[i]
    mail_item.To = 'patricklboll@gmail.com'
    mail_item.Display()
    mail_item.Save()
    mail_item.Send()
    time.sleep(random.uniform(10, 20))

