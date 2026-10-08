## Monte Carlo — MCD (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 230.88 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.14; residual vol 15.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.27 | +0.0% | 14.3% |
| IEF | +0.78 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 310.7 | +34.6% | ±2% |
| base | 45% | 234.16 | +1.4% | ±7% |
| bear | 35% | 213.73 | -7.4% | ±8% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| AI-pricing antitrust class action | 25% | -15.0% | none (stated assumption) |
| Q3 2026 earnings miss amid weakening US traffic | 100% | -3.8% | week of 2026-05-04 (-3.8%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.0% | +1.1% | -11.8% | -3.4% | +5.8% | +13.1% | 43% |
| 6m | +2.1% | +1.3% | -17.5% | -5.8% | +9.7% | +23.6% | 45% |
| 12m | +5.0% | +1.7% | -25.5% | -10.1% | +16.8% | +47.1% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +246.5% | -245.2% | +0.0% |
| 6m | -1.2% | +492.9% | -490.5% | +0.0% |
| 12m | -2.3% | +985.8% | -980.9% | +0.1% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.0% | 46% |
| bull +10pp / bear -10pp | +9.2% | 39% |
| bull -10pp / bear +10pp | +0.8% | 53% |
| residual vol -25% | +5.0% | 46% |
| residual vol +25% | +5.0% | 46% |

Reconciliation: 12m mean +4.95% vs probability-weighted target +4.95%. Every input is cited in the parameters file. A distribution, not a signal.
