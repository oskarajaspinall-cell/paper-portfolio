## Monte Carlo calibration backtest — TGT (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 7/8 (88%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +6.7% | -28.3% / +33.8% | -8.7% | -38.7% / +48.5% |
| 2024-09-30 | -12.1% | -28.2% / +33.8% | -32.1% | -38.6% / +48.5% |
| 2024-12-31 | -22.9% | -29.2% / +35.0% | -25.3% | -39.8% / +50.1% |
| 2025-03-31 | -3.2% | -29.2% / +35.2% | -13.3% | -39.9% / +50.6% |
| 2025-06-30 | -10.5% | -25.3% / +29.5% | +2.7% | -34.8% / +42.2% |
| 2025-09-30 | +14.7% | -24.5% / +28.3% | +39.5% | -33.6% / +40.4% |
| 2025-12-31 | +21.6% | -21.3% / +24.1% | +43.8% | -29.5% / +34.3% |
| 2026-03-31 | +18.3% | -21.6% / +24.6% | +33.6% | -29.8% / +34.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
