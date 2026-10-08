## Monte Carlo — PGR (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 212.05 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 24.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.35 | +4.0% | 14.3% |
| IEF | -0.31 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 242 | +14.1% | ±1% |
| base | 45% | 212 | -0.0% | ±0% |
| bear | 30% | 194 | -8.5% | ±5% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction | 60% | -5.0% | week of 2023-05-01 (-5.0%) |
| Monthly operating-results miss (core loss ratio surprise) | 50% | -8.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.1% | -0.4% | -19.6% | -8.6% | +8.1% | +21.9% | 51% |
| 6m | +0.1% | -1.2% | -27.6% | -12.6% | +11.5% | +32.1% | 53% |
| 12m | +1.0% | -2.3% | -37.0% | -18.3% | +16.6% | +50.7% | 54% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.6% | +1.3% | -2.7% | +0.1% |
| 6m | +1.3% | +2.6% | -5.4% | +0.0% |
| 12m | +2.7% | +5.1% | -10.7% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.0% | 54% |
| bull +10pp / bear -10pp | +3.2% | 50% |
| bull -10pp / bear +10pp | -1.3% | 57% |
| residual vol -25% | +1.0% | 52% |
| residual vol +25% | +1.0% | 55% |

Reconciliation: 12m mean +0.97% vs probability-weighted target +0.97%. Every input is cited in the parameters file. A distribution, not a signal.
