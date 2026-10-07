## Monte Carlo — HKG:9999 (2026-10-07)
10,000 scenario-weighted paths, seed 20261007, jump-diffusion with Student-t (df 4.5) innovations. Start: 185.6 HKD (close 2026-10-06). Baseline volatility 35.1% (123 daily log returns, 2026-04-09 to 2026-10-06; https://stockanalysis.com/quote/hkg/9999/history/).

| Scenario | Probability | 12m target | Drift (annualised) | Vol multiplier |
|---|---|---|---|---|
| bull | 25% | 226.0 | +19.7% | 0.9 |
| base | 50% | 196.6 | +5.8% | 1.0 |
| bear | 25% | 157.8 | -16.2% | 1.3 |

| Horizon | Mean | Median | P5 | P25 | P75 | P95 | P(loss) | Paths bull / base / bear |
|---|---|---|---|---|---|---|---|---|
| 3m | +2.8% | +1.4% | -26.1% | -10.4% | +14.5% | +35.9% | 47% | 25% / 49% / 26% |
| 6m | +5.9% | +2.9% | -35.1% | -13.8% | +22.2% | +56.3% | 45% | 25% / 49% / 26% |
| 12m | +12.3% | +5.7% | -46.2% | -18.2% | +36.1% | +92.3% | 44% | 25% / 49% / 26% |

Every input is cited in the parameters file. This is a distribution of outcomes, not a signal.
