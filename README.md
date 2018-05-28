## Black Scholes Model

##### Assumptions

* Only for European Call options
* Constant Volatility across different strike prices
* Constant Dividend and Risk-free rates

##### Inputs

1.  Strike price of option
2.  Current stock price
3.  Time to expiration
4.  Risk-free rate
5.  Volatility

## Capital Asset Pricing Model

##### Assumptions

* Investors always combine risk-free asset with risky assets
* Investors ought to be compensated by purchasing risky assets
* The compensation is usually known as excess market return / market premium for the given level of risk, Beta.
* Beta is calculated as Cov(stock, mkt) / Var(mkt)

##### Notes

Rf = Risk-free Rate
Mkt Premium = Mkt return - Rf
CAPM Formula: Return = Rf + Beta \* Mkt Premium

Since the formula is relatively straightforward, in CAPM.py, we'll attempt to calculate Beta using Linear Regression.
