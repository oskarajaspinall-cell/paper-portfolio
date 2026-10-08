## Monte Carlo — CCL (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 26.15 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.28; residual vol 40.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.70 | +0.0% | 14.3% |
| IEF | +0.47 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 34.03 | +30.1% | ±17% |
| base | 45% | 27.74 | +6.1% | ±6% |
| bear | 30% | 21.45 | -18.0% | ±8% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings surprise | 68% | -21.4% | week of 2022-09-26 (-21.4%) |
| Market-wide risk-off shock (VIX spike) | 70% | -18.3% | week of 2026-03-02 (-18.3%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +1.1% | +0.1% | -35.5% | -14.8% | +16.2% | +40.6% | 50% |
| 6m | +1.7% | -2.4% | -47.5% | -23.2% | +22.5% | +64.1% | 53% |
| 12m | +4.9% | -6.4% | -61.2% | -33.8% | +31.2% | +108.8% | 55% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.6% | +11.9% | -13.0% | +0.0% |
| 6m | -1.3% | +23.3% | -26.2% | +0.0% |
| 12m | -2.3% | +46.0% | -52.1% | +0.3% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +4.9% | 55% |
| bull +10pp / bear -10pp | +9.7% | 52% |
| bull -10pp / bear +10pp | +0.1% | 59% |
| residual vol -25% | +4.9% | 55% |
| residual vol +25% | +4.9% | 57% |

Reconciliation: 12m mean +4.88% vs probability-weighted target +4.88%. Every input is cited in the parameters file. A distribution, not a signal.
