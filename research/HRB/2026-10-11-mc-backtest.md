## Monte Carlo calibration backtest — HRB (2026-10-11)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +21.9% | -22.4% / +25.4% | +4.2% | -31.0% / +36.9% |
| 2024-09-30 | -15.5% | -21.6% / +24.5% | -13.8% | -29.9% / +35.2% |
| 2024-12-31 | +2.0% | -21.0% / +23.5% | +3.8% | -29.1% / +34.1% |
| 2025-03-31 | +1.8% | -21.7% / +24.5% | -6.3% | -29.9% / +35.6% |
| 2025-06-30 | -7.9% | -20.8% / +23.2% | -18.5% | -28.6% / +33.3% |
| 2025-09-30 | -11.5% | -20.0% / +22.3% | -36.0% | -27.7% / +32.2% |
| 2025-12-31 | -27.7% | -20.8% / +23.4% | -12.9% | -28.7% / +33.7% |
| 2026-03-31 | +20.6% | -23.7% / +27.1% | +37.9% | -32.6% / +39.1% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
