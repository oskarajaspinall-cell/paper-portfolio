## Monte Carlo — MA (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 574.76 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.34; residual vol 17.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.78 | +0.0% | 14.3% |
| IEF | +0.20 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 649.33 | +13.0% | ±17% |
| base | 50% | 574.76 | +0.0% | ±7% |
| bear | 30% | 412.24 | -28.3% | ±13% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| US interchange-fee legislation | 12% | -12.0% | none (stated assumption) |
| Merchant-interchange litigation settlement/judgment | 7% | -8.0% | none (stated assumption) |
| Q3 2026 earnings reaction (Oct 29, 2026) | 34% | -6.5% | week of 2021-10-25 (-6.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.7% | -2.1% | -17.3% | -8.8% | +5.0% | +15.5% | 58% |
| 6m | -3.5% | -4.4% | -27.9% | -14.7% | +6.7% | +23.9% | 61% |
| 12m | -5.9% | -8.4% | -43.1% | -24.9% | +10.3% | +40.0% | 62% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | -0.7% | -1.3% | +0.0% |
| 6m | -0.6% | -1.8% | -2.5% | +0.0% |
| 12m | -1.0% | -3.9% | -5.1% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -5.9% | 62% |
| bull +10pp / bear -10pp | -1.8% | 56% |
| bull -10pp / bear +10pp | -10.0% | 68% |
| residual vol -25% | -5.9% | 62% |
| residual vol +25% | -5.9% | 62% |

Reconciliation: 12m mean -5.89% vs probability-weighted target -5.89%. Every input is cited in the parameters file. A distribution, not a signal.
