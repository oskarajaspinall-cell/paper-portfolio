## Monte Carlo — EOG (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 144.21 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 27.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.17 | +0.0% | 14.3% |
| IEF | -1.00 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 158 | +9.6% | ±4% |
| base | 45% | 145 | +0.5% | ±0% |
| bear | 30% | 119 | -17.5% | ±8% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings surprise (quarterly release) | 100% | -9.4% | week of 2026-08-03 (-9.4%) |
| CFO transition execution risk | 100% | -5.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.6% | -0.8% | -13.7% | -6.2% | +4.8% | +13.1% | 54% |
| 6m | -1.5% | -1.9% | -20.8% | -10.0% | +6.5% | +19.2% | 56% |
| 12m | -2.6% | -3.7% | -32.1% | -15.8% | +9.4% | +29.9% | 58% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.7% | +942.0% | -943.7% | +0.0% |
| 6m | +1.5% | +1883.6% | -1887.3% | +0.0% |
| 12m | +3.0% | +3766.9% | -3774.7% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -2.6% | 58% |
| bull +10pp / bear -10pp | +0.1% | 52% |
| bull -10pp / bear +10pp | -5.3% | 63% |
| residual vol -25% | -2.6% | 57% |
| residual vol +25% | -2.6% | 58% |

Reconciliation: 12m mean -2.61% vs probability-weighted target -2.61%. Every input is cited in the parameters file. A distribution, not a signal.
