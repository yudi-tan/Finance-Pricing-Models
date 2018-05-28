import pandas as pd
import scipy.stats as scipy

tsla = pd.read_csv("TSLA.csv", parse_dates=True, index_col="Date")
sp = pd.read_csv("^GSPC.csv", parse_dates=True, index_col="Date")

prices = pd.concat([tsla['Close'], sp['Close']], axis=1)
prices.columns = ['TSLA', '^GSPC']

returns = prices.pct_change(1)
# drop first row
returns = returns.dropna(axis=0)

X = returns['^GSPC']
y = returns['TSLA']
slope, intercept, r_value, p_value, std_err = scipy.linregress(X, y)

print(slope)
