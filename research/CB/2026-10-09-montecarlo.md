## Monte Carlo — CB (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 343.78 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.03; residual vol 18.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.16 | +0.0% | 14.3% |
| IEF | +0.32 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 30% | 385.88 | +12.2% | ±9% |
| base | 50% | 336.74 | -2.0% | ±9% |
| bear | 20% | 250.23 | -27.2% | ±8% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release (Oct 20-21, 2026) | 40% | -7.7% | week of 2023-01-30 (-7.7%) |
| Disorderly rate/credit shock hitting CB's bond float | 20% | -5.4% | week of 2023-03-13 (-5.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.0% | -1.1% | -15.6% | -7.1% | +4.9% | +13.8% | 55% |
| 6m | -1.9% | -2.4% | -24.0% | -11.5% | +7.4% | +21.8% | 57% |
| 12m | -2.8% | -4.1% | -38.0% | -19.0% | +11.7% | +37.2% | 57% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.2% | +0.1% | -1.3% | +0.0% |
| 6m | -0.5% | +0.2% | -2.7% | +0.0% |
| 12m | -0.9% | +0.5% | -5.4% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -2.8% | 57% |
| bull +10pp / bear -10pp | +1.2% | 50% |
| bull -10pp / bear +10pp | -6.7% | 64% |
| residual vol -25% | -2.8% | 55% |
| residual vol +25% | -2.8% | 58% |

Reconciliation: 12m mean -2.79% vs probability-weighted target -2.79%. Every input is cited in the parameters file. A distribution, not a signal.
