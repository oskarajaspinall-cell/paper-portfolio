## Monte Carlo calibration backtest — LULU (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 0/8 (0%) |
| 6m | 7/8 (88%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -15.8% | -28.6% / +34.2% | +21.7% | -39.2% / +49.7% |
| 2024-09-30 | +38.1% | -28.8% / +34.6% | +4.7% | -39.3% / +50.0% |
| 2024-12-31 | -24.2% | -31.3% / +38.3% | -39.2% | -42.4% / +54.8% |
| 2025-03-31 | -19.8% | -31.1% / +38.1% | -39.8% | -42.3% / +54.3% |
| 2025-06-30 | -25.0% | -32.3% / +40.1% | -11.1% | -43.7% / +57.4% |
| 2025-09-30 | +18.5% | -33.7% / +42.0% | -17.3% | -45.3% / +60.8% |
| 2025-12-31 | -30.2% | -31.2% / +38.0% | -43.7% | -41.9% / +54.7% |
| 2026-03-31 | -19.4% | -30.8% / +37.5% | -30.5% | -41.5% / +54.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
