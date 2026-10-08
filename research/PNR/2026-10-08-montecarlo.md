## Monte Carlo — PNR (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 52.19 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.30; residual vol 27.9% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.06 | +0.0% | 14.3% |
| IEF | +0.52 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 61.35 | +17.6% | ±25% |
| base | 40% | 52.0 | -0.4% | ±1% |
| bear | 35% | 37.7 | -27.8% | ±22% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Severe earnings/guidance shock (Q3 2026 report, 2026-10-20) | 20% | -18.0% | week of 2026-07-13 (-18.0%) |
| Securities class-action / governance shock | 15% | -10.0% | none (stated assumption) |
| Leverage / M&A integration shock (Taco Group Holdings) | 20% | -3.1% | week of 2022-02-28 (-3.1%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -2.2% | -3.0% | -25.2% | -12.2% | +7.0% | +23.2% | 59% |
| 6m | -3.9% | -6.1% | -37.1% | -19.9% | +9.8% | +36.9% | 61% |
| 12m | -5.5% | -11.4% | -53.9% | -31.7% | +14.9% | +62.8% | 62% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | -1.2% | -1.8% | +0.0% |
| 6m | -0.8% | -2.4% | -3.5% | +0.0% |
| 12m | -1.5% | -4.9% | -6.9% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | -5.5% | 62% |
| bull +10pp / bear -10pp | -0.9% | 57% |
| bull -10pp / bear +10pp | -10.0% | 68% |
| residual vol -25% | -5.5% | 62% |
| residual vol +25% | -5.5% | 63% |

Reconciliation: 12m mean -5.48% vs probability-weighted target -5.48%. Every input is cited in the parameters file. A distribution, not a signal.
