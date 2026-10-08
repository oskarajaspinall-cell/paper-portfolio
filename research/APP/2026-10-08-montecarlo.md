## Monte Carlo — APP (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 281.29 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.31; residual vol 62.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +2.99 | +0.0% | 14.3% |
| IEF | -1.32 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 492.26 | +75.0% | ±6% |
| base | 45% | 281.29 | +0.0% | ±0% |
| bear | 30% | 212.13 | -24.6% | ±5% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| AI-claims securities/regulatory litigation shock | 50% | -20.0% | none (stated assumption) |
| Q3 2026 earnings surprise (Nov 4, 2026) | 98% | -12.4% | week of 2026-08-03 (-12.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.3% | -5.6% | -50.5% | -27.2% | +22.3% | +75.8% | 56% |
| 6m | +3.0% | -11.5% | -65.1% | -39.2% | +28.6% | +118.2% | 59% |
| 12m | +11.4% | -20.9% | -79.5% | -54.7% | +36.7% | +208.4% | 61% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +1.3% | +9.3% | -16.8% | +0.1% |
| 6m | +2.4% | +18.6% | -33.6% | +0.0% |
| 12m | +5.6% | +37.2% | -66.8% | +0.7% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +11.4% | 61% |
| bull +10pp / bear -10pp | +21.3% | 57% |
| bull -10pp / bear +10pp | +1.4% | 66% |
| residual vol -25% | +11.4% | 58% |
| residual vol +25% | +11.4% | 64% |

Reconciliation: 12m mean +11.37% vs probability-weighted target +11.37%. Every input is cited in the parameters file. A distribution, not a signal.
