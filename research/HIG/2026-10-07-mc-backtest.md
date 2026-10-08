## Monte Carlo calibration backtest — HIG (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +13.5% | -16.1% / +17.7% | +7.2% | -22.4% / +25.4% |
| 2024-09-30 | -5.3% | -16.1% / +17.6% | +5.6% | -22.4% / +25.4% |
| 2024-12-31 | +11.5% | -17.8% / +19.9% | +14.2% | -24.6% / +28.3% |
| 2025-03-31 | +2.4% | -17.7% / +19.6% | +9.8% | -24.7% / +27.7% |
| 2025-06-30 | +7.2% | -16.7% / +18.4% | +12.2% | -23.3% / +25.8% |
| 2025-09-30 | +4.6% | -15.7% / +17.1% | +0.3% | -21.9% / +24.2% |
| 2025-12-31 | -4.2% | -15.3% / +16.6% | -2.6% | -21.4% / +23.7% |
| 2026-03-31 | +1.7% | -15.0% / +16.4% | -5.3% | -21.1% / +22.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
