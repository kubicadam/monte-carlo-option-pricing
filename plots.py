"""Generate four plots from the Monte Carlo numerical experiment."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from monte_carlo import run, discounted_call, terminal_price, S0, mu, sigma, T

z, prices, losses, estimate, exact, var, es = run()
out = Path("results")
out.mkdir(exist_ok=True)

payoffs = discounted_call(z)
running = np.cumsum(payoffs) / np.arange(1, len(payoffs) + 1)
sample_sizes = np.arange(200, len(payoffs)+1, 200)
plt.figure(figsize=(8, 4.5))
plt.plot(sample_sizes, running[sample_sizes-1], label="Monte Carlo")
plt.axhline(exact, color="black", linestyle="--", label="Black-Scholes")
plt.xlabel("Number of samples")
plt.ylabel("Call price")
plt.title("Convergence")
plt.legend()
plt.tight_layout()
plt.savefig(out / "01_convergence.png")
plt.close()

plt.figure(figsize=(8, 4.5))
plt.hist(prices, bins=60, density=True)
plt.xlabel("Final price")
plt.title("Simulated final prices")
plt.tight_layout()
plt.savefig(out / "02_final_prices.png")
plt.close()

plt.figure(figsize=(8, 4.5))
plt.hist(losses, bins=60, density=True)
plt.axvline(var, color="darkred", label="95% VaR")
plt.axvline(es, color="black", linestyle="--", label="95% ES")
plt.xlabel("Loss (negative means gain)")
plt.title("Simulated investment losses")
plt.legend()
plt.tight_layout()
plt.savefig(out / "03_risk.png")
plt.close()

rng = np.random.default_rng(2027)
steps = 252
dt = T/steps
increments = (mu-sigma**2/2)*dt + sigma*np.sqrt(dt)*rng.standard_normal((25,steps))
paths = S0*np.exp(np.cumsum(increments,axis=1))
paths = np.column_stack((np.full(25,S0),paths))
plt.figure(figsize=(8, 4.5))
plt.plot(np.linspace(0,T,steps+1), paths.T,alpha=.5)
plt.xlabel("Time (years)")
plt.ylabel("Price")
plt.title("25 sample paths")
plt.tight_layout()
plt.savefig(out / "04_paths.png")
plt.close()
print("Saved four figures to results/")
