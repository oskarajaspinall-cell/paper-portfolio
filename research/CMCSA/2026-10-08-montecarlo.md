## Monte Carlo — CMCSA (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 20.94 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.11; residual vol 25.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.49 | +0.0% | 14.3% |
| IEF | +0.55 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 34.0 | +62.4% | ±18% |
| base | 45% | 24.0 | +14.6% | ±16% |
| bear | 35% | 16.5 | -21.2% | ±13% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 60% | -12.4% | week of 2022-04-25 (-12.4%) |
| NBCUniversal separation execution/terms | 20% | +4.1% | week of 2026-06-29 (+4.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.4% | +1.3% | -19.6% | -7.8% | +10.2% | +23.7% | 46% |
| 6m | +3.9% | +1.9% | -29.3% | -12.3% | +18.3% | +44.0% | 47% |
| 12m | +11.6% | +3.8% | -43.6% | -20.3% | +35.6% | +94.8% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +3.7% | -2.7% | +0.0% |
| 6m | -1.1% | +8.1% | -5.5% | +0.0% |
| 12m | -2.2% | +16.9% | -11.0% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +11.6% | 46% |
| bull +10pp / bear -10pp | +20.0% | 38% |
| bull -10pp / bear +10pp | +3.3% | 54% |
| residual vol -25% | +11.6% | 46% |
| residual vol +25% | +11.6% | 48% |

Reconciliation: 12m mean +11.63% vs probability-weighted target +11.63%. Every input is cited in the parameters file. A distribution, not a signal.
