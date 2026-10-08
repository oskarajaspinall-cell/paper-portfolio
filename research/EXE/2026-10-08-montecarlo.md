## Monte Carlo — EXE (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 88.12 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 28.6% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.34 | +0.0% | 14.3% |
| IEF | -0.64 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 114 | +29.4% | ±5% |
| base | 45% | 88 | -0.1% | ±0% |
| bear | 30% | 71 | -19.4% | ±5% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Large earnings-day reaction | 80% | -5.1% | week of 2025-02-24 (-5.1%) |
| Leverage/credit shock | 20% | -11.5% | week of 2023-11-06 (-11.5%) |
| Gas-price collapse | 20% | -18.2% | week of 2022-06-13 (-18.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.4% | -0.9% | -23.8% | -10.4% | +9.0% | +24.8% | 53% |
| 6m | -0.2% | -2.2% | -33.3% | -15.8% | +13.3% | +39.3% | 54% |
| 12m | +1.5% | -4.0% | -45.3% | -23.8% | +20.5% | +67.1% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.6% | +1.8% | -3.9% | +0.1% |
| 6m | +1.2% | +4.0% | -7.9% | +0.0% |
| 12m | +2.6% | +8.5% | -15.8% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.5% | 55% |
| bull +10pp / bear -10pp | +6.3% | 49% |
| bull -10pp / bear +10pp | -3.4% | 60% |
| residual vol -25% | +1.5% | 53% |
| residual vol +25% | +1.5% | 56% |

Reconciliation: 12m mean +1.45% vs probability-weighted target +1.45%. Every input is cited in the parameters file. A distribution, not a signal.
