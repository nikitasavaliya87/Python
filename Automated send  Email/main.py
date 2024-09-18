#basic code for send email
#import smtplib

# my_email="n270920161987@gmail.com"
# #password="n123456789*"
# password="daop zima aeoc xfbq"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="n270920161987@gmail.com",
#         msg="Subject:Hello\n\n this is body of my email. ")
#     #connection.close()


#basics of date time Module
# import datetime as dt
# now=dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()  # no of day starts from Monday as 0
# print(day_of_week)

# birthday=dt.datetime(year=1987,month=12,day=17)
# print(birthday)

#Randomly select quotes from quotes.txt by date
# import smtplib
# import datetime as dt
# import random

# my_email="n270920161987@gmail.com"

# password="daop zima aeoc xfb"

# now=dt.datetime.now()
# weekday=now.weekday()
# if weekday==2:
#     with open("C:/Users/nikit/OneDrive/Desktop/github/python/Automated send  Email/quotes.txt") as file:
#         all=file.readlines()
#         quotes=random.choice(all)
#     print(quotes)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(my_email,password)
#         connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg=f"Subject:Tueday Motivation\n\n {quotes} ")
#     #connection.close()

from datetime import datetime
import pandas
import random
import smtplib

today=datetime.now()
today_tuple=(today.month, today.day)
my_email="n270920161987@gmail.com"

password="daop zima aeoc xfb" #q

data=pandas.read_csv("Automated send  Email/data/birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for(index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"Automated send  Email/data/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents= letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
         from_addr=my_email,
         to_addrs=birthday_person["email"],
         msg=f"Subject:Happy Birthday!!\n\n {contents} ")

