## Monte Carlo — TFC (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 46.18 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.33; residual vol 23.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.06 | +0.0% | 14.3% |
| IEF | +0.57 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 55.42 | +20.0% | ±9% |
| base | 45% | 47.05 | +1.9% | ±14% |
| bear | 35% | 37.69 | -18.4% | ±16% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction (Oct 16, 2026) | 20% | -8.8% | week of 2022-01-18 (-8.8%) |
| Regional-bank deposit-funding-cost / credit-spread shock | 20% | -21.3% | week of 2023-03-13 (-21.3%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.9% | -1.3% | -21.8% | -9.4% | +7.2% | +21.0% | 54% |
| 6m | -1.6% | -3.0% | -31.3% | -15.2% | +10.4% | +32.5% | 56% |
| 12m | -1.6% | -5.8% | -45.1% | -24.0% | +16.5% | +57.0% | 58% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.7% | +0.9% | -2.0% | +0.0% |
| 6m | -1.5% | +1.9% | -4.0% | +0.0% |
| 12m | -2.8% | +3.8% | -7.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -1.6% | 58% |
| bull +10pp / bear -10pp | +2.3% | 52% |
| bull -10pp / bear +10pp | -5.4% | 62% |
| residual vol -25% | -1.6% | 56% |
| residual vol +25% | -1.6% | 59% |

Reconciliation: 12m mean -1.59% vs probability-weighted target -1.59%. Every input is cited in the parameters file. A distribution, not a signal.
