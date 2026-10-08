## Monte Carlo — MO (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 68.55 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.01; residual vol 25.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | -0.10 | +0.0% | 14.3% |
| IEF | +0.31 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 77.06 | +12.4% | ±8% |
| base | 50% | 67.11 | -2.1% | ±10% |
| bear | 30% | 54.7 | -20.2% | ±12% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 82% | -12.8% | week of 2025-10-27 (-12.8%) |
| FDA regulatory/litigation shock (nicotine-alternative approvals or adverse ruling) | 30% | -15.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.4% | -0.5% | -22.3% | -9.2% | +7.2% | +16.4% | 52% |
| 6m | -2.9% | -3.2% | -31.8% | -15.2% | +8.9% | +26.6% | 57% |
| 12m | -4.6% | -7.3% | -44.7% | -23.9% | +12.2% | +43.8% | 60% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +5.5% | -7.3% | +0.0% |
| 6m | -0.8% | +11.0% | -14.9% | +0.0% |
| 12m | -1.6% | +22.0% | -29.4% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -4.6% | 60% |
| bull +10pp / bear -10pp | -1.4% | 55% |
| bull -10pp / bear +10pp | -7.9% | 65% |
| residual vol -25% | -4.6% | 60% |
| residual vol +25% | -4.6% | 62% |

Reconciliation: 12m mean -4.63% vs probability-weighted target -4.63%. Every input is cited in the parameters file. A distribution, not a signal.
