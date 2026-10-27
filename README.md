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

I initiated this project to connect the mathematics and numerical computing I have been learning in Engineering Physics with a practical problem in quantitative finance. I defined the learning goals and helped shape the analytical scope, focusing on the mathematical assumptions behind the price model, probability distributions, Monte Carlo estimation, statistical uncertainty and the interpretation of option values and risk measures.

I also set requirements for mathematical explanations suited to my physics background, readable NumPy-based code, reproducible calculations and clear visualisations. I gave feedback on the scope, coding style and presentation of the results as the project developed.

I worked with AI on the initial Python implementation to accelerate prototyping, while using the project to develop the skills to build similar models independently.
