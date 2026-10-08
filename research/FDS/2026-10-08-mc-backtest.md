## Monte Carlo calibration backtest — FDS (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 4/8 (50%) |
| 6m | 5/8 (62%) | 2/8 (25%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +10.2% | -19.5% / +22.0% | +14.6% | -27.0% / +31.7% |
| 2024-09-30 | +6.3% | -19.2% / +21.6% | -1.7% | -26.6% / +31.2% |
| 2024-12-31 | -7.6% | -19.3% / +21.6% | -8.9% | -26.8% / +31.3% |
| 2025-03-31 | -1.4% | -18.4% / +20.6% | -35.1% | -25.7% / +29.7% |
| 2025-06-30 | -34.2% | -17.2% / +18.8% | -33.4% | -24.0% / +27.2% |
| 2025-09-30 | +1.2% | -21.4% / +24.4% | -30.9% | -29.8% / +34.4% |
| 2025-12-31 | -31.8% | -21.1% / +23.8% | -19.9% | -29.2% / +34.0% |
| 2026-03-31 | +17.4% | -26.3% / +30.5% | +38.9% | -35.9% / +44.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
