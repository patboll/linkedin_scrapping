import win32com.client as win32
import pandas as pd
import time
import random
# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**
# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**

messages = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapping\ChatGPT_messages_2.csv")
df3 = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapping\contact_list_4.csv")

# for i in range(2):
for i in range(len(df3['Name'])):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    # Change the "to" address to the column to loop thru
    # ******** NEXT LINE NEEDS TO BE CHANGED *****
    mail.To = df3['Email'].values[i]
    # mail.To = 'patricklboll@gmail.com'
    mail.Subject = 'Power BI Consulting Services from DataTouches'
    mail.GetInspector

    intro = "Dear " + df3['Name'].values[i] + ','
    line = '<br>'
    message = messages['Message'].values[i]
    closing = 'Thank you,' + '<br>' + "The DataTouches Team"
    index = mail.HTMLbody.find('>', mail.HTMLbody.find('<body'))
    mail.HTMLbody = mail.HTMLbody[:index + 1] + intro + line + line + message + line + line + closing + mail.HTMLbody[index + 1:]
    mail.Display()
    mail.send
    time.sleep(random.uniform(10, 20))
