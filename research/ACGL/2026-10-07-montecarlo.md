## Monte Carlo — ACGL (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 94.82 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.04; residual vol 20.9% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.31 | +0.0% | 14.3% |
| IEF | -0.11 | -2.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 27% | 122.0 | +28.7% | ±5% |
| base | 45% | 102.0 | +7.6% | ±4% |
| bear | 28% | 81.0 | -14.6% | ±5% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings release (second consecutive weak Insurance-segment print) | 76% | -8.8% | week of 2024-10-28 (-8.8%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.4% | +1.3% | -16.5% | -6.1% | +8.6% | +19.8% | 46% |
| 6m | +3.0% | +1.9% | -23.2% | -9.0% | +13.8% | +32.9% | 46% |
| 12m | +7.1% | +4.5% | -33.2% | -13.3% | +23.9% | +56.9% | 44% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +4.0% | -3.3% | +0.0% |
| 6m | +0.1% | +8.0% | -6.6% | +0.0% |
| 12m | +0.2% | +16.0% | -13.1% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +7.1% | 44% |
| bull +10pp / bear -10pp | +11.4% | 37% |
| bull -10pp / bear +10pp | +2.7% | 50% |
| residual vol -25% | +7.1% | 41% |
| residual vol +25% | +7.1% | 46% |

Reconciliation: 12m mean +7.07% vs probability-weighted target +7.07%. Every input is cited in the parameters file. A distribution, not a signal.
