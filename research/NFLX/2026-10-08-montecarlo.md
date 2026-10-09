## Monte Carlo — NFLX (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 69.7 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.17; residual vol 33.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.99 | +0.0% | 14.3% |
| IEF | -0.11 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 92.5 | +32.7% | ±30% |
| base | 40% | 64.74 | -7.1% | ±24% |
| bear | 35% | 46.83 | -32.8% | ±30% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings (Oct 20) confirms growth deceleration | 40% | -24.4% | week of 2022-01-18 (-24.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -3.1% | -2.9% | -31.0% | -13.8% | +7.6% | +24.3% | 58% |
| 6m | -5.2% | -7.5% | -45.3% | -23.9% | +11.3% | +42.4% | 61% |
| 12m | -6.2% | -14.9% | -65.3% | -39.1% | +17.5% | +84.6% | 63% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.1% | -1.4% | -3.5% | +0.0% |
| 6m | +0.2% | -2.7% | -7.0% | +0.0% |
| 12m | +0.6% | -5.5% | -14.1% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -6.2% | 63% |
| bull +10pp / bear -10pp | +0.4% | 58% |
| bull -10pp / bear +10pp | -12.7% | 69% |
| residual vol -25% | -6.2% | 63% |
| residual vol +25% | -6.2% | 64% |

Reconciliation: 12m mean -6.15% vs probability-weighted target -6.15%. Every input is cited in the parameters file. A distribution, not a signal.
