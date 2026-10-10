## Monte Carlo — OTIS (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 66.45 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.22; residual vol 16.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.58 | +0.0% | 14.3% |
| IEF | +0.51 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 87.0 | +30.9% | ±9% |
| base | 50% | 73.0 | +9.9% | ±0% |
| bear | 25% | 56.0 | -15.7% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings / service-margin confirmation (Oct 28, 2026) | 25% | -9.7% | week of 2025-07-21 (-9.7%) |
| CEO succession outcome (successor named, expected H1 2027) | 50% | -8.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.4% | +1.3% | -15.0% | -5.4% | +8.2% | +17.9% | 45% |
| 6m | +3.5% | +2.7% | -21.1% | -7.4% | +13.7% | +29.6% | 43% |
| 12m | +8.7% | +6.2% | -30.1% | -10.5% | +25.2% | +56.1% | 40% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +3.5% | -2.2% | +0.0% |
| 6m | -0.8% | +7.5% | -4.5% | +0.0% |
| 12m | -1.5% | +15.5% | -8.9% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +8.7% | 40% |
| bull +10pp / bear -10pp | +13.4% | 33% |
| bull -10pp / bear +10pp | +4.1% | 48% |
| residual vol -25% | +8.7% | 38% |
| residual vol +25% | +8.7% | 42% |

Reconciliation: 12m mean +8.73% vs probability-weighted target +8.73%. Every input is cited in the parameters file. A distribution, not a signal.
