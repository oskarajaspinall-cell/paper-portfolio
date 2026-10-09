## Monte Carlo calibration backtest — MA (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +8.5% | -16.9% / +18.8% | +16.4% | -23.4% / +27.4% |
| 2024-09-30 | +8.0% | -17.2% / +19.2% | +9.8% | -23.7% / +27.7% |
| 2024-12-31 | +1.7% | -16.4% / +18.2% | +3.7% | -22.8% / +26.3% |
| 2025-03-31 | +2.0% | -16.0% / +17.6% | +4.8% | -22.1% / +25.6% |
| 2025-06-30 | +2.8% | -16.1% / +17.9% | +5.6% | -22.4% / +25.7% |
| 2025-09-30 | +2.7% | -15.0% / +16.4% | -14.1% | -20.8% / +23.6% |
| 2025-12-31 | -16.3% | -14.6% / +15.8% | -13.6% | -20.4% / +22.7% |
| 2026-03-31 | +3.2% | -15.2% / +16.6% | +17.6% | -21.3% / +23.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
