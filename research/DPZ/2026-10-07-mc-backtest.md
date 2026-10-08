## Monte Carlo calibration backtest — DPZ (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -20.3% | -21.1% / +23.8% | -17.8% | -29.2% / +34.5% |
| 2024-09-30 | +0.5% | -23.7% / +27.4% | +5.0% | -32.8% / +38.9% |
| 2024-12-31 | +4.5% | -23.7% / +27.3% | +4.7% | -32.7% / +38.8% |
| 2025-03-31 | +0.2% | -24.4% / +28.2% | -1.8% | -33.5% / +40.3% |
| 2025-06-30 | -2.0% | -24.2% / +27.9% | -3.9% | -33.3% / +40.0% |
| 2025-09-30 | -1.9% | -22.0% / +24.9% | -19.4% | -30.4% / +35.8% |
| 2025-12-31 | -17.8% | -21.7% / +24.6% | -29.1% | -30.1% / +35.2% |
| 2026-03-31 | -13.8% | -20.7% / +23.2% | -15.0% | -28.7% / +33.3% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
