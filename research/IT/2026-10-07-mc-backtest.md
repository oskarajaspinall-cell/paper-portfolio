## Monte Carlo calibration backtest — IT (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 4/8 (50%) |
| 6m | 4/8 (50%) | 1/8 (12%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +13.6% | -21.9% / +25.2% | +8.7% | -30.1% / +36.2% |
| 2024-09-30 | -4.3% | -21.3% / +24.3% | -17.8% | -29.3% / +34.7% |
| 2024-12-31 | -14.1% | -20.0% / +22.7% | -17.3% | -27.7% / +32.8% |
| 2025-03-31 | -3.7% | -20.2% / +23.0% | -36.9% | -27.9% / +33.2% |
| 2025-06-30 | -34.4% | -19.3% / +21.9% | -37.3% | -26.7% / +31.4% |
| 2025-09-30 | -4.3% | -28.7% / +34.3% | -41.1% | -38.9% / +49.5% |
| 2025-12-31 | -38.5% | -29.3% / +35.2% | -46.6% | -39.6% / +50.6% |
| 2026-03-31 | -13.2% | -33.8% / +41.8% | +20.9% | -45.3% / +60.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
