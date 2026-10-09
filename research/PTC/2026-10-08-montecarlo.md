## Monte Carlo — PTC (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 193.6 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.25; residual vol 31.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.04 | +0.0% | 14.3% |
| IEF | +0.19 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 10% | 206.82 | +6.8% | ±23% |
| base | 75% | 196.05 | +1.3% | ±29% |
| bear | 15% | 133.15 | -31.2% | ±30% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Schneider Electric merger agreement termination | 15% | -30.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.9% | -1.8% | -26.8% | -11.1% | +7.7% | +22.1% | 55% |
| 6m | -3.1% | -3.9% | -41.1% | -18.9% | +11.8% | +37.2% | 57% |
| 12m | -3.1% | -7.4% | -60.0% | -31.1% | +20.4% | +67.2% | 58% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | -1.7% | -1.5% | +0.0% |
| 6m | -0.1% | -3.4% | -2.9% | +0.0% |
| 12m | +0.1% | -6.8% | -5.7% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -3.1% | 58% |
| bull +10pp / bear -10pp | +0.8% | 53% |
| residual vol -25% | -3.1% | 57% |
| residual vol +25% | -3.1% | 59% |

Reconciliation: 12m mean -3.05% vs probability-weighted target -3.05%. Every input is cited in the parameters file. A distribution, not a signal.
