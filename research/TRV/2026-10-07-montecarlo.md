## Monte Carlo — TRV (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 360.64 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.09; residual vol 21.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.35 | +0.0% | 14.3% |
| IEF | +0.47 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 409 | +13.4% | ±1% |
| base | 45% | 361 | +0.1% | ±3% |
| bear | 30% | 314 | -12.9% | ±3% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings — adverse reserve development or elevated catastrophe losses | 20% | -6.0% | week of 2022-04-18 (-6.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.3% | -0.8% | -17.5% | -7.7% | +7.0% | +18.7% | 53% |
| 6m | -0.5% | -1.8% | -25.1% | -11.6% | +9.5% | +27.4% | 54% |
| 12m | -0.5% | -3.2% | -34.5% | -17.5% | +13.5% | +42.9% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | -0.6% | -0.4% | +0.0% |
| 6m | +0.0% | -1.1% | -0.7% | +0.0% |
| 12m | +0.1% | -2.3% | -1.4% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -0.5% | 55% |
| bull +10pp / bear -10pp | +2.2% | 51% |
| bull -10pp / bear +10pp | -3.1% | 60% |
| residual vol -25% | -0.5% | 55% |
| residual vol +25% | -0.5% | 57% |

Reconciliation: 12m mean -0.48% vs probability-weighted target -0.48%. Every input is cited in the parameters file. A distribution, not a signal.
