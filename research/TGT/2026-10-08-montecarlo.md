## Monte Carlo — TGT (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 150.92 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.08; residual vol 28.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.57 | +0.0% | 14.3% |
| IEF | +0.49 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 170.75 | +13.1% | ±4% |
| base | 45% | 150.92 | +0.0% | ±3% |
| bear | 30% | 124.0 | -17.8% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings-day margin-miss reaction | 20% | -17.2% | week of 2024-11-18 (-17.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.7% | -1.6% | -23.9% | -10.8% | +8.8% | +25.0% | 54% |
| 6m | -1.5% | -3.6% | -33.6% | -16.4% | +11.6% | +36.8% | 57% |
| 12m | -2.1% | -6.7% | -45.6% | -24.9% | +16.1% | +56.3% | 59% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.5% | -0.4% | -1.1% | +0.1% |
| 6m | -1.0% | -0.8% | -2.1% | +0.0% |
| 12m | -1.9% | -1.5% | -4.2% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -2.1% | 59% |
| bull +10pp / bear -10pp | +1.0% | 54% |
| bull -10pp / bear +10pp | -5.2% | 63% |
| residual vol -25% | -2.1% | 57% |
| residual vol +25% | -2.1% | 60% |

Reconciliation: 12m mean -2.07% vs probability-weighted target -2.07%. Every input is cited in the parameters file. A distribution, not a signal.
