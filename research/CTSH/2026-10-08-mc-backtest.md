## Monte Carlo calibration backtest — CTSH (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 5/8 (62%) | 3/8 (38%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +11.1% | -20.2% / +22.7% | +16.9% | -27.7% / +32.7% |
| 2024-09-30 | +3.4% | -19.2% / +21.5% | -0.6% | -26.4% / +30.8% |
| 2024-12-31 | -3.8% | -19.1% / +21.4% | -1.1% | -26.2% / +31.0% |
| 2025-03-31 | +2.8% | -19.6% / +22.0% | -11.0% | -27.0% / +31.8% |
| 2025-06-30 | -13.5% | -19.4% / +21.9% | +11.0% | -26.7% / +31.5% |
| 2025-09-30 | +28.3% | -19.7% / +22.1% | -10.0% | -27.2% / +31.9% |
| 2025-12-31 | -29.8% | -18.8% / +21.1% | -52.6% | -26.3% / +30.0% |
| 2026-03-31 | -32.5% | -21.1% / +23.9% | -2.8% | -29.3% / +34.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
