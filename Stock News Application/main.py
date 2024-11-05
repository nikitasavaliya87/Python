import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

sTOCK_API_KEY="SUQOU9U390QLM5YJ";
NEWS_API_KEY="873cfa02b86e4f38a5d5e01114cf1ab5"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_param={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":sTOCK_API_KEY,

}
response=requests.get(STOCK_ENDPOINT,params=stock_param)
#print(response.json())
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
#print(data_list[0])
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)



day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


diff=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(diff)


diff_percentage=(diff/float(yesterday_closing_price))*100

if diff>5:
    #print("news")
    news_param={
       # "q":STOCK_NAME,
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME

    }
    response=requests.get(NEWS_ENDPOINT,params=news_param)
    article=response.json()["articles"]
    print(article)

    

three_article=article[:3]
print(three_article)





    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

