## Monte Carlo calibration backtest — BAC (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +2.6% | -23.0% / +26.6% | +13.2% | -31.5% / +38.5% |
| 2024-09-30 | +13.2% | -22.9% / +26.5% | +5.9% | -31.4% / +38.1% |
| 2024-12-31 | -6.4% | -22.0% / +25.5% | +7.6% | -30.1% / +36.6% |
| 2025-03-31 | +14.9% | -21.2% / +24.5% | +28.0% | -29.4% / +35.3% |
| 2025-06-30 | +11.4% | -22.1% / +26.0% | +20.5% | -30.7% / +37.4% |
| 2025-09-30 | +8.1% | -21.7% / +25.3% | -9.1% | -30.0% / +36.3% |
| 2025-12-31 | -15.9% | -20.7% / +24.1% | +4.2% | -28.8% / +34.6% |
| 2026-03-31 | +23.9% | -20.5% / +23.5% | +22.0% | -28.4% / +33.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
