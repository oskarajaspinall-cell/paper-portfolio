## Monte Carlo calibration backtest — ACN (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 3/8 (38%) |
| 6m | 7/8 (88%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +9.3% | -22.2% / +25.8% | +19.6% | -30.4% / +37.3% |
| 2024-09-30 | +2.3% | -22.3% / +25.5% | -12.2% | -30.5% / +37.2% |
| 2024-12-31 | -14.2% | -22.4% / +25.7% | -16.3% | -30.8% / +37.2% |
| 2025-03-31 | -2.4% | -21.9% / +25.1% | -20.7% | -30.1% / +36.1% |
| 2025-06-30 | -18.7% | -20.7% / +23.4% | -7.2% | -28.5% / +33.8% |
| 2025-09-30 | +14.2% | -21.2% / +24.1% | -18.4% | -29.4% / +34.6% |
| 2025-12-31 | -28.5% | -20.1% / +22.8% | -51.7% | -27.9% / +32.1% |
| 2026-03-31 | -32.5% | -21.6% / +24.5% | -6.7% | -29.7% / +35.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
