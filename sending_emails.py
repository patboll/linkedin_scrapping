import win32com.client as win32

# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**
# **YOU HAVE TO HAVE THE OUTLOOK APP OPEN ON YOUR LAPTOP WHEN YOU RUN THIS SCRIPT FOR IT TO WORK**

olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

mail_item = olApp.CreateItem(0)

mail_item.Subject = "You're Fired!"
mail_item.BodyFormat = 1
mail_item.Body = "Hey Pat, you're a shitty employee and you're fired"
mail_item.Sender = 'dev@datatouches.com'
mail_item.To = 'patricklboll@gmail.com'
mail_item.Display()
mail_item.Save()
mail_item.Send()
