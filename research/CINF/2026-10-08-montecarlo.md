## Monte Carlo — CINF (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 161.61 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.08; residual vol 21.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.35 | +0.0% | 14.3% |
| IEF | +0.42 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 30% | 197.17 | +22.0% | ±19% |
| base | 48% | 170.0 | +5.2% | ±22% |
| bear | 22% | 131.09 | -18.9% | ±22% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction (Q3 2026 reports Oct 26, 2026) | 35% | -12.2% | week of 2022-07-25 (-12.2%) |
| Risk-off shock hitting the equity book and AOCI simultaneously | 45% | -9.5% | week of 2025-03-31 (-9.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.5% | +0.9% | -17.4% | -6.4% | +7.6% | +17.5% | 46% |
| 6m | +1.4% | +1.0% | -27.2% | -11.0% | +13.2% | +31.1% | 48% |
| 12m | +4.9% | +2.3% | -43.1% | -18.1% | +24.9% | +62.0% | 47% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +3.3% | -3.0% | +0.0% |
| 6m | -0.9% | +6.6% | -6.0% | +0.0% |
| 12m | -1.7% | +13.2% | -11.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +4.9% | 47% |
| bull +10pp / bear -10pp | +9.0% | 42% |
| bull -10pp / bear +10pp | +0.8% | 53% |
| residual vol -25% | +4.9% | 46% |
| residual vol +25% | +4.9% | 48% |

Reconciliation: 12m mean +4.94% vs probability-weighted target +4.94%. Every input is cited in the parameters file. A distribution, not a signal.
