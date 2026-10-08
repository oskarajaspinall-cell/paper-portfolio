## Monte Carlo — WDAY (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 184.26 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.15; residual vol 43.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.08 | +0.0% | 14.3% |
| IEF | -0.07 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 247.4 | +34.3% | ±15% |
| base | 50% | 196.07 | +6.4% | ±19% |
| bear | 30% | 156.64 | -15.0% | ±23% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction | 76% | -14.3% | week of 2024-05-20 (-14.3%) |
| Securities-fraud investigation solicitation | 15% | -8.0% | none (stated assumption) |
| Additional restructuring/layoff disclosure | 25% | -5.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.6% | -1.0% | -31.5% | -14.6% | +13.7% | +38.4% | 52% |
| 6m | +1.6% | -2.7% | -43.8% | -21.7% | +19.9% | +62.0% | 54% |
| 12m | +5.6% | -4.9% | -58.7% | -31.7% | +30.0% | +105.6% | 54% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.1% | +4.4% | -6.2% | +0.1% |
| 6m | +0.1% | +8.9% | -12.6% | +0.0% |
| 12m | +0.4% | +17.7% | -24.9% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.6% | 54% |
| bull +10pp / bear -10pp | +10.5% | 50% |
| bull -10pp / bear +10pp | +0.6% | 58% |
| residual vol -25% | +5.6% | 51% |
| residual vol +25% | +5.6% | 57% |

Reconciliation: 12m mean +5.56% vs probability-weighted target +5.56%. Every input is cited in the parameters file. A distribution, not a signal.
