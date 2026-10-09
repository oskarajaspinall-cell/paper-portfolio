## Monte Carlo calibration backtest — HON (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -4.9% | -15.8% / +17.3% | +7.3% | -22.0% / +25.0% |
| 2024-09-30 | +11.1% | -15.4% / +16.8% | +2.3% | -21.3% / +24.3% |
| 2024-12-31 | -7.9% | -16.5% / +18.1% | +0.7% | -23.0% / +25.9% |
| 2025-03-31 | +9.4% | -17.0% / +18.6% | -0.0% | -23.8% / +26.7% |
| 2025-06-30 | -8.6% | -17.7% / +19.5% | -7.5% | -24.7% / +28.1% |
| 2025-09-30 | +1.2% | -17.2% / +19.0% | +14.9% | -23.9% / +27.3% |
| 2025-12-31 | +13.6% | -16.3% / +18.0% | +18.9% | -22.9% / +25.8% |
| 2026-03-31 | +4.7% | -16.3% / +17.9% | -8.4% | -22.8% / +25.5% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
