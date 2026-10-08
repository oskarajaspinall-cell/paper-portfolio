## Monte Carlo calibration backtest — MCD (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 6/8 (75%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +15.1% | -14.4% / +15.5% | +14.2% | -20.3% / +22.3% |
| 2024-09-30 | -2.7% | -15.7% / +17.2% | +2.3% | -22.1% / +24.2% |
| 2024-12-31 | +5.2% | -15.6% / +16.9% | +0.4% | -21.8% / +23.9% |
| 2025-03-31 | -4.5% | -16.1% / +17.5% | +0.5% | -22.4% / +25.0% |
| 2025-06-30 | +5.3% | -15.2% / +16.3% | +7.8% | -21.2% / +23.4% |
| 2025-09-30 | +2.4% | -13.8% / +14.9% | +1.4% | -19.4% / +21.2% |
| 2025-12-31 | -1.0% | -13.3% / +14.2% | -12.1% | -18.6% / +20.4% |
| 2026-03-31 | -11.2% | -12.7% / +13.6% | -21.6% | -17.8% / +19.5% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
