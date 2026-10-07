## Monte Carlo — FSLR (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 179.8 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.09; residual vol 50.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.03 | +6.0% | 14.3% |
| IEF | +0.83 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 236.0 | +31.3% | ±1% |
| base | 45% | 180.0 | +0.1% | ±0% |
| bear | 30% | 143.0 | -20.5% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reset | 35% | -18.5% | week of 2026-02-23 (-18.5%) |
| Tariff / Section 232 polysilicon policy shock | 40% | -20.0% | none (stated assumption) |
| Securities class action & patent litigation overhang | 15% | -12.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.0% | -3.0% | -38.5% | -18.7% | +16.1% | +46.9% | 55% |
| 6m | -0.1% | -6.5% | -51.3% | -27.5% | +20.5% | +71.4% | 57% |
| 12m | +1.7% | -12.4% | -66.1% | -39.8% | +26.9% | +116.0% | 60% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.9% | +1.2% | -5.7% | +0.1% |
| 6m | +1.7% | +2.4% | -11.5% | +0.0% |
| 12m | +3.6% | +4.9% | -22.8% | +0.6% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.7% | 60% |
| bull +10pp / bear -10pp | +6.9% | 56% |
| bull -10pp / bear +10pp | -3.4% | 63% |
| residual vol -25% | +1.7% | 57% |
| residual vol +25% | +1.7% | 62% |

Reconciliation: 12m mean +1.72% vs probability-weighted target +1.72%. Every input is cited in the parameters file. A distribution, not a signal.
