## Monte Carlo — WRB (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 69.73 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.02; residual vol 24.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.19 | +0.0% | 14.3% |
| IEF | +0.27 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 28% | 77.06 | +10.5% | ±5% |
| base | 50% | 73.89 | +6.0% | ±3% |
| bear | 22% | 60.62 | -13.1% | ±5% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction | 76% | -7.0% | week of 2024-04-22 (-7.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.6% | +0.1% | -18.7% | -7.7% | +8.5% | +21.2% | 50% |
| 6m | +1.2% | -0.1% | -25.9% | -11.2% | +12.2% | +32.6% | 50% |
| 12m | +3.1% | +0.5% | -35.7% | -16.0% | +18.5% | +50.4% | 49% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | +2.8% | -2.6% | +0.1% |
| 6m | -0.7% | +5.5% | -5.2% | +0.0% |
| 12m | -1.3% | +11.0% | -10.3% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +3.1% | 49% |
| bull +10pp / bear -10pp | +5.4% | 45% |
| bull -10pp / bear +10pp | +0.7% | 53% |
| residual vol -25% | +3.1% | 46% |
| residual vol +25% | +3.1% | 52% |

Reconciliation: 12m mean +3.05% vs probability-weighted target +3.05%. Every input is cited in the parameters file. A distribution, not a signal.
