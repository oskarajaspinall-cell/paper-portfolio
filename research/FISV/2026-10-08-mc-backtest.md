## Monte Carlo calibration backtest — FISV (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 5/8 (62%) | 3/8 (38%) |
| 6m | 4/8 (50%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +18.6% | -16.7% / +18.6% | +37.6% | -23.1% / +26.7% |
| 2024-09-30 | +16.6% | -16.1% / +17.9% | +21.2% | -22.4% / +25.8% |
| 2024-12-31 | +3.9% | -16.7% / +18.5% | -17.1% | -23.2% / +26.8% |
| 2025-03-31 | -20.3% | -17.2% / +19.1% | -40.1% | -23.9% / +27.4% |
| 2025-06-30 | -24.8% | -21.5% / +24.5% | -60.8% | -29.7% / +34.6% |
| 2025-09-30 | -47.9% | -23.0% / +26.3% | -58.4% | -31.6% / +37.5% |
| 2025-12-31 | -20.1% | -40.2% / +52.0% | -26.7% | -53.0% / +76.1% |
| 2026-03-31 | -8.3% | -40.4% / +52.3% | -13.8% | -53.3% / +76.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
