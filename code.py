import pandas as pd
import pandas_datareader as dr
from matplotlib import pyplot as plt

Title=input("Enter name of the stock: ")
stock_ticker = input("Enter the Stock ticker symbol: ")

#Error Handling
try:
    df = dr.data.get_data_yahoo(stock_ticker, start="2010-10-01")
    df["Adj Close"].plot(figsize=(20,7), title = Title);
    plt.legend()
except:
    print("Please check the ticker symbol again!!!!")
