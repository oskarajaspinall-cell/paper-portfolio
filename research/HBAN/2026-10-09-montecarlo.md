## Monte Carlo — HBAN (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 15.37 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.27; residual vol 26.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.08 | +0.0% | 14.3% |
| IEF | +0.17 | -6.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 19.31 | +25.6% | ±14% |
| base | 45% | 16.2 | +5.4% | ±15% |
| bear | 35% | 11.69 | -23.9% | ±13% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings guidance reset | 18% | -13.9% | week of 2022-01-18 (-13.9%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.2% | -2.0% | -23.6% | -11.2% | +7.9% | +24.2% | 55% |
| 6m | -1.6% | -3.7% | -34.5% | -17.6% | +11.9% | +38.6% | 57% |
| 12m | -0.8% | -6.6% | -49.0% | -27.5% | +19.2% | +66.6% | 57% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | -1.3% | -0.8% | +0.0% |
| 6m | -0.6% | -2.1% | -1.5% | +0.0% |
| 12m | -0.9% | -3.7% | -3.0% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -0.8% | 57% |
| bull +10pp / bear -10pp | +4.1% | 52% |
| bull -10pp / bear +10pp | -5.8% | 63% |
| residual vol -25% | -0.8% | 56% |
| residual vol +25% | -0.8% | 59% |

Reconciliation: 12m mean -0.82% vs probability-weighted target -0.82%. Every input is cited in the parameters file. A distribution, not a signal.
