## Monte Carlo — DPZ (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 302.87 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.17; residual vol 26.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.66 | +0.0% | 14.3% |
| IEF | +0.99 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 376 | +24.1% | ±17% |
| base | 50% | 310 | +2.4% | ±20% |
| bear | 30% | 259 | -14.5% | ±24% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 61% | -17.8% | week of 2024-07-15 (-17.8%) |
| Franchisee-system distress (accelerating beyond the current ~13-store closure) | 15% | -12.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.1% | +0.4% | -24.3% | -9.1% | +9.2% | +22.1% | 49% |
| 6m | -0.1% | -1.0% | -34.7% | -15.3% | +14.0% | +36.8% | 52% |
| 12m | +1.7% | -1.9% | -50.4% | -24.5% | +22.8% | +67.5% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -1.2% | +5.1% | -5.1% | +0.0% |
| 6m | -2.5% | +10.2% | -10.3% | +0.0% |
| 12m | -5.0% | +20.4% | -20.6% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.7% | 52% |
| bull +10pp / bear -10pp | +5.5% | 48% |
| bull -10pp / bear +10pp | -2.2% | 56% |
| residual vol -25% | +1.7% | 52% |
| residual vol +25% | +1.7% | 53% |

Reconciliation: 12m mean +1.66% vs probability-weighted target +1.66%. Every input is cited in the parameters file. A distribution, not a signal.
