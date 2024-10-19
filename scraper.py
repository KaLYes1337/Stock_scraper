import requests
from bs4 import BeautifulSoup
import time
import csv
import yfinance as yf


def get_stock_price(ticker):
    # Construct the Google Finance URL based on the ticker
    url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ"

    # Send a GET request to fetch the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        # Find the stock price using the class for the price element
        try:
            stock_price = soup.find("div", class_="YMlKec fxKbKc").text
            return stock_price
        except AttributeError:
            return "Error: Unable to find stock price"
    else:
        return (
            f"Error: Unable to fetch the webpage (status code: {response.status_code})"
        )


def get_multiple_stock_prices(tickers):
    stock_data = {}

    for ticker in tickers:
        price = get_stock_price(ticker)
        stock_data[ticker] = price
        print(f"{ticker}: {price}")

        # Sleep between requests to avoid hitting rate limits
        time.sleep(2)  # Sleep for 2 seconds between requests

    return stock_data


# Example usage for multiple stocks
tickers = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
stock_prices = get_multiple_stock_prices(tickers)


def save_stock_prices_to_csv(stock_data):
    with open("stock_prices.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Price"])

        for ticker, price in stock_data.items():
            writer.writerow([ticker, price])


# Save stock prices to a CSV
save_stock_prices_to_csv(stock_prices)


def get_stock_prices_yfinance(tickers):
    stock_data = {}

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period="1d")
        stock_data[ticker] = stock_info["Close"][
            0
        ]  # Get the closing price for the latest day

    return stock_data


# Example usage
tickers = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
stock_prices = get_stock_prices_yfinance(tickers)

for ticker, price in stock_prices.items():
    print(f"{ticker}: {price}")
