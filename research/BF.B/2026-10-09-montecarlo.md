## Monte Carlo — BF.B (2026-10-09)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 26.54 USD (close 2026-10-08).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.05; residual vol 35.7% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +0.49 | +0.0% | 14.3% |
| IEF | +0.29 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 20% | 33.95 | +27.9% | ±36% |
| base | 50% | 27.5 | +3.6% | ±26% |
| bear | 30% | 21.0 | -20.9% | ±36% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings miss / guidance disappointment | 100% | -15.7% | week of 2025-06-02 (-15.7%) |
| US-Canada trade war / tariff escalation on spirits | 100% | -4.3% | week of 2026-08-24 (-4.3%) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | -1.1% | -1.2% | -22.8% | -9.9% | +7.3% | +21.7% | 54% |
| 6m | -1.3% | -2.2% | -37.8% | -16.5% | +13.0% | +37.7% | 54% |
| 12m | +1.1% | -3.8% | -58.5% | -27.3% | +24.1% | +77.9% | 54% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.4% | +1349.7% | -1351.5% | +0.0% |
| 6m | -0.8% | +2699.3% | -2702.9% | +0.0% |
| 12m | -1.4% | +5398.6% | -5405.8% | +0.2% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +1.1% | 54% |
| bull +10pp / bear -10pp | +6.0% | 49% |
| bull -10pp / bear +10pp | -3.7% | 58% |
| residual vol -25% | +1.1% | 53% |
| residual vol +25% | +1.1% | 55% |

Reconciliation: 12m mean +1.13% vs probability-weighted target +1.13%. Every input is cited in the parameters file. A distribution, not a signal.
