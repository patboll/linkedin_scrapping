import pandas as pd

df2 = pd.read_csv(r"C:\Users\Patrick\PycharmProjects\Scrapin\Jobdata_linkedin.csv")

# This gets rid of the elements that are just '[]'
df2 = df2[df2.Email != '[]']
# Resets the index so the numbers of deleted rows aren't skipped
df2 = df2.reset_index()

# This for loop gets rid of the first two items in the string (which is [') and
# if there is a second email address it gets rid of it
for i in range(len(df2['Email'])):
    element = df2['Email'].loc[df2.index[i]]
    # gets rid of the first two items in the string
    element = element[2:]
    separator = '.com'
    # Deletes any second email addresses
    element = element.split(separator)[0] + separator
    corrected_element = element
    df2['Email'].loc[df2.index[i]] = corrected_element

# Deleting the rows with 'No Results' as the name
df2 = df2[df2["Name"].str.contains("No results") == False]

# Creates new dataframe that only contains names and emails
df3 = df2.filter(['Name','Email'], axis=1)

df3.to_csv('Jobdata_linkedin_clean.csv')
