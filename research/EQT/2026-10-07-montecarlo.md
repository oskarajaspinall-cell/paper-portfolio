## Monte Carlo — EQT (2026-10-07)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 52.47 USD (close 2026-10-06).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 32.5% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.52 | +0.0% | 14.3% |
| IEF | -0.43 | +0.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 73.5 | +40.1% | ±18% |
| base | 50% | 55.5 | +5.8% | ±24% |
| bear | 30% | 45.0 | -14.2% | ±1% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings beat/miss shock (gas-price driven) | 20% | -11.8% | week of 2025-07-21 (-11.8%) |
| Extreme Appalachian gas-price / basis-differential shock | 20% | -25.1% | week of 2022-06-13 (-25.1%) |
| Equity-funded M&A / dilution surprise | 40% | -10.9% | week of 2024-03-11 (-10.9%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.8% | +1.0% | -25.0% | -8.8% | +10.7% | +25.3% | 47% |
| 6m | +2.1% | +0.8% | -35.0% | -14.4% | +17.2% | +43.8% | 49% |
| 12m | +6.6% | +0.1% | -48.8% | -23.6% | +29.6% | +85.4% | 50% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +3.6% | -4.0% | +0.1% |
| 6m | -0.1% | +7.2% | -7.8% | +0.0% |
| 12m | +0.0% | +14.4% | -15.6% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +6.6% | 50% |
| bull +10pp / bear -10pp | +12.1% | 44% |
| bull -10pp / bear +10pp | +1.2% | 55% |
| residual vol -25% | +6.6% | 49% |
| residual vol +25% | +6.6% | 53% |

Reconciliation: 12m mean +6.63% vs probability-weighted target +6.63%. Every input is cited in the parameters file. A distribution, not a signal.
