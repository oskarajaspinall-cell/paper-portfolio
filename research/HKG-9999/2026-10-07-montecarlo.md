## Monte Carlo — HKG:9999 (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 185.6 HKD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-04-03 to 2026-09-28): R² 0.32; residual vol 30.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| HKG:2800 | +0.67 | +0.0% | 21.3% |
| KWEB | +0.27 | +0.0% | 33.9% |
| IEF | -0.02 | +0.0% | 6.6% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 30% | 226.0 | +21.8% | ±29% |
| base | 45% | 196.6 | +5.9% | ±34% |
| bear | 25% | 157.8 | -15.0% | ±41% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| PRC gaming regulation / VIE deconsolidation shock | 20% | -25.3% | week of 2023-12-18 (-25.3%) |
| Quarterly earnings miss | 20% | -12.7% | week of 2024-05-20 (-12.7%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.4% | -1.0% | -30.3% | -13.0% | +11.8% | +30.9% | 52% |
| 6m | +0.7% | -1.2% | -45.0% | -19.9% | +19.0% | +52.9% | 52% |
| 12m | +5.5% | -1.8% | -64.1% | -31.0% | +33.9% | +98.5% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.2% | -0.1% | -2.5% | +0.1% |
| 6m | +0.2% | +0.5% | -5.1% | +0.2% |
| 12m | +0.1% | +1.8% | -10.1% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.5% | 52% |
| bull +10pp / bear -10pp | +9.1% | 48% |
| bull -10pp / bear +10pp | +1.8% | 55% |
| residual vol -25% | +5.5% | 51% |
| residual vol +25% | +5.5% | 53% |

Reconciliation: 12m mean +5.45% vs probability-weighted target +5.45%. Every input is cited in the parameters file. A distribution, not a signal.
