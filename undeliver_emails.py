import pandas as pd
import re

#Read csv file
df = pd.read_csv('undelive_email.csv')

#Take the column with  all the email body and combine it into 1 cell
text = " ".join(str(review) for review in df.firstema)

#Extract e-mails into a list
match = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

#Convert the list with the e-mails into a dataframe
newlist = pd.DataFrame(match)

#Rename the column with the e-mails
newlist.columns = ['email']

#Drop duplicate e-mails
dfclean = newlist.drop_duplicates(subset='email', keep='first')

#Clean unwanted e-mails
#The list will contain the e-mail address used to send the original e-mails
# i.e. the company e-mail
df1 = dfclean[~dfclean.email.str.contains("tepaper")].copy()
df2 = df1[~df1.email.str.contains("togetherenergy")].copy()
df3 = df2[~df2.email.str.contains("eurprd05.prod")].copy()
df3['email'] = df3['email'].str.lower()

#Write the list of e-mails to a csv file
df3.to_csv('undeliverable_emails.csv', index = False)
