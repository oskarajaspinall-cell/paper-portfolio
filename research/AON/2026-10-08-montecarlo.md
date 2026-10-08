## Monte Carlo — AON (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 270.47 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.06; residual vol 23.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.33 | +0.0% | 14.3% |
| IEF | +0.35 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 372 | +37.5% | ±12% |
| base | 45% | 275 | +1.7% | ±21% |
| bear | 35% | 230 | -15.0% | ±3% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction (ahead of USI close) | 80% | -10.3% | week of 2022-04-25 (-10.3%) |
| USI deal regulatory approval / closing disruption | 40% | -9.1% | week of 2026-08-31 (-9.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.2% | +0.3% | -19.3% | -7.8% | +8.2% | +19.5% | 49% |
| 6m | +0.6% | -0.7% | -28.3% | -12.8% | +12.8% | +33.4% | 51% |
| 12m | +3.0% | -2.3% | -41.9% | -20.7% | +21.8% | +66.2% | 53% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.3% | +5.4% | -5.6% | +0.0% |
| 6m | -0.7% | +10.8% | -11.4% | +0.0% |
| 12m | -1.4% | +21.6% | -22.4% | +0.1% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +3.0% | 53% |
| bull +10pp / bear -10pp | +8.3% | 46% |
| bull -10pp / bear +10pp | -2.2% | 60% |
| residual vol -25% | +3.0% | 54% |
| residual vol +25% | +3.0% | 53% |

Reconciliation: 12m mean +3.02% vs probability-weighted target +3.02%. Every input is cited in the parameters file. A distribution, not a signal.
