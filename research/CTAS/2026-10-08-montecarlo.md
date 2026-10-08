## Monte Carlo — CTAS (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 197.19 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.21; residual vol 22.4% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.70 | +0.0% | 14.3% |
| IEF | +0.36 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 219.16 | +11.1% | ±3% |
| base | 45% | 207.51 | +5.2% | ±4% |
| bear | 30% | 181.5 | -8.0% | ±4% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings release surprise | 20% | -11.5% | week of 2024-12-16 (-11.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.6% | -0.1% | -18.9% | -7.8% | +8.5% | +21.8% | 50% |
| 6m | +1.1% | -0.5% | -26.4% | -11.2% | +12.1% | +32.6% | 51% |
| 12m | +2.8% | -0.3% | -35.0% | -16.2% | +18.4% | +50.0% | 51% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | +0.7% | -0.7% | +0.0% |
| 6m | -0.6% | +1.4% | -1.4% | +0.0% |
| 12m | -1.0% | +2.9% | -2.7% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.8% | 51% |
| bull +10pp / bear -10pp | +4.7% | 47% |
| bull -10pp / bear +10pp | +0.8% | 54% |
| residual vol -25% | +2.8% | 48% |
| residual vol +25% | +2.8% | 52% |

Reconciliation: 12m mean +2.75% vs probability-weighted target +2.75%. Every input is cited in the parameters file. A distribution, not a signal.
