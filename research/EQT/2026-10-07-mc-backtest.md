## Monte Carlo calibration backtest — EQT (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -5.3% | -30.2% / +36.8% | +17.4% | -40.9% / +53.1% |
| 2024-09-30 | +21.8% | -29.3% / +35.5% | +46.2% | -39.9% / +51.4% |
| 2024-12-31 | +20.0% | -29.4% / +35.9% | +32.3% | -39.9% / +51.6% |
| 2025-03-31 | +10.3% | -27.8% / +33.4% | +2.6% | -37.8% / +47.5% |
| 2025-06-30 | -7.0% | -26.3% / +31.3% | -7.0% | -35.9% / +44.7% |
| 2025-09-30 | +0.1% | -27.4% / +32.1% | +25.7% | -37.2% / +46.1% |
| 2025-12-31 | +25.6% | -26.9% / +31.5% | -1.7% | -36.5% / +45.3% |
| 2026-03-31 | -21.8% | -26.2% / +30.6% | -24.3% | -35.7% / +43.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
