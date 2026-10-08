## Monte Carlo — LULU (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 93.61 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.11; residual vol 40.8% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.02 | +0.0% | 14.3% |
| IEF | +0.07 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 135 | +44.2% | ±22% |
| base | 45% | 90 | -3.9% | ±0% |
| bear | 30% | 65 | -30.6% | ±26% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings print | 88% | -17.0% | week of 2025-09-02 (-17.0%) |
| Securities-fraud investigation / litigation escalation | 35% | -15.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.0% | -2.0% | -33.6% | -15.5% | +12.8% | +35.0% | 54% |
| 6m | -1.7% | -5.3% | -47.2% | -24.8% | +17.3% | +56.5% | 57% |
| 12m | +0.1% | -11.3% | -64.2% | -37.2% | +24.6% | +104.3% | 59% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +8.2% | -11.6% | +0.1% |
| 6m | -0.1% | +16.3% | -23.4% | +0.0% |
| 12m | +0.1% | +32.7% | -46.4% | +0.4% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +0.1% | 59% |
| bull +10pp / bear -10pp | +7.6% | 54% |
| bull -10pp / bear +10pp | -7.3% | 65% |
| residual vol -25% | +0.1% | 58% |
| residual vol +25% | +0.1% | 61% |

Reconciliation: 12m mean +0.15% vs probability-weighted target +0.15%. Every input is cited in the parameters file. A distribution, not a signal.
