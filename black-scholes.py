import numpy as np
import scipy.stats as scipy


def d1(S0, K, T, r, sigma):
    return (np.log(S0/K) + T * (r + 0.5 * sigma ** 2)) / (sigma * np.sqrt(T))


def d2(S0, K, T, r, sigma):
    D1 = d1(S0, K, T, r, sigma)
    return D1 - sigma * np.sqrt(T)


def BLACKSCHOLES(opt, S0, K, T, r, sigma):
    if opt == "CALL":
        return S0 * scipy.norm.cdf(d1(S0, K, T, r, sigma)) - K * np.exp(-r * T) * scipy.norm.cdf(d2(S0, K, T, r, sigma))
    elif opt == "PUT":
        return K * np.exp(-r * T) * scipy.norm.cdf(-d2(S0, K, T, r, sigma)) - S0 * scipy.norm.cdf(-d1(S0, K, T, r, sigma))


S0 = 100.0
K = 100.0
r = 0.05
sigma = 0.1
T = 10
opt = "CALL"

print("Stock price: ", S0)
print("Strike price: ", K)
print("Risk-free rate: ", r)
print("Volatility: ", sigma)
print("Time to expiration: ", T)
print("Option Type: ", opt)

price = BLACKSCHOLES(opt, S0, K, T, r, sigma)
print("Price according to Black-Scholes Model: ", price)
