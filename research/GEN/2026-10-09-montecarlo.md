## Monte Carlo — GEN (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 22.75 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.15; residual vol 38.9% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.96 | +0.0% | 14.3% |
| IEF | +0.33 | -2.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 42.0 | +84.6% | ±8% |
| base | 45% | 29.0 | +27.5% | ±11% |
| bear | 30% | 18.0 | -20.9% | ±22% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction miss | 25% | -10.7% | week of 2024-01-29 (-10.7%) |
| Leverage / credit-stress re-rating | 10% | -20.0% | none (stated assumption) |
| Repeat of an unexplained single-week price shock | 20% | -25.5% | week of 2026-09-21 (-25.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +5.0% | +3.1% | -27.8% | -10.5% | +18.4% | +44.1% | 44% |
| 6m | +10.9% | +5.6% | -39.1% | -14.9% | +31.1% | +78.7% | 43% |
| 12m | +27.3% | +12.4% | -53.3% | -21.6% | +59.9% | +157.1% | 41% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.2% | +5.8% | -3.1% | +0.1% |
| 6m | -0.4% | +11.6% | -6.2% | +0.0% |
| 12m | -0.6% | +23.3% | -12.4% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +27.3% | 41% |
| bull +10pp / bear -10pp | +37.8% | 35% |
| bull -10pp / bear +10pp | +16.7% | 48% |
| residual vol -25% | +27.3% | 37% |
| residual vol +25% | +27.3% | 46% |

Reconciliation: 12m mean +27.25% vs probability-weighted target +27.25%. Every input is cited in the parameters file. A distribution, not a signal.
