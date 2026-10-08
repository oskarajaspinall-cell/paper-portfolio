## Monte Carlo — CF (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 116.02 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 34.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | -0.14 | +0.0% | 14.3% |
| IEF | -1.06 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 140 | +20.7% | ±19% |
| base | 45% | 108 | -6.9% | ±25% |
| bear | 30% | 85 | -26.7% | ±31% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings miss | 30% | -8.7% | week of 2026-08-03 (-8.7%) |
| Trade-policy shock to fertilizer pricing (Belarus potash deal) | 100% | -10.2% | week of 2026-09-21 (-10.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -2.6% | -2.6% | -22.7% | -10.9% | +5.7% | +18.0% | 59% |
| 6m | -4.4% | -5.0% | -36.9% | -18.3% | +8.8% | +29.8% | 60% |
| 12m | -6.0% | -9.4% | -57.1% | -30.4% | +15.0% | +56.2% | 61% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +675.1% | -678.6% | +0.0% |
| 6m | -0.1% | +1350.3% | -1357.2% | +0.0% |
| 12m | -0.1% | +2700.6% | -2714.4% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -6.0% | 61% |
| bull +10pp / bear -10pp | -1.2% | 55% |
| bull -10pp / bear +10pp | -10.7% | 66% |
| residual vol -25% | -6.0% | 60% |
| residual vol +25% | -6.0% | 61% |

Reconciliation: 12m mean -5.96% vs probability-weighted target -5.96%. Every input is cited in the parameters file. A distribution, not a signal.
