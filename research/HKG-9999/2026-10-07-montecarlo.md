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
| bull | 30% | 226.0 | +21.8% | ±10% |
| base | 45% | 196.6 | +5.9% | ±11% |
| bear | 25% | 157.8 | -15.0% | ±14% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| PRC gaming-regulation or VIE action | 20% | -25.3% | week of 2023-12-18 (-25.3%) |
| Weak Ananta global launch reception | 20% | -12.7% | week of 2024-05-20 (-12.7%) |
| HFCAA audit-inspection risk resurfacing | 10% | -15.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.8% | -0.4% | -27.5% | -12.1% | +12.4% | +33.1% | 51% |
| 6m | +2.3% | -1.0% | -37.6% | -17.4% | +18.7% | +52.8% | 52% |
| 12m | +5.5% | -1.7% | -50.6% | -25.0% | +28.1% | +85.7% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.2% | +1.7% | -2.9% | +0.1% |
| 6m | +0.2% | +4.1% | -5.9% | +0.3% |
| 12m | +0.1% | +8.9% | -11.9% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.5% | 52% |
| bull +10pp / bear -10pp | +9.1% | 48% |
| bull -10pp / bear +10pp | +1.8% | 55% |
| residual vol -25% | +5.5% | 49% |
| residual vol +25% | +5.5% | 54% |

Reconciliation: 12m mean +5.45% vs probability-weighted target +5.45%. Every input is cited in the parameters file. A distribution, not a signal.
