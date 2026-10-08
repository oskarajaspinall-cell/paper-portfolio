## Monte Carlo calibration backtest — PYPL (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +26.6% | -31.0% / +37.9% | +43.8% | -42.0% / +55.1% |
| 2024-09-30 | +11.5% | -30.4% / +36.9% | -16.3% | -41.2% / +53.6% |
| 2024-12-31 | -25.0% | -30.3% / +36.8% | -15.2% | -41.1% / +53.7% |
| 2025-03-31 | +13.0% | -28.8% / +34.7% | +3.3% | -39.3% / +50.4% |
| 2025-06-30 | -8.6% | -27.1% / +32.1% | -18.4% | -36.9% / +46.7% |
| 2025-09-30 | -10.7% | -27.2% / +32.4% | -34.9% | -37.2% / +47.2% |
| 2025-12-31 | -27.1% | -25.2% / +29.5% | -25.7% | -34.7% / +42.6% |
| 2026-03-31 | +1.9% | -28.9% / +35.1% | +27.0% | -39.5% / +50.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
