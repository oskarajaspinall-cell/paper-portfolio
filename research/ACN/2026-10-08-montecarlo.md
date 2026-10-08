## Monte Carlo — ACN (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 196.64 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.08; residual vol 40.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.67 | +0.0% | 14.3% |
| IEF | +0.09 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 225 | +14.4% | ±9% |
| base | 45% | 201 | +2.2% | ±10% |
| bear | 30% | 170 | -13.5% | ±11% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 40% | -24.8% | week of 2026-06-15 (-24.8%) |
| Public-sector governance / data-breach fallout | 10% | -8.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.4% | -0.6% | -30.1% | -12.7% | +13.0% | +33.8% | 51% |
| 6m | +0.0% | -2.9% | -41.6% | -20.0% | +16.8% | +51.2% | 54% |
| 12m | +0.5% | -6.7% | -55.8% | -30.0% | +22.4% | +80.1% | 56% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.1% | +2.2% | -3.8% | +0.1% |
| 6m | -0.3% | +3.8% | -7.7% | +0.0% |
| 12m | -0.4% | +7.0% | -15.4% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +0.5% | 56% |
| bull +10pp / bear -10pp | +3.3% | 53% |
| bull -10pp / bear +10pp | -2.3% | 59% |
| residual vol -25% | +0.5% | 54% |
| residual vol +25% | +0.5% | 59% |

Reconciliation: 12m mean +0.54% vs probability-weighted target +0.54%. Every input is cited in the parameters file. A distribution, not a signal.
