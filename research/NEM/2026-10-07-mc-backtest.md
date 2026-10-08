## Monte Carlo calibration backtest — NEM (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 2/8 (25%) |
| 6m | 5/8 (62%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +29.5% | -26.7% / +31.4% | -8.4% | -36.3% / +45.9% |
| 2024-09-30 | -29.4% | -26.3% / +31.0% | -9.7% | -36.0% / +45.1% |
| 2024-12-31 | +27.8% | -27.5% / +32.7% | +51.6% | -37.4% / +47.7% |
| 2025-03-31 | +18.6% | -26.9% / +31.6% | +78.7% | -36.6% / +46.0% |
| 2025-06-30 | +50.7% | -29.8% / +35.7% | +87.5% | -40.5% / +52.2% |
| 2025-09-30 | +24.4% | -30.5% / +37.2% | +20.4% | -41.5% / +53.7% |
| 2025-12-31 | -3.3% | -29.7% / +35.5% | -8.7% | -40.4% / +51.9% |
| 2026-03-31 | -5.6% | -32.0% / +39.0% | +19.5% | -43.2% / +57.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
