## Monte Carlo calibration backtest — HBAN (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +18.9% | -24.8% / +28.8% | +31.8% | -33.8% / +41.9% |
| 2024-09-30 | +12.9% | -25.7% / +29.9% | +3.0% | -34.9% / +43.4% |
| 2024-12-31 | -8.8% | -24.6% / +28.7% | +3.4% | -33.6% / +41.7% |
| 2025-03-31 | +13.4% | -23.5% / +27.4% | +20.0% | -32.4% / +39.6% |
| 2025-06-30 | +5.9% | -24.3% / +28.5% | +8.8% | -33.3% / +41.3% |
| 2025-09-30 | +2.7% | -23.1% / +26.8% | -11.8% | -31.8% / +38.8% |
| 2025-12-31 | -14.1% | -23.5% / +27.4% | +2.2% | -32.2% / +39.4% |
| 2026-03-31 | +19.0% | -23.7% / +27.7% | +5.7% | -32.5% / +39.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
