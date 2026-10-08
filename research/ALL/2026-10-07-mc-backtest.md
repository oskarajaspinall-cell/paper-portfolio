## Monte Carlo calibration backtest — ALL (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +19.6% | -20.2% / +22.4% | +21.7% | -27.7% / +32.0% |
| 2024-09-30 | +3.3% | -19.3% / +21.3% | +10.6% | -26.5% / +30.3% |
| 2024-12-31 | +7.1% | -19.5% / +21.8% | +2.0% | -26.9% / +31.2% |
| 2025-03-31 | -4.7% | -19.4% / +21.7% | +4.1% | -26.8% / +30.7% |
| 2025-06-30 | +9.2% | -19.0% / +20.9% | +7.2% | -26.0% / +29.7% |
| 2025-09-30 | -1.9% | -17.4% / +19.0% | -3.8% | -24.1% / +27.0% |
| 2025-12-31 | -2.0% | -17.9% / +19.6% | +16.5% | -24.7% / +27.7% |
| 2026-03-31 | +18.8% | -17.4% / +19.0% | +13.3% | -24.1% / +27.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
