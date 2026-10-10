## Monte Carlo — JKHY (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 145.69 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.02; residual vol 26.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.20 | +0.0% | 14.3% |
| IEF | +0.06 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 203.0 | +39.3% | ±7% |
| base | 50% | 175.62 | +20.5% | ±12% |
| bear | 25% | 107.21 | -26.4% | ±21% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings-day reaction | 20% | -9.7% | week of 2023-08-14 (-9.7%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +2.5% | +1.4% | -18.1% | -7.2% | +11.2% | +26.2% | 46% |
| 6m | +5.4% | +3.3% | -28.2% | -10.8% | +19.7% | +44.8% | 44% |
| 12m | +13.5% | +9.7% | -43.7% | -15.4% | +38.1% | +83.2% | 40% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +2.1% | -0.6% | +0.0% |
| 6m | -0.0% | +4.1% | -1.1% | +0.0% |
| 12m | +0.0% | +8.3% | -2.2% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +13.5% | 40% |
| bull +10pp / bear -10pp | +20.1% | 32% |
| bull -10pp / bear +10pp | +6.9% | 48% |
| residual vol -25% | +13.5% | 35% |
| residual vol +25% | +13.5% | 44% |

Reconciliation: 12m mean +13.50% vs probability-weighted target +13.50%. Every input is cited in the parameters file. A distribution, not a signal.
