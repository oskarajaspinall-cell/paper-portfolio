## Monte Carlo — AOS (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 56.9 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.20; residual vol 22.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.66 | +0.0% | 14.3% |
| IEF | +0.64 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 68.0 | +19.5% | ±10% |
| base | 45% | 60.0 | +5.4% | ±0% |
| bear | 30% | 47.0 | -17.4% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release (Oct 29, 2026) confirms guidance cut / tariff impact | 20% | -9.3% | week of 2022-04-25 (-9.3%) |
| Tariff cost impact (newly announced trade tariffs, excluded from FY2026 guidance) | 50% | -10.0% | none (stated assumption) |
| China business strategic review outcome (partnership or exit announcement) | 30% | +12.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.2% | -0.8% | -19.6% | -8.8% | +7.8% | +20.8% | 53% |
| 6m | +0.2% | -1.1% | -28.2% | -12.6% | +11.7% | +32.6% | 52% |
| 12m | +2.1% | -1.5% | -38.9% | -18.8% | +19.7% | +54.8% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +0.5% | -1.5% | +0.0% |
| 6m | -0.0% | +1.4% | -2.9% | +0.0% |
| 12m | +0.1% | +3.3% | -5.6% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.1% | 52% |
| bull +10pp / bear -10pp | +5.8% | 46% |
| bull -10pp / bear +10pp | -1.6% | 57% |
| residual vol -25% | +2.1% | 50% |
| residual vol +25% | +2.1% | 54% |

Reconciliation: 12m mean +2.11% vs probability-weighted target +2.11%. Every input is cited in the parameters file. A distribution, not a signal.
