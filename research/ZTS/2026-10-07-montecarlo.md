## Monte Carlo — ZTS (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 71.33 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.08; residual vol 37.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.48 | +5.0% | 14.3% |
| IEF | +0.83 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 115 | +61.2% | ±8% |
| base | 50% | 83 | +16.4% | ±3% |
| bear | 30% | 58 | -18.7% | ±16% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings / guidance-cut risk (Q3 2026, Nov 5 2026) | 20% | -27.4% | week of 2026-05-04 (-27.4%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +2.4% | +0.9% | -27.4% | -10.7% | +14.5% | +36.5% | 48% |
| 6m | +5.7% | +1.9% | -37.9% | -15.5% | +23.2% | +60.9% | 47% |
| 12m | +14.8% | +4.6% | -50.7% | -22.8% | +41.4% | +115.4% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.2% | +2.5% | -1.8% | +0.1% |
| 6m | -0.5% | +5.5% | -3.6% | +0.0% |
| 12m | -1.0% | +11.5% | -7.0% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +14.8% | 46% |
| bull +10pp / bear -10pp | +22.8% | 40% |
| bull -10pp / bear +10pp | +6.8% | 52% |
| residual vol -25% | +14.8% | 42% |
| residual vol +25% | +14.8% | 50% |

Reconciliation: 12m mean +14.82% vs probability-weighted target +14.82%. Every input is cited in the parameters file. A distribution, not a signal.
