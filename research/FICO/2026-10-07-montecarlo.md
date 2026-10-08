## Monte Carlo — FICO (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 695.46 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.16; residual vol 52.6% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.27 | +0.0% | 14.3% |
| IEF | +1.24 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 990 | +42.4% | ±2% |
| base | 45% | 705 | +1.4% | ±13% |
| bear | 35% | 505 | -27.4% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| FHFA mortgage-pricing simplification / VantageScore displacement shock | 60% | -23.4% | week of 2026-09-28 (-23.4%) |
| Quarterly earnings reaction (next: 2026-11-04) | 76% | -9.2% | week of 2026-07-27 (-9.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.8% | -3.8% | -40.9% | -20.0% | +15.3% | +48.3% | 55% |
| 6m | -1.5% | -8.7% | -55.1% | -30.8% | +19.5% | +74.0% | 59% |
| 12m | -0.5% | -16.3% | -70.3% | -44.9% | +25.2% | +123.0% | 62% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -1.6% | +6.2% | -9.4% | +0.1% |
| 6m | -3.2% | +12.4% | -19.2% | +0.0% |
| 12m | -6.2% | +24.8% | -38.3% | +0.6% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -0.5% | 62% |
| bull +10pp / bear -10pp | +6.5% | 58% |
| bull -10pp / bear +10pp | -7.5% | 66% |
| residual vol -25% | -0.5% | 60% |
| residual vol +25% | -0.5% | 65% |

Reconciliation: 12m mean -0.50% vs probability-weighted target -0.50%. Every input is cited in the parameters file. A distribution, not a signal.
