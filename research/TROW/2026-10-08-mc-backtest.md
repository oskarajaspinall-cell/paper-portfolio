## Monte Carlo calibration backtest — TROW (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -7.5% | -25.4% / +30.5% | +0.3% | -34.6% / +44.4% |
| 2024-09-30 | +6.7% | -24.6% / +29.4% | -14.3% | -33.6% / +42.8% |
| 2024-12-31 | -19.7% | -24.4% / +29.1% | -14.6% | -33.4% / +42.3% |
| 2025-03-31 | +6.4% | -24.1% / +28.7% | +15.9% | -33.0% / +41.5% |
| 2025-06-30 | +9.0% | -23.1% / +27.5% | +11.7% | -31.6% / +39.7% |
| 2025-09-30 | +2.5% | -22.7% / +26.7% | -12.2% | -30.9% / +38.6% |
| 2025-12-31 | -14.3% | -19.2% / +21.7% | +8.1% | -26.3% / +31.6% |
| 2026-03-31 | +26.2% | -18.8% / +21.4% | +22.2% | -25.9% / +30.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
