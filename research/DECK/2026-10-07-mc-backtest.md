## Monte Carlo calibration backtest — DECK (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 6/8 (75%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -7.7% | -27.4% / +32.5% | +29.1% | -37.3% / +46.5% |
| 2024-09-30 | +29.9% | -28.0% / +33.6% | -30.0% | -38.2% / +48.1% |
| 2024-12-31 | -46.1% | -27.0% / +32.1% | -49.7% | -36.8% / +45.8% |
| 2025-03-31 | -6.6% | -28.4% / +34.4% | -5.2% | -38.8% / +49.2% |
| 2025-06-30 | +1.5% | -29.6% / +36.0% | -1.1% | -40.3% / +52.0% |
| 2025-09-30 | -2.5% | -31.0% / +37.6% | -11.1% | -41.7% / +54.4% |
| 2025-12-31 | -8.8% | -32.2% / +39.7% | +1.4% | -43.3% / +57.2% |
| 2026-03-31 | +11.2% | -32.8% / +40.5% | -16.4% | -44.0% / +58.6% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
