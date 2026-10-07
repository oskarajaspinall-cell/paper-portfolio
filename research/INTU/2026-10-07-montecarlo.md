## Monte Carlo — INTU (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 289.81 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.07; residual vol 44.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.68 | +0.0% | 14.3% |
| IEF | +0.19 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 368 | +27.0% | ±24% |
| base | 50% | 326 | +12.5% | ±1% |
| bear | 25% | 233 | -19.6% | ±10% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings/guidance miss (FY2027 reset) | 19% | -18.6% | week of 2026-05-18 (-18.6%) |
| AI-native disruption / price-driven DIY tax churn disclosed at Investor Day | 15% | -30.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.8% | +0.2% | -32.6% | -13.5% | +15.6% | +41.1% | 50% |
| 6m | +3.2% | -0.7% | -44.3% | -19.9% | +22.0% | +63.2% | 51% |
| 12m | +8.1% | -2.9% | -58.6% | -30.0% | +35.3% | +108.5% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +1.9% | -2.7% | +0.1% |
| 6m | -0.0% | +3.3% | -5.4% | +0.0% |
| 12m | +0.1% | +6.2% | -10.6% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +8.1% | 52% |
| bull +10pp / bear -10pp | +12.7% | 48% |
| bull -10pp / bear +10pp | +3.4% | 56% |
| residual vol -25% | +8.1% | 48% |
| residual vol +25% | +8.1% | 56% |

Reconciliation: 12m mean +8.09% vs probability-weighted target +8.09%. Every input is cited in the parameters file. A distribution, not a signal.
