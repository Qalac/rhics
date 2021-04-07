import requests
from datetime import date, timedelta

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=OFJRQ0NCDVEJLCCB "

time = str(date.today() - timedelta(days=1))

def make_call():
    response = requests.get(url)
    response = response.json()
    return response['Time Series (Daily)'][time]

def resolve():
    results = make_call()
    return results