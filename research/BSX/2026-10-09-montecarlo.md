## Monte Carlo — BSX (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 42.04 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.14; residual vol 33.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.75 | +0.0% | 14.3% |
| IEF | +0.13 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 82.57 | +96.4% | ±33% |
| base | 40% | 54.18 | +28.9% | ±11% |
| bear | 40% | 31.04 | -26.2% | ±33% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings / guidance reset | 20% | -18.4% | week of 2026-02-02 (-18.4%) |
| Cyberattack / operational disruption recurrence | 20% | -7.0% | week of 2026-08-24 (-7.0%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +2.4% | +0.9% | -25.7% | -10.5% | +14.3% | +35.1% | 48% |
| 6m | +6.4% | +1.7% | -39.4% | -16.6% | +26.1% | +66.3% | 48% |
| 12m | +20.4% | +4.5% | -60.2% | -26.9% | +51.7% | +156.0% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +2.3% | -1.6% | +0.1% |
| 6m | -0.0% | +4.5% | -3.2% | +0.0% |
| 12m | +0.1% | +9.1% | -6.2% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +20.4% | 46% |
| bull +10pp / bear -10pp | +32.6% | 39% |
| bull -10pp / bear +10pp | +8.1% | 53% |
| residual vol -25% | +20.4% | 44% |
| residual vol +25% | +20.4% | 49% |

Reconciliation: 12m mean +20.37% vs probability-weighted target +20.37%. Every input is cited in the parameters file. A distribution, not a signal.
