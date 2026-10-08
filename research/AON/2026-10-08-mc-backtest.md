## Monte Carlo calibration backtest — AON (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 4/8 (50%) |
| 6m | 8/8 (100%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +16.9% | -18.8% / +21.1% | +21.0% | -26.2% / +30.2% |
| 2024-09-30 | +3.8% | -18.9% / +21.0% | +13.9% | -26.3% / +29.8% |
| 2024-12-31 | +9.7% | -18.5% / +20.6% | -1.7% | -25.8% / +29.3% |
| 2025-03-31 | -10.4% | -17.8% / +19.8% | -9.4% | -24.9% / +27.8% |
| 2025-06-30 | +1.2% | -17.0% / +18.7% | +1.5% | -23.8% / +26.4% |
| 2025-09-30 | +0.4% | -16.6% / +18.2% | -11.5% | -23.1% / +25.8% |
| 2025-12-31 | -11.9% | -16.3% / +17.7% | -7.4% | -22.7% / +25.2% |
| 2026-03-31 | +5.1% | -16.9% / +18.4% | -10.9% | -23.4% / +26.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
