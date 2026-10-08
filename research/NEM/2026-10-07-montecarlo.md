## Monte Carlo — NEM (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 116.39 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.10; residual vol 42.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.83 | +5.0% | 14.3% |
| IEF | +0.79 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 135.29 | +16.2% | ±12% |
| base | 45% | 115.0 | -1.2% | ±15% |
| bear | 30% | 76.05 | -34.7% | ±22% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings release | 60% | -16.0% | week of 2024-10-21 (-16.0%) |
| Gold price shock (real-yield / dollar driven correction) | 100% | -12.6% | week of 2026-03-16 (-12.6%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -2.4% | -2.7% | -27.5% | -13.1% | +7.7% | +24.1% | 57% |
| 6m | -4.6% | -6.2% | -40.6% | -21.3% | +10.2% | +37.7% | 60% |
| 12m | -6.9% | -11.7% | -58.8% | -34.0% | +14.1% | +61.4% | 62% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.4% | +846.6% | -850.8% | +0.0% |
| 6m | +0.8% | +1693.2% | -1701.9% | +0.0% |
| 12m | +1.8% | +3386.4% | -3403.8% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -6.9% | 62% |
| bull +10pp / bear -10pp | -1.8% | 57% |
| bull -10pp / bear +10pp | -12.0% | 67% |
| residual vol -25% | -6.9% | 62% |
| residual vol +25% | -6.9% | 63% |

Reconciliation: 12m mean -6.88% vs probability-weighted target -6.88%. Every input is cited in the parameters file. A distribution, not a signal.
