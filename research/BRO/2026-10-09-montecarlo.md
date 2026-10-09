## Monte Carlo — BRO (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 63.75 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 28.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.38 | +0.0% | 14.3% |
| IEF | +0.42 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 74.85 | +17.4% | ±25% |
| base | 45% | 67.05 | +5.2% | ±22% |
| bear | 30% | 54.0 | -15.3% | ±18% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings confirms organic decline | 35% | -12.6% | week of 2026-04-27 (-12.6%) |
| Debt-funded M&A announcement reaction | 60% | -8.3% | week of 2022-03-07 (-8.3%) |
| Captive-tax (IRS Section 831(b)) / Oxford litigation ruling | 10% | -12.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.5% | -0.4% | -20.3% | -8.5% | +7.5% | +19.2% | 51% |
| 6m | -0.3% | -1.2% | -30.5% | -13.9% | +12.2% | +32.6% | 52% |
| 12m | +2.1% | -2.1% | -45.9% | -22.1% | +21.9% | +63.9% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +3.0% | -3.9% | +0.0% |
| 6m | -0.9% | +6.4% | -7.8% | +0.0% |
| 12m | -1.7% | +13.3% | -15.4% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.1% | 53% |
| bull +10pp / bear -10pp | +5.4% | 48% |
| bull -10pp / bear +10pp | -1.2% | 57% |
| residual vol -25% | +2.1% | 52% |
| residual vol +25% | +2.1% | 54% |

Reconciliation: 12m mean +2.09% vs probability-weighted target +2.09%. Every input is cited in the parameters file. A distribution, not a signal.
