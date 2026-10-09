## Monte Carlo calibration backtest — PEP (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +3.1% | -13.0% / +13.9% | -7.2% | -18.3% / +19.5% |
| 2024-09-30 | -9.3% | -13.2% / +14.1% | -10.7% | -18.6% / +20.1% |
| 2024-12-31 | -1.5% | -13.4% / +14.3% | -12.6% | -18.9% / +20.5% |
| 2025-03-31 | -11.2% | -14.2% / +15.4% | -4.0% | -20.0% / +21.9% |
| 2025-06-30 | +8.2% | -13.6% / +14.6% | +11.9% | -19.0% / +21.0% |
| 2025-09-30 | +3.4% | -14.1% / +15.1% | +11.0% | -19.7% / +21.9% |
| 2025-12-31 | +7.4% | -14.6% / +15.6% | +0.3% | -20.2% / +22.8% |
| 2026-03-31 | -6.6% | -16.4% / +17.8% | -14.2% | -22.7% / +26.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
