## Monte Carlo — CI (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 281.03 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.03; residual vol 28.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.22 | +0.0% | 14.3% |
| IEF | +0.52 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 30% | 365.44 | +30.0% | ±27% |
| base | 50% | 298.47 | +6.2% | ±27% |
| bear | 20% | 239.51 | -14.8% | ±27% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Medical-cost-ratio / earnings shock | 40% | -19.0% | week of 2025-10-27 (-19.0%) |
| PBM reform / regulatory shock | 40% | -11.3% | week of 2024-12-09 (-11.3%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.2% | +2.1% | -22.7% | -7.6% | +10.2% | +22.8% | 44% |
| 6m | +3.0% | +2.6% | -33.8% | -12.7% | +17.8% | +41.9% | 45% |
| 12m | +9.2% | +4.5% | -51.5% | -20.9% | +33.9% | +86.0% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +4.4% | -4.2% | +0.0% |
| 6m | +0.0% | +8.8% | -8.6% | +0.0% |
| 12m | +0.0% | +17.6% | -17.1% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +9.2% | 46% |
| bull +10pp / bear -10pp | +13.6% | 41% |
| bull -10pp / bear +10pp | +4.7% | 50% |
| residual vol -25% | +9.2% | 45% |
| residual vol +25% | +9.2% | 46% |

Reconciliation: 12m mean +9.16% vs probability-weighted target +9.16%. Every input is cited in the parameters file. A distribution, not a signal.
