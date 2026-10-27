# Mathematical notes

For terminal prices, this experiment assumes a lognormal model:
`S_T = S_0 exp((a - sigma^2/2)T + sigma sqrt(T) Z)`, with `Z ~ N(0,1)`.

For option pricing we use `a=r` (risk-neutral valuation); for a separate hypothetical investment-loss experiment we use `a=mu`. The discounted call payoff is `exp(-rT) max(S_T-K,0)`.

The Monte Carlo price is the sample mean of discounted payoffs. Its estimated standard error is the sample standard deviation divided by the square root of the number of independent draws. A rough 95% interval is mean +/- 1.96 standard errors.

**Antithetic sampling:** average the two payoffs obtained from `Z` and `-Z`. Each pair gives one independent observation.

**Delta:** approximate the partial derivative of call price with respect to `S0` using a symmetric finite difference with *the same random draws* for the up/down cases.

**Risk:** define a one-year loss `L = S0-S_T` under the hypothetical drift `mu`. The 95% VaR is the 95th percentile of the losses; Expected Shortfall is the mean loss at or above that threshold.

These are model-based examples, not a fit to historical data. No stochastic differential equation or Ito calculus is needed to reproduce the chosen terminal-price distribution.
