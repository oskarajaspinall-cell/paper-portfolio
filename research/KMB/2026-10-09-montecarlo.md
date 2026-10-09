## Monte Carlo — KMB (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 97.74 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 21.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.15 | +0.0% | 14.3% |
| IEF | +0.64 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 127.37 | +30.3% | ±7% |
| base | 50% | 97.75 | +0.0% | ±21% |
| bear | 30% | 66.95 | -31.5% | ±21% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Kenvue deal EU antitrust decision / M&A completion shock | 20% | -13.2% | week of 2025-11-03 (-13.2%) |
| Quarterly earnings reaction | 100% | -7.8% | week of 2025-04-21 (-7.8%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.7% | -1.4% | -18.3% | -8.5% | +5.2% | +14.2% | 55% |
| 6m | -2.9% | -2.9% | -30.8% | -15.3% | +9.7% | +25.0% | 56% |
| 12m | -3.4% | -5.9% | -50.0% | -27.2% | +19.3% | +49.6% | 56% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.5% | +513.3% | -515.2% | +0.0% |
| 6m | -0.9% | +1026.7% | -1030.3% | +0.0% |
| 12m | -1.9% | +2053.3% | -2060.6% | +0.1% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -3.4% | 56% |
| bull +10pp / bear -10pp | +2.8% | 47% |
| bull -10pp / bear +10pp | -9.6% | 65% |
| residual vol -25% | -3.4% | 56% |
| residual vol +25% | -3.4% | 57% |

Reconciliation: 12m mean -3.38% vs probability-weighted target -3.38%. Every input is cited in the parameters file. A distribution, not a signal.
