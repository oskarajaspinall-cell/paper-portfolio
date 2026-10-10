## Monte Carlo — GDDY (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 98.18 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.15; residual vol 33.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.92 | +0.0% | 14.3% |
| IEF | +0.14 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 142 | +44.6% | ±11% |
| base | 50% | 115 | +17.1% | ±0% |
| bear | 25% | 73 | -25.6% | ±0% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Securities-fraud class actions / promotional-discount disclosure allegations | 33% | -13.6% | week of 2026-03-09 (-13.6%) |
| Quarterly earnings print (next: Oct 29, 2026) | 68% | -11.2% | week of 2026-07-27 (-11.2%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +2.5% | +1.4% | -26.7% | -10.6% | +14.5% | +35.5% | 47% |
| 6m | +5.3% | +2.1% | -36.9% | -15.4% | +23.0% | +57.0% | 47% |
| 12m | +13.3% | +4.8% | -50.5% | -22.2% | +40.2% | +106.1% | 46% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +5.6% | -4.9% | +0.1% |
| 6m | -0.0% | +11.2% | -9.9% | +0.0% |
| 12m | +0.1% | +22.5% | -19.6% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +13.3% | 46% |
| bull +10pp / bear -10pp | +20.3% | 39% |
| bull -10pp / bear +10pp | +6.3% | 52% |
| residual vol -25% | +13.3% | 41% |
| residual vol +25% | +13.3% | 49% |

Reconciliation: 12m mean +13.31% vs probability-weighted target +13.31%. Every input is cited in the parameters file. A distribution, not a signal.
