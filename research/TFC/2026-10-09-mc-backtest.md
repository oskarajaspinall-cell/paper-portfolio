## Monte Carlo calibration backtest — TFC (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +16.5% | -25.3% / +29.9% | +20.6% | -34.8% / +43.3% |
| 2024-09-30 | +3.9% | -25.1% / +29.6% | -2.7% | -34.5% / +42.7% |
| 2024-12-31 | -6.3% | -24.2% / +28.3% | -0.0% | -33.2% / +40.8% |
| 2025-03-31 | +6.7% | -23.7% / +27.3% | +16.7% | -32.7% / +39.4% |
| 2025-06-30 | +9.3% | -24.2% / +28.1% | +21.6% | -33.1% / +40.3% |
| 2025-09-30 | +11.3% | -23.5% / +27.3% | -1.1% | -32.2% / +39.1% |
| 2025-12-31 | -11.1% | -23.2% / +27.0% | +1.8% | -31.9% / +38.9% |
| 2026-03-31 | +14.6% | -22.0% / +25.0% | +9.2% | -30.2% / +36.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
