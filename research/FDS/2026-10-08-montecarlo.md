## Monte Carlo — FDS (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 272.78 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.08; residual vol 39.0% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.56 | +0.0% | 14.3% |
| IEF | +0.76 | -3.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 315 | +15.5% | ±2% |
| base | 45% | 285 | +4.5% | ±0% |
| bear | 30% | 240 | -12.0% | ±7% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Earnings-day margin miss | 34% | -20.1% | week of 2025-09-15 (-20.1%) |
| AI-competitive disruption shock (unscheduled) | 45% | -18.5% | week of 2026-02-02 (-18.5%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.1% | -1.0% | -30.8% | -13.5% | +12.8% | +33.4% | 52% |
| 6m | +0.4% | -2.6% | -40.9% | -19.8% | +17.2% | +51.5% | 54% |
| 12m | +2.3% | -5.2% | -53.6% | -28.3% | +25.2% | +81.2% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +4.1% | -5.5% | +0.1% |
| 6m | -1.1% | +8.6% | -11.2% | +0.0% |
| 12m | -2.2% | +17.6% | -22.0% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +2.3% | 55% |
| bull +10pp / bear -10pp | +5.0% | 52% |
| bull -10pp / bear +10pp | -0.5% | 58% |
| residual vol -25% | +2.3% | 52% |
| residual vol +25% | +2.3% | 58% |

Reconciliation: 12m mean +2.28% vs probability-weighted target +2.28%. Every input is cited in the parameters file. A distribution, not a signal.
