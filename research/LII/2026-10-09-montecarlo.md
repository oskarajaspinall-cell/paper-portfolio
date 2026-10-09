## Monte Carlo — LII (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 361.54 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.19; residual vol 34.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.98 | +0.0% | 14.3% |
| IEF | +0.33 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 392.66 | +8.6% | ±33% |
| base | 45% | 356.77 | -1.3% | ±33% |
| bear | 35% | 244.9 | -32.3% | ±33% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Antitrust/shareholder litigation shock | 20% | -2.4% | week of 2026-08-24 (-2.4%) |
| Earnings/guidance-cut shock (Q3 2026, Oct 28) | 20% | -23.2% | week of 2026-07-27 (-23.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -4.3% | -4.5% | -30.0% | -14.6% | +5.7% | +21.6% | 62% |
| 6m | -7.4% | -8.8% | -45.8% | -24.9% | +8.5% | +36.4% | 63% |
| 12m | -10.2% | -16.9% | -67.7% | -40.8% | +13.9% | +68.9% | 65% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | -3.6% | -1.8% | +0.0% |
| 6m | -0.9% | -7.3% | -3.5% | +0.0% |
| 12m | -1.6% | -14.6% | -6.9% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -10.2% | 65% |
| bull +10pp / bear -10pp | -6.1% | 61% |
| bull -10pp / bear +10pp | -14.3% | 69% |
| residual vol -25% | -10.2% | 65% |
| residual vol +25% | -10.2% | 66% |

Reconciliation: 12m mean -10.16% vs probability-weighted target -10.16%. Every input is cited in the parameters file. A distribution, not a signal.
