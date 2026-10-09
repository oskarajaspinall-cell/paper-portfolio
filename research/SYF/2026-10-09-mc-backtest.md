## Monte Carlo calibration backtest — SYF (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 0/8 (0%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +14.4% | -25.7% / +30.4% | +48.7% | -35.2% / +43.8% |
| 2024-09-30 | +33.4% | -26.5% / +31.5% | +6.5% | -36.0% / +45.7% |
| 2024-12-31 | -20.2% | -26.2% / +31.3% | +1.3% | -35.8% / +45.1% |
| 2025-03-31 | +26.9% | -25.8% / +30.6% | +43.6% | -35.2% / +44.2% |
| 2025-06-30 | +13.1% | -25.8% / +30.7% | +31.0% | -35.3% / +44.3% |
| 2025-09-30 | +15.9% | -24.6% / +29.2% | -11.6% | -33.6% / +41.9% |
| 2025-12-31 | -23.7% | -23.4% / +27.3% | -7.8% | -32.1% / +39.2% |
| 2026-03-31 | +20.8% | -23.7% / +27.5% | +12.5% | -32.3% / +39.7% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
