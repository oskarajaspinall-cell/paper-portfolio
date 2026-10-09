## Monte Carlo calibration backtest — BF.B (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 5/8 (62%) |
| 6m | 6/8 (75%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +6.9% | -19.1% / +21.5% | -4.4% | -26.7% / +30.3% |
| 2024-09-30 | -19.3% | -19.2% / +21.5% | -28.0% | -26.8% / +30.4% |
| 2024-12-31 | -10.8% | -20.2% / +22.8% | -30.8% | -28.1% / +32.4% |
| 2025-03-31 | -22.5% | -21.3% / +24.2% | -20.0% | -29.5% / +34.1% |
| 2025-06-30 | +3.2% | -23.8% / +27.5% | +0.5% | -32.8% / +39.3% |
| 2025-09-30 | -2.6% | -24.7% / +28.6% | +2.1% | -33.9% / +41.1% |
| 2025-12-31 | +4.8% | -24.9% / +28.8% | +8.7% | -33.9% / +41.2% |
| 2026-03-31 | +3.7% | -27.1% / +31.6% | -2.1% | -36.9% / +46.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
