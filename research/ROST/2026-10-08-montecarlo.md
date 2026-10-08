## Monte Carlo — ROST (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 225.53 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.16; residual vol 22.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.62 | +0.0% | 14.3% |
| IEF | +0.42 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 250.9 | +11.2% | ±9% |
| base | 45% | 225.5 | -0.0% | ±5% |
| bear | 30% | 201.6 | -10.6% | ±10% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings print reaction (2026-11-19) | 18% | -21.9% | week of 2022-05-16 (-21.9%) |
| Real yield shock / multiple de-rating | 80% | -8.6% | week of 2025-03-10 (-8.6%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.3% | -0.0% | -19.8% | -7.6% | +7.5% | +18.0% | 50% |
| 6m | -0.6% | -1.0% | -27.8% | -12.0% | +10.5% | +27.7% | 52% |
| 12m | -0.4% | -2.9% | -38.2% | -18.4% | +15.3% | +45.0% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +4.3% | -4.9% | +0.0% |
| 6m | -0.9% | +8.7% | -9.9% | +0.0% |
| 12m | -1.7% | +17.3% | -19.6% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -0.4% | 55% |
| bull +10pp / bear -10pp | +1.8% | 51% |
| bull -10pp / bear +10pp | -2.6% | 58% |
| residual vol -25% | -0.4% | 53% |
| residual vol +25% | -0.4% | 56% |

Reconciliation: 12m mean -0.38% vs probability-weighted target -0.38%. Every input is cited in the parameters file. A distribution, not a signal.
