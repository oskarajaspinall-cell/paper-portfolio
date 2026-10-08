## Monte Carlo — GRAB (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 3.08 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.30; residual vol 33.3% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.49 | +0.0% | 14.3% |
| IEF | -0.43 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 4.43 | +43.8% | ±7% |
| base | 45% | 3.33 | +8.1% | ±7% |
| bear | 30% | 2.74 | -11.0% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction (Q3 2026, due ~Nov 2, 2026) | 40% | -42.1% | week of 2022-02-28 (-42.1%) |
| Indonesia two-wheel/delivery commission-cap regulatory shock | 30% | -15.0% | none (stated assumption) |
| Atome Financial stake completion / BNPL credit-risk integration | 60% | -8.4% | week of 2026-09-14 (-8.4%) |
| Uber/Delivery Hero combination intensifying foodpanda competition | 15% | -12.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.8% | +3.4% | -41.3% | -9.8% | +16.4% | +35.4% | 43% |
| 6m | +4.3% | +4.3% | -50.0% | -19.0% | +25.8% | +59.9% | 45% |
| 12m | +11.3% | +3.5% | -62.6% | -28.4% | +41.8% | +112.9% | 47% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.5% | +9.2% | -10.8% | +0.0% |
| 6m | +1.0% | +19.2% | -21.9% | +0.0% |
| 12m | +2.3% | +39.0% | -43.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +11.3% | 47% |
| bull +10pp / bear -10pp | +16.8% | 43% |
| bull -10pp / bear +10pp | +5.8% | 51% |
| residual vol -25% | +11.3% | 46% |
| residual vol +25% | +11.3% | 48% |

Reconciliation: 12m mean +11.30% vs probability-weighted target +11.30%. Every input is cited in the parameters file. A distribution, not a signal.
