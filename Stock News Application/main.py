import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

sTOCK_API_KEY="SUQOU9U390QLM5YJ";
NEWS_API_KEY="873cfa02b86e4f38a5d5e01114cf1ab5"


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


#diff=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
diff=(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(diff)
emoji=None
if diff>0:
    emoji="⬆️"
else: 
    emoji="⬇️"

diff_percentage=round(diff/float(yesterday_closing_price))*100
print(diff_percentage)

if diff>5:
    #print("news")
    news_param={
       # "q":STOCK_NAME,
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME

    }
    response=requests.get(NEWS_ENDPOINT,params=news_param)
    article=response.json()["articles"]
    #print(article)

    

three_article=article[:3]
#print(three_article)


f_article=[f"{STOCK_NAME}:{emoji}{diff_percentage}% \nHeadline: {article['title']}.  \nBrief:{article['description']}" for article in three_article]

print(f_article)






