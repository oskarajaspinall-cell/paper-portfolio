## Monte Carlo calibration backtest — ACGL (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 6/8 (75%) |
| 6m | 8/8 (100%) | 7/8 (88%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +11.1% | -18.5% / +20.5% | -6.1% | -25.6% / +29.3% |
| 2024-09-30 | -14.4% | -17.9% / +19.8% | -11.9% | -24.8% / +28.3% |
| 2024-12-31 | +2.9% | -18.6% / +20.7% | -2.2% | -25.8% / +29.6% |
| 2025-03-31 | -5.0% | -18.9% / +21.1% | -4.4% | -26.3% / +29.9% |
| 2025-06-30 | +0.6% | -18.6% / +20.6% | +6.1% | -25.5% / +29.3% |
| 2025-09-30 | +5.5% | -18.0% / +19.7% | +2.8% | -24.8% / +28.0% |
| 2025-12-31 | -2.6% | -16.8% / +18.2% | +1.7% | -23.4% / +26.1% |
| 2026-03-31 | +4.4% | -16.1% / +17.5% | +1.3% | -22.4% / +24.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
