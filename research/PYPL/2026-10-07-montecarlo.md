## Monte Carlo — PYPL (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 54.61 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.18; residual vol 39.9% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.14 | +6.0% | 14.3% |
| IEF | -0.02 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 22% | 75.38 | +38.0% | ±13% |
| base | 48% | 58.89 | +7.8% | ±17% |
| bear | 30% | 47.53 | -13.0% | ±21% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 94% | -23.3% | week of 2026-02-02 (-23.3%) |
| Takeover speculation collapse | 30% | -15.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.5% | +1.6% | -39.3% | -16.0% | +19.2% | +42.2% | 48% |
| 6m | +2.9% | -0.8% | -52.2% | -25.1% | +26.4% | +70.7% | 51% |
| 12m | +8.2% | -4.3% | -65.5% | -36.3% | +38.1% | +126.5% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +1.6% | +16.1% | -19.5% | +0.0% |
| 6m | +3.3% | +32.2% | -39.7% | +0.0% |
| 12m | +6.8% | +64.4% | -79.2% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +8.2% | 53% |
| bull +10pp / bear -10pp | +13.3% | 50% |
| bull -10pp / bear +10pp | +3.1% | 56% |
| residual vol -25% | +8.2% | 53% |
| residual vol +25% | +8.2% | 54% |

Reconciliation: 12m mean +8.24% vs probability-weighted target +8.24%. Every input is cited in the parameters file. A distribution, not a signal.
