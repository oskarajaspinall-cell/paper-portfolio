## Monte Carlo calibration backtest — ZTS (2026-10-07)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 3/8 (38%) |
| 6m | 6/8 (75%) | 3/8 (38%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +12.9% | -23.1% / +26.6% | -3.2% | -31.5% / +38.6% |
| 2024-09-30 | -15.3% | -22.1% / +25.3% | -15.8% | -30.3% / +36.5% |
| 2024-12-31 | -0.6% | -22.3% / +25.6% | -4.5% | -30.8% / +36.5% |
| 2025-03-31 | -3.9% | -21.8% / +24.6% | -11.4% | -30.1% / +35.2% |
| 2025-06-30 | -7.8% | -20.5% / +23.1% | -18.6% | -28.4% / +33.0% |
| 2025-09-30 | -11.7% | -20.0% / +22.4% | -20.4% | -27.7% / +31.8% |
| 2025-12-31 | -9.8% | -21.3% / +24.1% | -39.2% | -29.5% / +34.2% |
| 2026-03-31 | -32.6% | -20.2% / +22.7% | -36.6% | -28.0% / +32.3% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
