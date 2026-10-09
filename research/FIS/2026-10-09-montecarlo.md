## Monte Carlo — FIS (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 34.34 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.10; residual vol 29.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.57 | +0.0% | 14.3% |
| IEF | +0.54 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 59.49 | +73.2% | ±3% |
| base | 45% | 40.0 | +16.5% | ±21% |
| bear | 35% | 26.0 | -24.3% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction (next: Q3 2026 results, Nov 4 2026) | 40% | -29.1% | week of 2022-10-31 (-29.1%) |
| Credit / refinancing stress shock | 80% | -9.9% | week of 2026-02-09 (-9.9%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.6% | +2.3% | -29.4% | -9.0% | +13.1% | +29.0% | 45% |
| 6m | +4.5% | +1.9% | -39.0% | -15.4% | +23.0% | +55.5% | 47% |
| 12m | +13.6% | +1.9% | -53.6% | -26.1% | +43.2% | +118.3% | 49% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +8.9% | -8.6% | +0.0% |
| 6m | -0.8% | +18.5% | -17.2% | +0.0% |
| 12m | -1.6% | +37.6% | -34.4% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +13.6% | 49% |
| bull +10pp / bear -10pp | +23.3% | 41% |
| bull -10pp / bear +10pp | +3.8% | 56% |
| residual vol -25% | +13.6% | 49% |
| residual vol +25% | +13.6% | 49% |

Reconciliation: 12m mean +13.56% vs probability-weighted target +13.56%. Every input is cited in the parameters file. A distribution, not a signal.
