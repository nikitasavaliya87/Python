import smtplib

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


import datetime as dt
now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()  # no of day starts from Monday as 0
print(day_of_week)

birthday=dt.datetime(year=1987,month=12,day=17)
print(birthday)
