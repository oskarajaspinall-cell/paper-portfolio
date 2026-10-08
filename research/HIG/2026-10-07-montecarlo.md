## Monte Carlo — HIG (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 126.79 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.09; residual vol 20.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.37 | +0.0% | 14.3% |
| IEF | +0.40 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 147.0 | +15.9% | ±8% |
| base | 55% | 127.0 | +0.2% | ±4% |
| bear | 20% | 92.0 | -27.4% | ±14% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release | 20% | -8.0% | week of 2024-10-21 (-8.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.2% | -1.7% | -17.5% | -8.4% | +5.7% | +16.7% | 57% |
| 6m | -1.6% | -2.6% | -26.3% | -12.9% | +8.6% | +26.0% | 56% |
| 12m | -1.4% | -3.3% | -39.5% | -19.5% | +14.4% | +43.4% | 56% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | -1.3% | -0.5% | +0.0% |
| 6m | +0.0% | -2.0% | -0.9% | +0.0% |
| 12m | +0.1% | -3.3% | -1.8% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -1.4% | 56% |
| bull +10pp / bear -10pp | +2.9% | 49% |
| bull -10pp / bear +10pp | -5.7% | 63% |
| residual vol -25% | -1.4% | 53% |
| residual vol +25% | -1.4% | 57% |

Reconciliation: 12m mean -1.41% vs probability-weighted target -1.41%. Every input is cited in the parameters file. A distribution, not a signal.
