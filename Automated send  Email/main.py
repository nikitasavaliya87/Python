import smtplib

my_email="n270920161987@gmail.com"
#password="n123456789*"
password="daop zima aeoc xfb"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="n270920161987@gmail.com",
        msg="Subject:Hello\n\n this is body of my email. "
        )
    #connection.close()