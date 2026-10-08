## Monte Carlo — ALL (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 224.27 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 23.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.33 | +4.0% | 14.3% |
| IEF | +0.20 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 30% | 299.03 | +33.3% | ±23% |
| base | 45% | 249.19 | +11.1% | ±17% |
| bear | 25% | 161.97 | -27.8% | ±23% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction | 60% | -5.3% | week of 2021-11-01 (-5.3%) |
| Severe catastrophe-loss quarter (hurricane/wildfire cluster) | 50% | -9.3% | week of 2022-10-17 (-9.3%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.0% | +1.1% | -17.7% | -6.9% | +8.7% | +20.0% | 46% |
| 6m | +2.5% | +1.8% | -29.0% | -11.1% | +15.7% | +35.9% | 46% |
| 12m | +8.1% | +4.8% | -46.8% | -19.1% | +30.9% | +74.7% | 45% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.1% | +3.2% | -3.0% | +0.0% |
| 6m | +0.2% | +6.4% | -6.0% | +0.0% |
| 12m | +0.5% | +12.7% | -11.9% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +8.1% | 45% |
| bull +10pp / bear -10pp | +14.2% | 38% |
| bull -10pp / bear +10pp | +1.9% | 52% |
| residual vol -25% | +8.1% | 44% |
| residual vol +25% | +8.1% | 47% |

Reconciliation: 12m mean +8.06% vs probability-weighted target +8.06%. Every input is cited in the parameters file. A distribution, not a signal.
