import pandas as pd

df4 = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapin\Jobdata_linkedin_clean.csv")

# Creates a loop that prints all the names and emails
for i in range(len(df4['Email'])):
    name = df4['Name'].loc[df4.index[i]]
    email = df4['Email'].loc[df4.index[i]]
    print(f'My name is {name} and my email is {email}')



