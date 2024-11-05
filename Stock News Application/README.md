# Stock and News Notifier
This Python script tracks stock price changes for a specified company (e.g., Tesla Inc.) and retrieves related news articles if the stock price fluctuates significantly. It fetches the last two days' closing prices, calculates the difference, and, if the change exceeds a set threshold, displays a summary of the latest news.

## Features
- Fetches stock data using the Alpha Vantage API.
- Calculates the percentage change between the last two closing prices.
- Detects significant price fluctuations and displays an alert.
- Retrieves and displays the latest news articles related to the company if the change is significant.

## Requirements
- Python 3.x
- Alpha Vantage API key for stock data
- NewsAPI key for fetching relevant news

## Code Explanation
The code performs the following steps:

1. **API Setup**:

- Defines the Alpha Vantage and NewsAPI endpoints.
- Initializes parameters and API keys to fetch stock data and news.

2. **Fetch Stock Data**:

- Sends a GET request to Alpha Vantage using the specified stock symbol (TSLA).
- Retrieves the closing prices for the last two days to calculate the price change.

3. **Calculate Price Change**:

- Compares the closing prices of the two most recent days.
- Calculates the difference and sets an emoji indicator (⬆️ for an increase, ⬇️ for a decrease).
- Computes the percentage change and rounds it.

4. **Check for Significant Change**:

- If the price change is greater than 5%, it triggers a request to NewsAPI.

5. **Fetch and Display News**:

- Retrieves the top 3 news articles related to the company.
- Formats and displays the stock ticker, percentage change, headline, and summary for each article.

## Enjoy Learning!!