import numpy as np
from scipy.stats import norm

S0, K, r, mu, sigma, T, N = 100., 105., .03, .07, .20, 1., 50000

def terminal_price(s0, drift, sigma, t, z):
    return s0 * np.exp((drift - sigma**2 / 2) * t + sigma * np.sqrt(t) * z)

def discounted_call(z, s0=S0):
    st = terminal_price(s0, r, sigma, T, z)
    return np.exp(-r*T) * np.maximum(st-K, 0)

def black_scholes():
    d1 = (np.log(S0/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    return S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2), norm.cdf(d1)

def estimate(x):
    return np.mean(x), np.std(x,ddof=1)/np.sqrt(len(x))

def run():
    rng = np.random.default_rng(42)
    z = rng.standard_normal(N)
    price, error = estimate(discounted_call(z))
    exact, delta_exact = black_scholes()
    h = .1
    delta = (np.mean(discounted_call(z,S0+h))-
             np.mean(discounted_call(z,S0-h)))/(2*h)
    half = rng.standard_normal(N//2)
    pairs = (discounted_call(half)+discounted_call(-half))/2
    anti, anti_se = estimate(pairs)
    st = terminal_price(S0,mu,sigma,T,rng.standard_normal(N))
    losses = S0-st
    var = np.quantile(losses,.95)
    es = np.mean(losses[losses>=var])
    print(f"Monte Carlo: {price:.4f} (SE {error:.4f})")
    print(f"Black-Scholes: {exact:.4f}")
    print(f"Antithetic: {anti:.4f} (SE {anti_se:.4f})")
    print(f"Delta: {delta:.4f} (analytical {delta_exact:.4f})")
    print(f"95% VaR: {var:.4f}; Expected Shortfall: {es:.4f}")
    return z,st,losses,price,exact,var,es

if __name__=="__main__":
    run()
