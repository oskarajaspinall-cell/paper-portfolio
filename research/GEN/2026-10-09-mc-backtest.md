## Monte Carlo calibration backtest — GEN (2026-10-09)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 6/8 (75%) | 4/8 (50%) |
| 6m | 7/8 (88%) | 5/8 (62%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +9.9% | -22.7% / +26.1% | +16.0% | -31.4% / +37.1% |
| 2024-09-30 | +1.1% | -22.0% / +25.1% | -2.9% | -30.5% / +35.8% |
| 2024-12-31 | -4.0% | -21.8% / +24.9% | +6.8% | -30.2% / +35.4% |
| 2025-03-31 | +11.3% | -20.5% / +23.2% | +9.9% | -28.6% / +33.3% |
| 2025-06-30 | -1.2% | -20.2% / +23.0% | -4.3% | -28.1% / +33.0% |
| 2025-09-30 | -3.1% | -21.0% / +24.0% | -35.7% | -29.0% / +34.4% |
| 2025-12-31 | -33.6% | -20.6% / +23.6% | -11.0% | -28.5% / +33.8% |
| 2026-03-31 | +34.0% | -22.2% / +25.4% | +19.0% | -30.7% / +36.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
