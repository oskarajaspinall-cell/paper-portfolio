## Monte Carlo calibration backtest — CRM (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 5/8 (62%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +9.2% | -28.6% / +34.5% | +40.8% | -38.7% / +50.5% |
| 2024-09-30 | +22.5% | -28.6% / +34.6% | -2.3% | -38.8% / +50.3% |
| 2024-12-31 | -20.2% | -28.3% / +34.1% | -19.0% | -38.4% / +49.6% |
| 2025-03-31 | +1.6% | -27.5% / +32.9% | -9.4% | -37.3% / +47.8% |
| 2025-06-30 | -10.8% | -25.9% / +30.8% | -2.4% | -35.3% / +44.7% |
| 2025-09-30 | +9.5% | -24.9% / +29.4% | -26.2% | -34.2% / +42.6% |
| 2025-12-31 | -32.6% | -23.7% / +27.7% | -40.2% | -32.5% / +39.7% |
| 2026-03-31 | -11.2% | -25.4% / +30.0% | +31.4% | -34.8% / +43.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
