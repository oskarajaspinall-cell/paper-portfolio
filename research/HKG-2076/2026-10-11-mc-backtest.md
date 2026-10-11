## Monte Carlo calibration backtest — HKG:2076 (2026-10-11)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 4/4 (100%) | 2/4 (50%) |
| 6m | 4/4 (100%) | 2/4 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | skipped: only 59 common completed weeks (need >= 104) [missing] | | | |
| 2024-09-30 | skipped: only 71 common completed weeks (need >= 104) [missing] | | | |
| 2024-12-31 | skipped: only 84 common completed weeks (need >= 104) [missing] | | | |
| 2025-03-31 | skipped: only 95 common completed weeks (need >= 104) [missing] | | | |
| 2025-06-30 | +28.8% | -36.2% / +47.1% | +15.1% | -48.5% / +69.9% |
| 2025-09-30 | -10.6% | -35.7% / +46.3% | -39.9% | -47.9% / +68.7% |
| 2025-12-31 | -32.7% | -35.5% / +45.9% | -38.7% | -47.6% / +68.0% |
| 2026-03-31 | -8.9% | -35.2% / +45.4% | +2.6% | -47.1% / +67.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
