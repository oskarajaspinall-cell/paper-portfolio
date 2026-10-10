## Monte Carlo calibration backtest — OTIS (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +0.0% | -15.9% / +17.6% | -1.7% | -22.0% / +25.4% |
| 2024-09-30 | -10.1% | -16.7% / +18.5% | -1.4% | -23.1% / +26.5% |
| 2024-12-31 | +9.6% | -16.8% / +18.6% | +5.2% | -23.3% / +26.9% |
| 2025-03-31 | -4.0% | -16.7% / +18.3% | -10.7% | -23.1% / +26.2% |
| 2025-06-30 | -7.0% | -16.9% / +18.5% | -9.4% | -23.6% / +26.7% |
| 2025-09-30 | -2.6% | -16.5% / +18.1% | -15.2% | -23.1% / +25.6% |
| 2025-12-31 | -12.9% | -16.0% / +17.4% | -15.6% | -22.4% / +24.8% |
| 2026-03-31 | -3.1% | -16.5% / +18.1% | -12.1% | -23.1% / +25.6% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
