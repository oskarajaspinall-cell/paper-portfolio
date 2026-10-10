## Monte Carlo calibration backtest — GDDY (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 3/8 (38%) |
| 6m | 5/8 (62%) | 1/8 (12%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +16.6% | -23.0% / +26.7% | +49.2% | -31.6% / +38.8% |
| 2024-09-30 | +30.4% | -23.5% / +27.2% | +14.7% | -32.1% / +39.4% |
| 2024-12-31 | -12.1% | -22.7% / +26.2% | -11.5% | -31.1% / +38.0% |
| 2025-03-31 | +0.7% | -24.2% / +28.0% | -21.0% | -33.1% / +40.6% |
| 2025-06-30 | -21.5% | -24.0% / +27.7% | -29.4% | -33.0% / +40.1% |
| 2025-09-30 | -10.1% | -25.8% / +30.3% | -43.4% | -35.5% / +43.3% |
| 2025-12-31 | -37.1% | -23.6% / +27.4% | -33.5% | -32.5% / +38.9% |
| 2026-03-31 | +5.7% | -25.2% / +29.5% | +21.5% | -34.5% / +41.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
