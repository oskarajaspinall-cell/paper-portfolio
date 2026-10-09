## Monte Carlo calibration backtest — FIS (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +11.1% | -25.6% / +29.9% | +8.2% | -35.2% / +43.3% |
| 2024-09-30 | -1.4% | -24.2% / +28.0% | -10.5% | -33.3% / +40.5% |
| 2024-12-31 | -9.2% | -23.8% / +27.5% | +0.1% | -32.6% / +39.7% |
| 2025-03-31 | +10.2% | -25.4% / +29.8% | -11.8% | -35.1% / +42.5% |
| 2025-06-30 | -20.0% | -25.1% / +29.4% | -15.8% | -34.6% / +41.8% |
| 2025-09-30 | +5.2% | -25.1% / +29.1% | -25.9% | -34.4% / +41.6% |
| 2025-12-31 | -29.6% | -21.4% / +24.4% | -41.4% | -29.6% / +34.7% |
| 2026-03-31 | -16.8% | -20.1% / +22.6% | -22.7% | -27.9% / +32.3% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
