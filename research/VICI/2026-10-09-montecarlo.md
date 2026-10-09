## Monte Carlo — VICI (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 22.79 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.22; residual vol 16.6% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.31 | +0.0% | 14.3% |
| IEF | +1.08 | -6.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 33.78 | +48.2% | ±16% |
| base | 45% | 25.5 | +11.9% | ±16% |
| bear | 35% | 19.4 | -14.9% | ±16% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction (Q3 2026, reports Oct 28, 2026) | 19% | -3.9% | week of 2025-10-27 (-3.9%) |
| Caesars/MGM tenant-concentration credit or rent-coverage shock | 5% | -18.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.2% | +0.8% | -13.3% | -5.0% | +7.2% | +17.0% | 47% |
| 6m | +3.4% | +2.0% | -21.4% | -8.6% | +13.9% | +32.8% | 45% |
| 12m | +9.8% | +4.8% | -34.5% | -14.1% | +29.1% | +71.8% | 44% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -1.6% | +2.9% | -0.5% | +0.0% |
| 6m | -3.3% | +6.4% | -1.0% | +0.0% |
| 12m | -6.6% | +13.5% | -2.0% | +0.1% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +9.8% | 44% |
| bull +10pp / bear -10pp | +16.1% | 36% |
| bull -10pp / bear +10pp | +3.5% | 51% |
| residual vol -25% | +9.8% | 44% |
| residual vol +25% | +9.8% | 45% |

Reconciliation: 12m mean +9.79% vs probability-weighted target +9.79%. Every input is cited in the parameters file. A distribution, not a signal.
