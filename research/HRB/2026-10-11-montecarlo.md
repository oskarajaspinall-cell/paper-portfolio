## Monte Carlo — HRB (2026-10-11)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 44.05 USD (close 2026-10-09).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.03; residual vol 38.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.34 | +0.0% | 14.3% |
| IEF | +0.40 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 63.0 | +43.0% | ±37% |
| base | 45% | 54.02 | +22.6% | ±37% |
| bear | 30% | 37.58 | -14.7% | ±37% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings miss / negative reaction | 19% | -16.7% | week of 2026-02-02 (-16.7%) |
| Free government filing / AI DIY disruption shock | 15% | -15.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.7% | +2.1% | -25.6% | -8.8% | +12.3% | +28.7% | 45% |
| 6m | +5.0% | +4.1% | -40.7% | -14.4% | +23.6% | +54.0% | 44% |
| 12m | +16.5% | +8.8% | -61.8% | -23.5% | +49.1% | +119.5% | 43% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +1.9% | -1.7% | +0.0% |
| 6m | +0.0% | +3.9% | -3.3% | +0.0% |
| 12m | +0.0% | +7.7% | -6.5% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +16.5% | 43% |
| bull +10pp / bear -10pp | +22.3% | 39% |
| bull -10pp / bear +10pp | +10.8% | 47% |
| residual vol -25% | +16.5% | 42% |
| residual vol +25% | +16.5% | 46% |

Reconciliation: 12m mean +16.53% vs probability-weighted target +16.53%. Every input is cited in the parameters file. A distribution, not a signal.
