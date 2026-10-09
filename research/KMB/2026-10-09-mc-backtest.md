## Monte Carlo calibration backtest — KMB (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +1.8% | -14.6% / +15.7% | -4.2% | -20.5% / +22.4% |
| 2024-09-30 | -6.7% | -14.1% / +15.1% | +0.5% | -19.8% / +21.7% |
| 2024-12-31 | +7.7% | -14.5% / +15.5% | -1.2% | -20.3% / +22.3% |
| 2025-03-31 | -8.3% | -14.7% / +15.8% | -11.5% | -20.5% / +22.6% |
| 2025-06-30 | -3.5% | -14.9% / +16.2% | -19.3% | -20.8% / +23.3% |
| 2025-09-30 | -16.4% | -14.9% / +16.1% | -17.3% | -20.8% / +23.3% |
| 2025-12-31 | -1.1% | -16.7% / +18.0% | +11.1% | -23.1% / +26.2% |
| 2026-03-31 | +12.4% | -17.1% / +18.5% | +2.4% | -23.5% / +27.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
