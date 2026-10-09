## Monte Carlo calibration backtest — CB (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +10.2% | -15.0% / +16.3% | +3.9% | -20.9% / +23.4% |
| 2024-09-30 | -3.8% | -14.6% / +16.0% | +3.0% | -20.3% / +22.7% |
| 2024-12-31 | +7.1% | -15.1% / +16.5% | +3.4% | -21.1% / +23.3% |
| 2025-03-31 | -3.5% | -15.6% / +17.0% | -4.7% | -21.9% / +24.1% |
| 2025-06-30 | -1.2% | -14.8% / +15.9% | +10.7% | -20.7% / +22.7% |
| 2025-09-30 | +12.0% | -14.1% / +15.0% | +14.4% | -19.6% / +21.3% |
| 2025-12-31 | +2.1% | -14.3% / +15.2% | +9.6% | -19.9% / +21.7% |
| 2026-03-31 | +7.3% | -13.6% / +14.4% | +5.1% | -19.0% / +20.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
