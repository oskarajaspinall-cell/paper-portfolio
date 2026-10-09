## Monte Carlo — ADP (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 270.73 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.12; residual vol 24.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.53 | +0.0% | 14.3% |
| IEF | -0.16 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 292.44 | +8.0% | ±11% |
| base | 45% | 276.22 | +2.0% | ±13% |
| bear | 35% | 222.02 | -18.0% | ±21% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 20% | -11.1% | week of 2023-10-23 (-11.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.4% | -2.1% | -18.6% | -8.9% | +5.4% | +17.8% | 58% |
| 6m | -2.6% | -4.0% | -28.3% | -14.3% | +7.6% | +27.7% | 59% |
| 12m | -3.8% | -6.7% | -43.1% | -22.9% | +12.4% | +44.8% | 60% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.1% | -1.5% | -0.7% | +0.0% |
| 6m | +0.2% | -3.0% | -1.3% | +0.0% |
| 12m | +0.5% | -6.1% | -2.6% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -3.8% | 60% |
| bull +10pp / bear -10pp | -1.2% | 56% |
| bull -10pp / bear +10pp | -6.4% | 64% |
| residual vol -25% | -3.8% | 58% |
| residual vol +25% | -3.8% | 60% |

Reconciliation: 12m mean -3.78% vs probability-weighted target -3.78%. Every input is cited in the parameters file. A distribution, not a signal.
