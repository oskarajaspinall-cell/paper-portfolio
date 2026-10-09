## Monte Carlo — SYF (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 73.72 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.35; residual vol 25.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.30 | +0.0% | 14.3% |
| IEF | -0.21 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 22% | 88.0 | +19.4% | ±25% |
| base | 50% | 75.0 | +1.7% | ±25% |
| bear | 28% | 50.0 | -32.2% | ±25% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction (Oct 20, 2026) | 34% | -5.2% | week of 2026-01-26 (-5.2%) |
| Credit-quality / regulatory shock (NCOs above 6.0% target, allowance under-reserving) | 20% | -11.3% | week of 2023-03-13 (-11.3%) |
| Loss or non-renewal of a top sales-platform partner | 5% | -20.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -2.1% | -2.7% | -24.4% | -11.9% | +7.1% | +22.3% | 57% |
| 6m | -3.5% | -5.4% | -38.0% | -19.9% | +10.8% | +37.0% | 59% |
| 12m | -3.9% | -10.1% | -57.5% | -32.5% | +19.4% | +69.9% | 60% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.2% | -1.9% | -1.6% | +0.0% |
| 6m | +0.3% | -3.7% | -3.2% | +0.0% |
| 12m | +1.0% | -7.4% | -6.3% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -3.9% | 60% |
| bull +10pp / bear -10pp | +1.3% | 55% |
| bull -10pp / bear +10pp | -9.0% | 65% |
| residual vol -25% | -3.9% | 60% |
| residual vol +25% | -3.9% | 61% |

Reconciliation: 12m mean -3.88% vs probability-weighted target -3.88%. Every input is cited in the parameters file. A distribution, not a signal.
