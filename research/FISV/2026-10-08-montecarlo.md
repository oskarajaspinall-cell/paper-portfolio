## Monte Carlo — FISV (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 45.31 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.03; residual vol 58.1% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.54 | +0.0% | 14.3% |
| IEF | +0.44 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 54.2 | +19.6% | ±23% |
| base | 45% | 47.7 | +5.3% | ±8% |
| bear | 30% | 36.0 | -20.5% | ±27% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction (Q3 2026, Nov 3) | 20% | -46.7% | week of 2025-10-27 (-46.7%) |
| Leverage / credit-distress shock | 80% | -10.1% | week of 2026-03-09 (-10.1%) |
| Activist / governance escalation | 100% | -4.6% | week of 2026-09-28 (-4.6%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.0% | -2.2% | -40.5% | -17.3% | +14.3% | +41.4% | 54% |
| 6m | -1.0% | -5.2% | -54.4% | -26.9% | +19.8% | +65.7% | 56% |
| 12m | +1.1% | -10.5% | -69.0% | -40.1% | +29.5% | +108.8% | 58% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | +0.0% | +297.4% | -302.0% | +0.1% |
| 6m | -0.0% | +595.5% | -603.9% | +0.0% |
| 12m | +0.1% | +1191.6% | -1207.4% | +0.6% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.1% | 58% |
| bull +10pp / bear -10pp | +5.1% | 55% |
| bull -10pp / bear +10pp | -2.9% | 61% |
| residual vol -25% | +1.1% | 53% |
| residual vol +25% | +1.1% | 62% |

Reconciliation: 12m mean +1.11% vs probability-weighted target +1.11%. Every input is cited in the parameters file. A distribution, not a signal.
