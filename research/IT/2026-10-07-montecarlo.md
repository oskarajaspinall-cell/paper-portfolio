## Monte Carlo — IT (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 184.92 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.10; residual vol 46.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.90 | +7.0% | 14.3% |
| IEF | +0.58 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 269 | +45.5% | ±8% |
| base | 45% | 201 | +8.7% | ±0% |
| bear | 30% | 124 | -32.9% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings print vindicates AI-disruption bear case | 60% | -30.3% | week of 2025-08-04 (-30.3%) |
| Earnings print accelerates contract value, AI fear fades | 100% | +22.9% | week of 2026-08-03 (+22.9%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.7% | +1.8% | -35.6% | -12.7% | +14.7% | +33.9% | 46% |
| 6m | +1.4% | -0.7% | -48.1% | -22.0% | +21.5% | +57.9% | 51% |
| 12m | +5.4% | -4.3% | -62.4% | -34.1% | +34.4% | +107.3% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +1.5% | -1294.5% | +1291.1% | +0.1% |
| 6m | +3.0% | -2588.9% | +2581.8% | +0.0% |
| 12m | +6.2% | -5177.8% | +5163.5% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.4% | 53% |
| bull +10pp / bear -10pp | +13.2% | 47% |
| bull -10pp / bear +10pp | -2.4% | 60% |
| residual vol -25% | +5.4% | 53% |
| residual vol +25% | +5.4% | 54% |

Reconciliation: 12m mean +5.40% vs probability-weighted target +5.40%. Every input is cited in the parameters file. A distribution, not a signal.
