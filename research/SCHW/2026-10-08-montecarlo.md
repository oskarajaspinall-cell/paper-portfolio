## Monte Carlo — SCHW (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 95.58 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.22; residual vol 23.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.92 | +0.0% | 14.3% |
| IEF | -0.09 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 113.0 | +18.2% | ±20% |
| base | 43% | 93.55 | -2.1% | ±6% |
| bear | 32% | 69.64 | -27.1% | ±10% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Q3 2026 earnings reaction (Oct 15) | 34% | -17.6% | week of 2024-07-15 (-17.6%) |
| Banking-sector deposit-flight / AFS-HTM mark-to-market shock | 20% | -24.2% | week of 2023-03-06 (-24.2%) |
| AI/fintech competitive disruption (Vanguard) | 50% | -5.9% | week of 2026-09-21 (-5.9%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.8% | -1.2% | -25.0% | -9.9% | +6.9% | +19.0% | 54% |
| 6m | -3.4% | -4.2% | -34.5% | -17.1% | +9.5% | +31.2% | 59% |
| 12m | -5.0% | -9.7% | -49.6% | -28.2% | +12.7% | +56.1% | 62% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.1% | +1.8% | -4.7% | +0.0% |
| 6m | +0.2% | +3.6% | -9.5% | +0.0% |
| 12m | +0.5% | +7.2% | -18.9% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -5.0% | 62% |
| bull +10pp / bear -10pp | -0.5% | 56% |
| bull -10pp / bear +10pp | -9.6% | 67% |
| residual vol -25% | -5.0% | 62% |
| residual vol +25% | -5.0% | 62% |

Reconciliation: 12m mean -5.04% vs probability-weighted target -5.04%. Every input is cited in the parameters file. A distribution, not a signal.
