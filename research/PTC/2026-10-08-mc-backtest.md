## Monte Carlo calibration backtest — PTC (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 2/8 (25%) |
| 6m | 6/8 (75%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -0.7% | -18.7% / +20.9% | +5.9% | -25.8% / +30.4% |
| 2024-09-30 | +1.3% | -18.9% / +21.2% | -15.0% | -26.1% / +30.7% |
| 2024-12-31 | -16.1% | -18.5% / +20.7% | -8.2% | -25.5% / +30.0% |
| 2025-03-31 | +9.4% | -20.0% / +22.5% | +31.1% | -27.6% / +32.4% |
| 2025-06-30 | +19.9% | -19.7% / +22.4% | +4.3% | -27.1% / +32.4% |
| 2025-09-30 | -13.0% | -19.8% / +22.3% | -32.2% | -27.5% / +32.1% |
| 2025-12-31 | -22.1% | -20.4% / +23.1% | -34.5% | -28.3% / +33.2% |
| 2026-03-31 | -15.9% | -19.8% / +22.2% | +0.4% | -27.6% / +32.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
