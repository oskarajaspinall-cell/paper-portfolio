## Monte Carlo — CRM (2026-10-08)
10,000 paths (scenario mix allocated exactly), seed 20261007, Student-t (df 4.5) residual noise, correlated factor paths and event jumps. Start 224.56 USD (close 2026-10-07).
Factor regression (156 weekly returns, 2023-10-09 to 2026-09-28): R² 0.21; residual vol 39.6% (50/50 blend of 52w/156w weekly residual vol, annualised x sqrt(52)).

| Factor | Beta | Expected 12m move | Uncertainty |
|---|---|---|---|
| SPY | +1.21 | +0.0% | 14.3% |
| IEF | -0.00 | -5.0% | 6.5% |

| Scenario | Probability | 12m target | Target return | Band |
|---|---|---|---|---|
| bull | 25% | 288.26 | +28.4% | ±6% |
| base | 45% | 242.6 | +8.0% | ±0% |
| bear | 30% | 175.43 | -21.9% | ±11% |

| Jump | Annual probability | Impact | Analogue |
|---|---|---|---|
| Quarterly earnings reaction | 76% | -13.9% | week of 2024-05-28 (-13.9%) |
| Competitive AI-disruption shock (e.g. a large rival's enterprise-AI launch) | 30% | -15.0% | none (stated assumption) |
| Agentforce security-vulnerability disclosure/exploit | 20% | -10.0% | none (stated assumption) |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) |
|---|---|---|---|---|---|---|---|
| 3m | +0.9% | -0.9% | -31.8% | -14.3% | +14.4% | +38.6% | 52% |
| 6m | +1.4% | -2.6% | -43.3% | -21.5% | +19.3% | +60.1% | 53% |
| 12m | +4.1% | -5.8% | -57.6% | -31.3% | +28.4% | +98.7% | 56% |

Attribution of the mean log return:

| Horizon | Factor | Scenario | Jumps | Noise |
|---|---|---|---|---|
| 3m | -0.0% | +6.0% | -7.4% | +0.1% |
| 6m | -0.1% | +11.4% | -15.0% | +0.0% |
| 12m | +0.1% | +22.4% | -29.7% | +0.5% |

Sensitivity (12m):

| Case | Mean | P(loss) |
|---|---|---|
| probabilities as researched | +4.1% | 56% |
| bull +10pp / bear -10pp | +9.2% | 51% |
| bull -10pp / bear +10pp | -0.9% | 60% |
| residual vol -25% | +4.1% | 52% |
| residual vol +25% | +4.1% | 58% |

Reconciliation: 12m mean +4.14% vs probability-weighted target +4.14%. Every input is cited in the parameters file. A distribution, not a signal.
