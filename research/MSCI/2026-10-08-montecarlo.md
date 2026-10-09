## Monte Carlo — MSCI (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 555.38 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.24; residual vol 24.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.84 | +0.0% | 14.3% |
| IEF | +0.41 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 655 | +17.9% | ±24% |
| base | 45% | 583 | +5.0% | ±24% |
| bear | 35% | 480 | -13.6% | ±24% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release (2026-10-20) | 25% | -12.4% | week of 2026-07-20 (-12.4%) |
| BlackRock client-concentration shock (index in-sourcing/dual-sourcing) | 5% | -20.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.9% | -1.0% | -20.6% | -8.6% | +6.8% | +18.7% | 53% |
| 6m | -0.9% | -1.8% | -31.1% | -14.3% | +11.7% | +32.4% | 54% |
| 12m | +1.1% | -3.0% | -48.0% | -23.1% | +21.3% | +62.9% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.5% | +0.1% | -1.3% | +0.0% |
| 6m | -1.1% | +0.8% | -2.6% | +0.0% |
| 12m | -2.0% | +2.1% | -5.0% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.1% | 53% |
| bull +10pp / bear -10pp | +4.2% | 50% |
| bull -10pp / bear +10pp | -2.1% | 57% |
| residual vol -25% | +1.1% | 53% |
| residual vol +25% | +1.1% | 54% |

Reconciliation: 12m mean +1.07% vs probability-weighted target +1.07%. Every input is cited in the parameters file. A distribution, not a signal.
