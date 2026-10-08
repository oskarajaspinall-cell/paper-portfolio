## Monte Carlo calibration backtest — INCY (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 3/8 (38%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +4.0% | -18.9% / +21.1% | +8.9% | -26.3% / +30.0% |
| 2024-09-30 | +5.2% | -21.0% / +23.7% | -7.9% | -29.0% / +33.7% |
| 2024-12-31 | -12.5% | -24.0% / +27.7% | -1.2% | -32.9% / +39.4% |
| 2025-03-31 | +12.8% | -24.2% / +28.0% | +36.5% | -33.2% / +39.9% |
| 2025-06-30 | +21.0% | -24.6% / +28.3% | +46.4% | -33.8% / +41.2% |
| 2025-09-30 | +21.1% | -24.3% / +28.2% | +9.2% | -33.5% / +40.7% |
| 2025-12-31 | -9.8% | -23.8% / +27.4% | +13.6% | -32.9% / +39.7% |
| 2026-03-31 | +26.0% | -23.8% / +27.6% | +37.2% | -32.8% / +39.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
