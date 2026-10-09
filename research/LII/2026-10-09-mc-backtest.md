## Monte Carlo calibration backtest — LII (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 6/8 (75%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +13.0% | -23.3% / +27.1% | +16.2% | -32.0% / +39.5% |
| 2024-09-30 | +2.7% | -22.7% / +26.2% | -8.2% | -31.0% / +38.1% |
| 2024-12-31 | -10.6% | -22.8% / +26.3% | -8.1% | -31.2% / +38.2% |
| 2025-03-31 | +2.8% | -23.0% / +26.7% | -5.2% | -31.5% / +38.8% |
| 2025-06-30 | -7.8% | -22.8% / +26.1% | -11.8% | -31.3% / +37.6% |
| 2025-09-30 | -4.3% | -23.4% / +27.2% | -15.7% | -32.3% / +39.3% |
| 2025-12-31 | -11.9% | -23.2% / +27.0% | +13.8% | -32.0% / +38.8% |
| 2026-03-31 | +29.2% | -23.5% / +27.3% | -14.2% | -32.6% / +39.0% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
