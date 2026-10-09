## Monte Carlo calibration backtest — BSX (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 1/8 (12%) |
| 6m | 5/8 (62%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +8.0% | -16.2% / +17.9% | +14.5% | -22.5% / +25.9% |
| 2024-09-30 | +8.8% | -15.7% / +17.2% | +19.2% | -21.8% / +24.9% |
| 2024-12-31 | +9.6% | -14.9% / +16.3% | +17.5% | -20.8% / +23.6% |
| 2025-03-31 | +7.2% | -14.9% / +16.3% | -1.2% | -20.7% / +23.5% |
| 2025-06-30 | -7.8% | -15.3% / +16.7% | -9.8% | -21.2% / +24.1% |
| 2025-09-30 | -2.2% | -15.2% / +16.5% | -29.5% | -21.3% / +23.6% |
| 2025-12-31 | -28.0% | -15.9% / +17.4% | -54.0% | -22.3% / +24.9% |
| 2026-03-31 | -36.1% | -21.0% / +23.8% | -36.5% | -29.2% / +33.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
