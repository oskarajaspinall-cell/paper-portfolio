## Monte Carlo — HCA (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 445.01 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 27.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.39 | +0.0% | 14.3% |
| IEF | +0.48 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 571.97 | +28.5% | ±21% |
| base | 50% | 404.48 | -9.1% | ±2% |
| bear | 30% | 298.05 | -33.0% | ±21% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction (ACA-exchange/payer-mix headwind) | 100% | -11.4% | week of 2026-04-20 (-11.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -3.0% | -3.4% | -18.4% | -9.5% | +3.1% | +14.0% | 64% |
| 6m | -5.5% | -6.8% | -30.6% | -16.2% | +3.6% | +24.1% | 67% |
| 12m | -8.8% | -12.6% | -49.0% | -26.8% | +3.2% | +50.2% | 71% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +758.2% | -761.1% | +0.0% |
| 6m | -1.2% | +1516.3% | -1522.2% | +0.0% |
| 12m | -2.4% | +3032.7% | -3044.5% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -8.8% | 71% |
| bull +10pp / bear -10pp | -2.6% | 63% |
| bull -10pp / bear +10pp | -14.9% | 79% |
| residual vol -25% | -8.8% | 73% |
| residual vol +25% | -8.8% | 70% |

Reconciliation: 12m mean -8.76% vs probability-weighted target -8.76%. Every input is cited in the parameters file. A distribution, not a signal.
