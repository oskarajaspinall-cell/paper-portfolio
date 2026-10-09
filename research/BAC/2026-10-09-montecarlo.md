## Monte Carlo — BAC (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 53.61 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.36; residual vol 22.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.13 | +0.0% | 14.3% |
| IEF | -0.05 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 59.66 | +11.3% | ±22% |
| base | 45% | 51.45 | -4.0% | ±19% |
| bear | 35% | 42.54 | -20.6% | ±15% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction | 50% | -6.2% | week of 2022-01-18 (-6.2%) |
| Banking-sector contagion / AOCI stress echo (2023-style) | 60% | -11.4% | week of 2023-03-06 (-11.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -2.4% | -2.8% | -22.6% | -10.8% | +5.9% | +19.0% | 59% |
| 6m | -4.4% | -5.9% | -33.3% | -18.1% | +7.6% | +29.8% | 62% |
| 12m | -6.8% | -11.6% | -49.3% | -28.9% | +10.5% | +51.0% | 65% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +0.7% | -4.0% | +0.0% |
| 6m | +0.0% | +1.5% | -8.0% | +0.0% |
| 12m | +0.2% | +2.9% | -15.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -6.8% | 65% |
| bull +10pp / bear -10pp | -3.6% | 61% |
| bull -10pp / bear +10pp | -10.0% | 69% |
| residual vol -25% | -6.8% | 65% |
| residual vol +25% | -6.8% | 64% |

Reconciliation: 12m mean -6.78% vs probability-weighted target -6.78%. Every input is cited in the parameters file. A distribution, not a signal.
