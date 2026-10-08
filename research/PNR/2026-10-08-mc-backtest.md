## Monte Carlo calibration backtest — PNR (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 3/8 (38%) |
| 6m | 6/8 (75%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +19.6% | -20.9% / +24.2% | +29.0% | -28.6% / +34.7% |
| 2024-09-30 | +4.5% | -22.3% / +25.7% | -10.0% | -30.6% / +37.2% |
| 2024-12-31 | -13.9% | -21.8% / +25.0% | +3.0% | -30.0% / +36.4% |
| 2025-03-31 | +19.6% | -22.0% / +25.3% | +27.1% | -30.2% / +36.8% |
| 2025-06-30 | +6.2% | -22.6% / +26.3% | +2.5% | -30.8% / +38.1% |
| 2025-09-30 | -3.5% | -20.1% / +22.9% | -22.3% | -27.5% / +33.3% |
| 2025-12-31 | -19.4% | -19.4% / +22.1% | -27.3% | -26.7% / +31.9% |
| 2026-03-31 | -9.7% | -19.2% / +21.5% | -36.3% | -26.5% / +31.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
