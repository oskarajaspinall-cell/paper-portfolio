## Monte Carlo — HKG:2076 (2026-10-11)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 60.0 HKD (close 2026-10-09).
Factor regression (156 weekly returns, 2023-04-03 to 2026-09-28): R² 0.32; residual vol 37.9% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| HKG:2800 | +0.81 | +0.0% | 21.3% |
| KWEB | +0.31 | +0.0% | 33.9% |
| IEF | +0.02 | +0.0% | 6.6% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 131.83 | +119.7% | ±24% |
| base | 45% | 83.3 | +38.8% | ±38% |
| bear | 30% | 48.36 | -19.4% | ±38% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Large negative earnings reaction | 24% | -14.2% | week of 2024-08-26 (-14.2%) |
| China VIE-enforceability / HFCAA regulatory shock | 41% | -19.2% | week of 2025-04-07 (-19.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +6.5% | +4.4% | -31.1% | -11.1% | +21.8% | +51.1% | 43% |
| 6m | +15.4% | +9.1% | -45.7% | -16.2% | +40.2% | +97.4% | 41% |
| 12m | +41.6% | +20.2% | -65.4% | -25.2% | +83.9% | +223.4% | 40% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.2% | +7.0% | -3.9% | +0.1% |
| 6m | +0.2% | +14.0% | -7.9% | +0.2% |
| 12m | +0.1% | +28.1% | -15.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +41.6% | 40% |
| bull +10pp / bear -10pp | +55.5% | 33% |
| bull -10pp / bear +10pp | +27.7% | 46% |
| residual vol -25% | +41.6% | 39% |
| residual vol +25% | +41.6% | 41% |

Reconciliation: 12m mean +41.58% vs probability-weighted target +41.58%. Every input is cited in the parameters file. A distribution, not a signal.
