## Monte Carlo — BMY (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 59.59 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.02; residual vol 25.6% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.21 | +5.0% | 14.3% |
| IEF | +0.23 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 74.0 | +24.2% | ±3% |
| base | 45% | 60.0 | +0.7% | ±11% |
| bear | 30% | 48.0 | -19.4% | ±14% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings / legacy-erosion print risk (Q3 2026, Oct 29 2026) | 19% | -9.6% | week of 2023-10-23 (-9.6%) |
| Pipeline / regulatory binary-readout risk | 100% | -3.0% | week of 2023-02-06 (-3.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.5% | -1.2% | -17.7% | -8.2% | +6.4% | +18.9% | 54% |
| 6m | -0.5% | -2.2% | -26.4% | -12.7% | +10.1% | +30.4% | 55% |
| 12m | +0.5% | -3.4% | -39.7% | -20.1% | +17.2% | +53.2% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +192.5% | -193.7% | +0.0% |
| 6m | +0.0% | +385.4% | -387.5% | +0.0% |
| 12m | +0.1% | +771.1% | -774.9% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +0.5% | 55% |
| bull +10pp / bear -10pp | +4.9% | 48% |
| bull -10pp / bear +10pp | -3.8% | 61% |
| residual vol -25% | +0.5% | 52% |
| residual vol +25% | +0.5% | 56% |

Reconciliation: 12m mean +0.52% vs probability-weighted target +0.52%. Every input is cited in the parameters file. A distribution, not a signal.
