## Monte Carlo calibration backtest — INTU (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 5/8 (62%) | 5/8 (62%) |
| 6m | 6/8 (75%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +2.2% | -25.6% / +30.6% | +2.1% | -34.6% / +44.4% |
| 2024-09-30 | +3.3% | -25.5% / +30.2% | -2.9% | -34.4% / +43.8% |
| 2024-12-31 | -6.1% | -25.1% / +29.9% | +22.0% | -34.2% / +43.4% |
| 2025-03-31 | +29.9% | -24.8% / +29.1% | +16.9% | -33.8% / +42.2% |
| 2025-06-30 | -10.0% | -23.0% / +26.4% | -12.6% | -31.6% / +38.2% |
| 2025-09-30 | -2.9% | -22.5% / +25.8% | -40.1% | -31.2% / +36.9% |
| 2025-12-31 | -38.3% | -20.5% / +23.2% | -60.2% | -28.5% / +32.9% |
| 2026-03-31 | -35.5% | -28.0% / +33.4% | -33.3% | -38.2% / +47.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
