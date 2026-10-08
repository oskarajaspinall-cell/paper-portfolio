## Monte Carlo calibration backtest — BMY (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 5/8 (62%) | 4/8 (50%) |
| 6m | 6/8 (75%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +19.6% | -17.0% / +18.4% | +40.4% | -23.6% / +26.4% |
| 2024-09-30 | +14.6% | -20.4% / +22.7% | +20.5% | -28.2% / +32.7% |
| 2024-12-31 | +5.2% | -20.9% / +23.3% | -17.9% | -28.8% / +33.4% |
| 2025-03-31 | -21.9% | -21.4% / +24.0% | -24.7% | -29.5% / +34.6% |
| 2025-06-30 | -3.6% | -22.2% / +25.2% | +21.1% | -30.6% / +36.3% |
| 2025-09-30 | +25.5% | -20.8% / +23.3% | +36.1% | -28.7% / +33.3% |
| 2025-12-31 | +8.4% | -20.5% / +22.8% | +7.6% | -28.3% / +32.7% |
| 2026-03-31 | -0.7% | -20.8% / +23.4% | +9.7% | -28.8% / +33.6% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
