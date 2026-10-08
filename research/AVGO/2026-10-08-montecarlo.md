## Monte Carlo — AVGO (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 376.51 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.49; residual vol 33.2% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +2.44 | +0.0% | 14.3% |
| IEF | -0.55 | -4.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 495.0 | +31.5% | ±22% |
| base | 45% | 376.51 | +0.0% | ±21% |
| bear | 30% | 289.96 | -23.0% | ±20% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 48% | -15.9% | week of 2024-09-03 (-15.9%) |
| AI-chip debt-financing confirmation shock | 60% | -15.0% | none (stated assumption) |
| Market-wide risk-off shock (VIX spike) | 70% | -13.5% | week of 2025-03-31 (-13.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -0.7% | -3.1% | -36.3% | -17.2% | +13.9% | +42.6% | 55% |
| 6m | -1.2% | -6.3% | -49.8% | -27.3% | +19.1% | +66.0% | 57% |
| 12m | +1.0% | -13.2% | -65.5% | -39.8% | +27.0% | +114.4% | 60% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.5% | +6.8% | -10.9% | +0.0% |
| 6m | +0.9% | +13.5% | -22.1% | +0.0% |
| 12m | +2.4% | +27.0% | -44.0% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.0% | 60% |
| bull +10pp / bear -10pp | +6.4% | 56% |
| bull -10pp / bear +10pp | -4.5% | 64% |
| residual vol -25% | +1.0% | 60% |
| residual vol +25% | +1.0% | 61% |

Reconciliation: 12m mean +0.97% vs probability-weighted target +0.97%. Every input is cited in the parameters file. A distribution, not a signal.
