"""Simple numerical checks for the Monte Carlo experiment."""
import numpy as np
from monte_carlo import terminal_price, discounted_call, black_scholes, estimate, S0, K, T

z = np.zeros(10)
assert np.all(terminal_price(S0,0,0,T,z) == S0)
assert np.all(discounted_call(z) >= 0)
price, delta = black_scholes()
assert 0 < price < S0
assert 0 < delta < 1
mean, error = estimate(np.array([1.,2.,3.,4.]))
assert abs(mean-2.5) < 1e-12
assert error > 0
print("Numerical checks passed.")
