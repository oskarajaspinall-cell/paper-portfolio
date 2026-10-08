## Monte Carlo — STZ (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 115.67 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 28.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.41 | +4.0% | 14.3% |
| IEF | +0.27 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 161 | +39.2% | ±6% |
| base | 50% | 124 | +7.2% | ±4% |
| bear | 30% | 88 | -23.9% | ±8% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings/guidance miss | 20% | -18.1% | week of 2025-01-06 (-18.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.0% | -0.8% | -23.2% | -10.0% | +9.5% | +25.4% | 52% |
| 6m | +0.9% | -1.4% | -32.9% | -15.0% | +14.8% | +41.3% | 52% |
| 12m | +4.3% | -1.6% | -46.0% | -23.0% | +25.3% | +74.1% | 52% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.2% | -0.2% | -1.1% | +0.1% |
| 6m | +0.4% | +0.2% | -2.2% | +0.0% |
| 12m | +0.8% | +1.1% | -4.4% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +4.3% | 52% |
| bull +10pp / bear -10pp | +10.6% | 44% |
| bull -10pp / bear +10pp | -2.0% | 58% |
| residual vol -25% | +4.3% | 49% |
| residual vol +25% | +4.3% | 54% |

Reconciliation: 12m mean +4.26% vs probability-weighted target +4.26%. Every input is cited in the parameters file. A distribution, not a signal.
