## Monte Carlo calibration backtest — APP (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 2/8 (25%) |
| 6m | 5/8 (62%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +60.5% | -44.3% / +61.1% | +333.9% | -57.9% / +89.3% |
| 2024-09-30 | +162.4% | -44.8% / +62.3% | +113.2% | -58.5% / +90.3% |
| 2024-12-31 | -18.7% | -51.9% / +77.2% | -0.4% | -66.6% / +112.4% |
| 2025-03-31 | +22.5% | -54.0% / +82.1% | +145.9% | -68.7% / +120.0% |
| 2025-06-30 | +100.7% | -54.7% / +83.5% | +114.0% | -69.4% / +122.9% |
| 2025-09-30 | +6.6% | -53.8% / +80.8% | -43.1% | -68.5% / +118.9% |
| 2025-12-31 | -46.6% | -49.6% / +71.7% | -33.2% | -63.9% / +105.0% |
| 2026-03-31 | +25.2% | -48.9% / +70.3% | -18.5% | -63.1% / +103.8% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
