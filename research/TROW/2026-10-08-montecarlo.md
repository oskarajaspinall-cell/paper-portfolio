## Monte Carlo — TROW (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 104.07 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.46; residual vol 18.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.10 | +0.0% | 14.3% |
| IEF | +0.34 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 138 | +32.6% | ±7% |
| base | 45% | 110 | +5.7% | ±11% |
| bear | 30% | 85 | -18.3% | ±15% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings / AUM report surprise | 25% | -10.5% | week of 2026-02-02 (-10.5%) |
| Net-outflow / AUM disclosure shock | 20% | -10.5% | week of 2022-09-12 (-10.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.8% | +0.1% | -18.2% | -7.6% | +8.4% | +22.0% | 50% |
| 6m | +1.8% | +0.0% | -26.6% | -11.7% | +13.3% | +35.4% | 50% |
| 12m | +5.2% | +1.0% | -39.3% | -18.2% | +23.9% | +64.5% | 49% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +1.5% | -1.5% | +0.0% |
| 6m | -0.0% | +3.0% | -2.9% | +0.0% |
| 12m | +0.1% | +6.0% | -5.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +5.2% | 49% |
| bull +10pp / bear -10pp | +10.3% | 42% |
| bull -10pp / bear +10pp | +0.1% | 55% |
| residual vol -25% | +5.2% | 47% |
| residual vol +25% | +5.2% | 50% |

Reconciliation: 12m mean +5.22% vs probability-weighted target +5.22%. Every input is cited in the parameters file. A distribution, not a signal.
