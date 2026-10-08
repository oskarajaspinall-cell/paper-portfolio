## Monte Carlo — CTSH (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 57.07 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.16; residual vol 37.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.89 | +0.0% | 14.3% |
| IEF | +0.26 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 70.0 | +22.7% | ±12% |
| base | 45% | 59.0 | +3.4% | ±0% |
| bear | 30% | 45.0 | -21.1% | ±9% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings deterioration surprise | 20% | -16.5% | week of 2022-10-31 (-16.5%) |
| Debt-funded bolt-on M&A announcement | 20% | -2.5% | week of 2024-06-10 (-2.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.2% | -1.9% | -29.6% | -13.7% | +11.9% | +34.4% | 54% |
| 6m | -0.3% | -4.1% | -41.1% | -20.5% | +15.7% | +51.8% | 56% |
| 12m | +0.8% | -7.3% | -54.2% | -30.6% | +23.0% | +82.6% | 57% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | -1.0% | -1.2% | +0.1% |
| 6m | -0.0% | -2.0% | -2.3% | +0.0% |
| 12m | +0.1% | -4.1% | -4.6% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +0.8% | 57% |
| bull +10pp / bear -10pp | +5.2% | 53% |
| bull -10pp / bear +10pp | -3.5% | 61% |
| residual vol -25% | +0.8% | 55% |
| residual vol +25% | +0.8% | 59% |

Reconciliation: 12m mean +0.84% vs probability-weighted target +0.84%. Every input is cited in the parameters file. A distribution, not a signal.
