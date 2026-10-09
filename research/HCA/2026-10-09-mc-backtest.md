## Monte Carlo calibration backtest — HCA (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 1/8 (12%) |
| 6m | 8/8 (100%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +19.6% | -22.1% / +25.4% | -10.1% | -30.5% / +36.7% |
| 2024-09-30 | -24.8% | -22.1% / +25.3% | -14.8% | -30.6% / +36.8% |
| 2024-12-31 | +13.4% | -23.5% / +27.0% | +25.9% | -32.4% / +38.7% |
| 2025-03-31 | +11.1% | -24.3% / +28.1% | +22.9% | -33.4% / +40.0% |
| 2025-06-30 | +10.7% | -22.3% / +25.2% | +26.2% | -30.7% / +36.2% |
| 2025-09-30 | +14.0% | -21.5% / +24.4% | +12.9% | -29.7% / +34.9% |
| 2025-12-31 | -1.0% | -19.8% / +22.1% | -17.6% | -27.5% / +32.0% |
| 2026-03-31 | -16.8% | -19.6% / +21.7% | -7.3% | -27.2% / +31.5% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
