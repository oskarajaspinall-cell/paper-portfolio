## Monte Carlo calibration backtest — STZ (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 6/8 (75%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -5.5% | -15.8% / +17.5% | -12.9% | -22.0% / +24.8% |
| 2024-09-30 | -13.4% | -16.2% / +17.8% | -28.2% | -22.5% / +25.4% |
| 2024-12-31 | -17.0% | -15.9% / +17.5% | -26.7% | -22.2% / +24.8% |
| 2025-03-31 | -11.7% | -20.4% / +23.0% | -27.1% | -28.2% / +32.7% |
| 2025-06-30 | -17.4% | -20.5% / +23.0% | -12.4% | -28.3% / +32.8% |
| 2025-09-30 | +6.0% | -21.4% / +24.2% | +15.9% | -29.4% / +34.4% |
| 2025-12-31 | +9.3% | -22.4% / +25.4% | +6.3% | -30.9% / +36.5% |
| 2026-03-31 | -2.7% | -21.0% / +23.5% | -23.9% | -29.0% / +33.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
