## Monte Carlo — AMP (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 496.61 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.38; residual vol 22.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.11 | -2.0% | 14.3% |
| IEF | -0.53 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 629.0 | +26.7% | ±7% |
| base | 45% | 529.7 | +6.7% | ±5% |
| bear | 35% | 409.7 | -17.5% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 76% | -5.5% | week of 2025-10-27 (-5.5%) |
| Advisor attrition / negative investor-disclosure shock | 60% | -12.5% | week of 2026-02-09 (-12.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.1% | -0.3% | -22.2% | -9.5% | +9.3% | +23.9% | 51% |
| 6m | +0.3% | -0.9% | -31.0% | -14.4% | +13.3% | +36.8% | 52% |
| 12m | +2.2% | -2.4% | -43.1% | -21.4% | +20.8% | +63.8% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.1% | +4.4% | -5.2% | +0.0% |
| 6m | -0.1% | +8.8% | -10.5% | +0.0% |
| 12m | +0.0% | +17.5% | -20.6% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.2% | 53% |
| bull +10pp / bear -10pp | +6.6% | 47% |
| bull -10pp / bear +10pp | -2.2% | 59% |
| residual vol -25% | +2.2% | 52% |
| residual vol +25% | +2.2% | 54% |

Reconciliation: 12m mean +2.20% vs probability-weighted target +2.20%. Every input is cited in the parameters file. A distribution, not a signal.
