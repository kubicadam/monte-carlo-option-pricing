# Monte Carlo Option Pricing & Financial Risk Analysis

*Python · NumPy · SciPy · Matplotlib | Student project · Synthetic data*

I initiated this project to connect probability theory and numerical methods from my Engineering Physics studies at Warsaw University of Technology with quantitative finance. It estimates the value of a European call option using Monte Carlo simulation and compares it with the Black–Scholes formula.

## Methods

- 50,000 simulated terminal prices under a lognormal model.
- Monte Carlo convergence, standard error and a 95% confidence interval.
- Antithetic sampling and numerical estimation of option Delta.
- Separate model-based risk analysis: 95% Value at Risk and Expected Shortfall.

Option pricing uses the risk-free rate (`r`); the risk experiment uses an assumed return (`mu`). See [mathematical notes](notes/MATH_NOTES.md).

## Example results

With `S0=100`, `K=105`, `r=3%`, `mu=7%`, `sigma=20%`, `T=1 year`, and a fixed seed:

| Measure | Value |
|---|---:|
| Monte Carlo call price | 7.1485 |
| Black–Scholes benchmark | 7.1281 |
| Monte Carlo standard error | 0.0564 |
| Antithetic standard error | 0.0466 |
| Numerical / analytical Delta | 0.5009 / 0.5024 |
| 95% VaR / Expected Shortfall | 24.5020 / 30.2133 |

The estimated option price is close to the analytical benchmark. Antithetic sampling reduced the estimated standard error in this run. All risk figures depend on hypothetical model assumptions; they are **not market forecasts**.

## Visualisations

![Monte Carlo convergence](results/01_convergence.svg)
![Simulated terminal prices](results/02_final_prices.svg)
![Simulated loss distribution](results/03_risk.svg)
![Illustrative asset-price paths](results/04_paths.svg)

## Run locally

```bash
python -m pip install -r requirements.txt
python monte_carlo.py
python checks.py
python plots.py
```

`plots.py` saves PNG charts in `results/`. See [source code](monte_carlo.py) and [plotting script](plots.py).

## Project development and my contribution

I initiated this project to explore how Python and numerical methods can be applied to a problem in quantitative finance. I helped shape the objectives and requirements, including a focus on NumPy, mathematical explanations suited to my Engineering Physics background, readable code, reproducible examples and clear visualisations. I also gave feedback on the scope, coding style and presentation as the project developed.

I was particularly interested in the mathematical assumptions behind the lognormal price model, the relationship between Monte Carlo estimates and their statistical uncertainty, and comparison with the Black–Scholes benchmark. I wanted the analysis to explain not only the calculated values, but also what Delta, Value at Risk and Expected Shortfall mean under the chosen assumptions.

The initial Python implementation and documentation were developed with AI assistance to accelerate prototyping and support numerical checks.
