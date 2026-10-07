## Monte Carlo — DECK (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 81.66 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.17; residual vol 39.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.24 | +0.0% | 14.3% |
| IEF | +0.30 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 35% | 106.2 | +30.1% | ±3% |
| base | 45% | 86.33 | +5.7% | ±0% |
| bear | 20% | 64.75 | -20.7% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings print (Oct 22, 2026 and subsequent quarters) | 90% | -21.0% | week of 2025-05-19 (-21.0%) |
| Retail-partner concentration / promotional reset | 63% | -14.6% | week of 2022-02-28 (-14.6%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.9% | +1.5% | -35.8% | -14.0% | +17.7% | +39.7% | 47% |
| 6m | +3.5% | +0.4% | -47.3% | -21.2% | +24.8% | +63.7% | 50% |
| 12m | +8.9% | -0.8% | -59.4% | -30.1% | +37.0% | +112.4% | 51% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +16.4% | -17.4% | +0.0% |
| 6m | -0.1% | +32.9% | -35.1% | +0.0% |
| 12m | +0.1% | +65.7% | -69.7% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +8.9% | 51% |
| bull +10pp / bear -10pp | +14.0% | 47% |
| bull -10pp / bear +10pp | +3.9% | 55% |
| residual vol -25% | +8.9% | 50% |
| residual vol +25% | +8.9% | 53% |

Reconciliation: 12m mean +8.95% vs probability-weighted target +8.95%. Every input is cited in the parameters file. A distribution, not a signal.
