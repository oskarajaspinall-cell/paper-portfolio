## Monte Carlo calibration backtest — SCHW (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 8/8 (100%) | 6/8 (75%) |
| 6m | 8/8 (100%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | -10.5% | -27.3% / +32.7% | +2.1% | -37.2% / +47.2% |
| 2024-09-30 | +16.4% | -28.4% / +34.4% | +21.6% | -38.7% / +49.8% |
| 2024-12-31 | +4.5% | -27.9% / +33.6% | +21.2% | -38.0% / +48.7% |
| 2025-03-31 | +16.0% | -27.2% / +32.6% | +23.4% | -37.3% / +47.2% |
| 2025-06-30 | +6.4% | -25.9% / +30.9% | +13.9% | -35.5% / +44.7% |
| 2025-09-30 | +7.0% | -23.1% / +26.9% | -2.6% | -31.7% / +38.7% |
| 2025-12-31 | -9.0% | -21.5% / +24.7% | -10.4% | -29.6% / +35.5% |
| 2026-03-31 | -1.5% | -19.9% / +22.6% | +7.9% | -27.4% / +32.4% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
