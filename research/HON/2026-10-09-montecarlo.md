## Monte Carlo — HON (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 206.6 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.22; residual vol 23.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.75 | +0.0% | 14.3% |
| IEF | +0.27 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 284.73 | +37.8% | ±0% |
| base | 50% | 199.75 | -3.3% | ±0% |
| bear | 30% | 164.78 | -20.2% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release (Oct 22, 2026) during an active separation | 20% | -8.7% | week of 2026-04-20 (-8.7%) |
| Aerospace/corporate-separation catalyst (completion or update) | 30% | -10.0% | week of 2026-06-01 (-10.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.8% | -1.7% | -21.6% | -10.2% | +7.7% | +22.9% | 55% |
| 6m | -1.1% | -3.4% | -31.3% | -15.3% | +11.0% | +36.3% | 57% |
| 12m | -0.2% | -6.3% | -43.1% | -23.6% | +17.1% | +63.2% | 58% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +0.0% | -1.5% | +0.0% |
| 6m | -0.7% | +0.6% | -3.0% | +0.0% |
| 12m | -1.3% | +1.7% | -6.0% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -0.2% | 58% |
| bull +10pp / bear -10pp | +5.6% | 51% |
| bull -10pp / bear +10pp | -6.0% | 65% |
| residual vol -25% | -0.2% | 58% |
| residual vol +25% | -0.2% | 58% |

Reconciliation: 12m mean -0.17% vs probability-weighted target -0.17%. Every input is cited in the parameters file. A distribution, not a signal.
