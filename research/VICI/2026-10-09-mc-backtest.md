## Monte Carlo calibration backtest — VICI (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +19.2% | -15.7% / +17.2% | +5.3% | -21.7% / +24.9% |
| 2024-09-30 | -11.4% | -16.1% / +17.6% | -0.7% | -22.4% / +25.1% |
| 2024-12-31 | +12.1% | -15.9% / +17.4% | +14.6% | -22.3% / +24.7% |
| 2025-03-31 | +2.2% | -15.8% / +17.2% | +4.3% | -22.1% / +24.3% |
| 2025-06-30 | +2.0% | -15.1% / +16.1% | -10.2% | -20.9% / +22.9% |
| 2025-09-30 | -12.0% | -13.9% / +14.8% | -15.4% | -19.5% / +21.2% |
| 2025-12-31 | -3.9% | -14.2% / +15.2% | -0.0% | -19.9% / +21.8% |
| 2026-03-31 | +4.0% | -14.2% / +15.3% | -8.4% | -19.7% / +21.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
