## Monte Carlo — PEP (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 128.34 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 19.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.11 | +0.0% | 14.3% |
| IEF | +0.65 | -2.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 165.21 | +28.7% | ±19% |
| base | 45% | 144.31 | +12.4% | ±20% |
| bear | 30% | 99.67 | -22.3% | ±20% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings / guidance surprise | 42% | -6.6% | week of 2025-04-21 (-6.6%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.7% | +0.8% | -14.3% | -5.5% | +7.1% | +15.9% | 46% |
| 6m | +1.9% | +1.8% | -24.7% | -9.8% | +13.4% | +29.6% | 46% |
| 12m | +6.1% | +3.9% | -41.4% | -17.8% | +27.4% | +61.4% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | +1.5% | -0.9% | +0.0% |
| 6m | -0.6% | +3.0% | -1.8% | +0.0% |
| 12m | -1.3% | +6.0% | -3.7% | +0.1% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +6.1% | 46% |
| bull +10pp / bear -10pp | +11.2% | 38% |
| bull -10pp / bear +10pp | +1.0% | 53% |
| residual vol -25% | +6.1% | 45% |
| residual vol +25% | +6.1% | 47% |

Reconciliation: 12m mean +6.08% vs probability-weighted target +6.08%. Every input is cited in the parameters file. A distribution, not a signal.
