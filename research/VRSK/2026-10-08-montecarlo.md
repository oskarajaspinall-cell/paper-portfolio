## Monte Carlo — VRSK (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 168.68 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.04; residual vol 31.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.26 | +0.0% | 14.3% |
| IEF | +0.48 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 205 | +21.5% | ±11% |
| base | 45% | 180 | +6.7% | ±12% |
| bear | 30% | 135 | -20.0% | ±16% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| AccuLynx Delaware Chancery Court ruling / litigation risk | 20% | -5.3% | week of 2026-08-10 (-5.3%) |
| Quarterly earnings surprise (Q3 2026 report, Nov 5, 2026) | 25% | -9.1% | week of 2022-05-02 (-9.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.4% | -1.5% | -23.2% | -10.8% | +9.0% | +25.5% | 54% |
| 6m | +0.1% | -2.3% | -33.1% | -16.0% | +13.6% | +40.7% | 54% |
| 12m | +2.4% | -3.4% | -46.6% | -24.1% | +22.5% | +70.1% | 54% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +0.1% | -1.1% | +0.1% |
| 6m | -1.2% | +0.9% | -2.1% | +0.0% |
| 12m | -2.4% | +2.4% | -4.1% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.4% | 54% |
| bull +10pp / bear -10pp | +6.6% | 49% |
| bull -10pp / bear +10pp | -1.7% | 59% |
| residual vol -25% | +2.4% | 51% |
| residual vol +25% | +2.4% | 56% |

Reconciliation: 12m mean +2.41% vs probability-weighted target +2.41%. Every input is cited in the parameters file. A distribution, not a signal.
