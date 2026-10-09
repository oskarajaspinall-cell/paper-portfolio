## Monte Carlo — MKC (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 45.94 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.09; residual vol 28.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.21 | +0.0% | 14.3% |
| IEF | +1.09 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 62.0 | +35.0% | ±28% |
| base | 45% | 50.0 | +8.8% | ±9% |
| bear | 35% | 36.0 | -21.6% | ±28% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Unilever Foods acquisition - UK CMA regulatory block/delay/remedies | 100% | -5.1% | week of 2026-09-14 (-5.1%) |
| Quarterly earnings reaction | 100% | -14.1% | week of 2023-10-02 (-14.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.4% | -0.5% | -18.4% | -7.6% | +6.6% | +18.1% | 52% |
| 6m | +0.2% | -0.3% | -30.4% | -11.9% | +11.7% | +32.1% | 51% |
| 12m | +3.4% | +0.9% | -49.0% | -19.3% | +21.1% | +66.7% | 49% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.8% | +1288.7% | -1289.0% | +0.0% |
| 6m | -1.6% | +2577.8% | -2577.9% | +0.0% |
| 12m | -3.2% | +5156.2% | -5155.9% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +3.4% | 49% |
| bull +10pp / bear -10pp | +9.1% | 43% |
| bull -10pp / bear +10pp | -2.3% | 54% |
| residual vol -25% | +3.4% | 47% |
| residual vol +25% | +3.4% | 50% |

Reconciliation: 12m mean +3.40% vs probability-weighted target +3.40%. Every input is cited in the parameters file. A distribution, not a signal.
