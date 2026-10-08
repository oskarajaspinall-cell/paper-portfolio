## Monte Carlo — INCY (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 112.73 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.09; residual vol 32.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.38 | +4.0% | 14.3% |
| IEF | +1.17 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 133.0 | +18.0% | ±6% |
| base | 45% | 118.0 | +4.7% | ±6% |
| bear | 30% | 95.0 | -15.7% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Large earnings-week move | 20% | -10.5% | week of 2023-05-01 (-10.5%) |
| Negative pipeline/regulatory update | 40% | -9.7% | week of 2024-12-09 (-9.7%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.2% | -1.1% | -25.0% | -11.3% | +10.7% | +29.0% | 53% |
| 6m | +0.4% | -2.3% | -35.2% | -16.8% | +14.8% | +44.2% | 54% |
| 12m | +1.9% | -4.4% | -47.1% | -24.8% | +21.8% | +70.7% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.8% | +1.5% | -2.0% | +0.1% |
| 6m | -1.6% | +3.1% | -4.0% | +0.0% |
| 12m | -3.2% | +6.2% | -7.9% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.9% | 55% |
| bull +10pp / bear -10pp | +5.3% | 51% |
| bull -10pp / bear +10pp | -1.5% | 59% |
| residual vol -25% | +1.9% | 53% |
| residual vol +25% | +1.9% | 57% |

Reconciliation: 12m mean +1.88% vs probability-weighted target +1.88%. Every input is cited in the parameters file. A distribution, not a signal.
