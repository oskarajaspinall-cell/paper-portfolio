## Monte Carlo calibration backtest — WDAY (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 6/8 (75%) |
| 6m | 5/8 (62%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +13.3% | -27.8% / +33.0% | +24.6% | -37.9% / +48.0% |
| 2024-09-30 | +9.3% | -28.1% / +33.3% | -2.1% | -38.3% / +48.3% |
| 2024-12-31 | -10.4% | -27.8% / +32.9% | -10.8% | -37.9% / +47.9% |
| 2025-03-31 | -0.5% | -27.2% / +32.0% | +3.4% | -37.2% / +46.7% |
| 2025-06-30 | +3.9% | -26.5% / +31.2% | -7.0% | -36.2% / +44.9% |
| 2025-09-30 | -10.5% | -26.0% / +30.5% | -49.7% | -35.7% / +44.2% |
| 2025-12-31 | -43.7% | -23.5% / +27.4% | -43.7% | -32.4% / +39.7% |
| 2026-03-31 | +0.0% | -27.2% / +32.7% | +52.6% | -37.1% / +46.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
