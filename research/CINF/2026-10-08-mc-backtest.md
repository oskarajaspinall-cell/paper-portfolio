## Monte Carlo calibration backtest — CINF (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +17.6% | -19.0% / +21.5% | +26.9% | -26.3% / +30.5% |
| 2024-09-30 | +6.8% | -18.8% / +21.0% | +8.6% | -26.1% / +29.7% |
| 2024-12-31 | +1.6% | -19.3% / +21.7% | +2.7% | -26.8% / +30.5% |
| 2025-03-31 | +1.1% | -19.4% / +21.7% | +9.1% | -27.0% / +30.6% |
| 2025-06-30 | +7.9% | -18.8% / +21.0% | +13.9% | -26.2% / +29.6% |
| 2025-09-30 | +5.6% | -17.3% / +19.2% | -1.0% | -24.3% / +27.0% |
| 2025-12-31 | -6.2% | -17.3% / +19.0% | +13.0% | -24.1% / +27.0% |
| 2026-03-31 | +20.4% | -16.2% / +17.7% | +7.0% | -22.6% / +25.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
