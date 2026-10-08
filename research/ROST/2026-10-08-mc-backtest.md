## Monte Carlo calibration backtest — ROST (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 6/8 (75%) | 1/8 (12%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +3.6% | -21.7% / +25.1% | +0.4% | -29.9% / +36.1% |
| 2024-09-30 | +1.2% | -21.5% / +24.6% | -16.8% | -29.5% / +35.5% |
| 2024-12-31 | -17.7% | -21.7% / +24.8% | -15.9% | -29.8% / +35.8% |
| 2025-03-31 | +2.3% | -22.4% / +25.6% | +21.5% | -30.9% / +36.9% |
| 2025-06-30 | +18.8% | -20.7% / +23.5% | +42.3% | -28.9% / +33.4% |
| 2025-09-30 | +19.8% | -20.3% / +22.9% | +40.3% | -28.2% / +32.4% |
| 2025-12-31 | +17.1% | -19.6% / +22.1% | +18.2% | -27.4% / +31.1% |
| 2026-03-31 | +0.9% | -18.5% / +20.7% | +12.0% | -25.9% / +29.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
