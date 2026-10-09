## Monte Carlo calibration backtest — MKC (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +21.6% | -20.6% / +23.3% | +16.1% | -28.6% / +33.3% |
| 2024-09-30 | -7.0% | -20.2% / +22.8% | -1.0% | -27.9% / +32.6% |
| 2024-12-31 | +6.3% | -18.7% / +20.8% | +0.2% | -25.9% / +29.9% |
| 2025-03-31 | -5.8% | -17.8% / +19.6% | -18.4% | -24.7% / +28.2% |
| 2025-06-30 | -13.4% | -16.8% / +18.4% | -8.5% | -23.4% / +26.5% |
| 2025-09-30 | +5.6% | -16.5% / +18.0% | -18.1% | -22.9% / +25.9% |
| 2025-12-31 | -22.5% | -17.2% / +18.8% | -24.8% | -23.7% / +27.5% |
| 2026-03-31 | -2.9% | -20.4% / +22.8% | -8.0% | -27.9% / +33.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
