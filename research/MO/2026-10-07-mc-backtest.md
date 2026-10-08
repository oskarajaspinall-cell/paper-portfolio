## Monte Carlo calibration backtest — MO (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 2/8 (25%) |
| 6m | 7/8 (88%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +12.3% | -15.1% / +16.3% | +20.0% | -21.0% / +23.1% |
| 2024-09-30 | +4.6% | -15.1% / +16.3% | +18.2% | -21.2% / +23.2% |
| 2024-12-31 | +13.0% | -15.2% / +16.5% | +16.2% | -21.3% / +23.4% |
| 2025-03-31 | +2.8% | -14.8% / +16.1% | +16.8% | -20.7% / +22.9% |
| 2025-06-30 | +13.7% | -13.4% / +14.2% | +1.5% | -18.7% / +20.5% |
| 2025-09-30 | -10.7% | -13.2% / +14.0% | +4.7% | -18.4% / +20.1% |
| 2025-12-31 | +17.4% | -14.7% / +15.8% | +32.2% | -20.5% / +22.9% |
| 2026-03-31 | +12.7% | -15.7% / +17.0% | +6.7% | -21.8% / +24.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
