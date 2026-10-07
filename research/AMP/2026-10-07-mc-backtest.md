## Monte Carlo calibration backtest — AMP (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +4.9% | -20.7% / +24.2% | +21.5% | -28.8% / +34.3% |
| 2024-09-30 | +14.7% | -21.8% / +25.6% | +3.5% | -30.1% / +36.3% |
| 2024-12-31 | -9.8% | -22.2% / +26.2% | -0.9% | -30.7% / +37.1% |
| 2025-03-31 | +9.9% | -21.6% / +25.3% | +4.2% | -29.9% / +36.4% |
| 2025-06-30 | -5.1% | -21.5% / +25.3% | -4.3% | -29.9% / +36.0% |
| 2025-09-30 | +0.9% | -20.2% / +23.6% | -11.9% | -28.0% / +33.5% |
| 2025-12-31 | -12.7% | -19.6% / +22.4% | -9.2% | -26.9% / +32.1% |
| 2026-03-31 | +4.0% | -20.2% / +22.8% | +13.6% | -27.8% / +32.9% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
